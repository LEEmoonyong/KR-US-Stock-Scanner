"""
기사 3줄 요약 생성 및 품질 관리 모듈.
- 노이즈(저작권, 광고, 기자명 등) 제거
- 기사와 무관한 내용 필터링
- 제목과의 관련성 검증
"""
import re


# === 노이즈 패턴 (기사 본문/요약에서 제거) ===
NOISE_PATTERNS = [
    (r"\S+@\S+\.\w+", " "),
    (r"<[^>]*저작권[^>]*>", " ", re.I),
    (r"저작권자\s*\([cC]\)\s*[^>]+", " "),
    (r"무단전재\s*및\s*재배포\s*금지[^.]*\.?", " "),
    (r"AI\s*학습\s*및\s*활용\s*금지[^.]*\.?", " "),
    (r"[\d]{4}\.\s*[\d]{1,2}\.\s*[\d]{1,2}\s*[ⓒ©\(c\)]?\s*", " "),
    (r"[ⓒ©]\s*[A-Za-z]+=[^\s,]+", " "),
    (r"관련\s*키워드[^\n]*(?=\n|$)", " "),
    (r"관련\s*기사[^\n]*(?=\n|$)", " "),
    (r"\[시황종합\]|\[장중시황\]|\[종목현미경\]|\[2보\]|\[1보\]", " "),
    (r"=\s*뉴스\d|=\s*연합뉴스", " "),
    (r"댓글\s*많은\s*뉴스.{0,1200}?(?=\n\n|\Z)", " ", re.DOTALL),
    (r"많이\s*본\s*뉴스.{0,800}?(?=\n\n|\Z)", " ", re.DOTALL),
    (r"추천\s*기사.{0,500}?(?=\n\n|\Z)", " ", re.DOTALL),
    (r"\[뉴스캐비닛\].{0,600}?(?=\n\n|\Z)", " ", re.DOTALL),
    (r"시나리오\s*분석.{0,800}?(?=\n\n|\Z)", " ", re.DOTALL),
    (r"시나리오\s*\d+\s*:.{0,300}", " "),
    (r"\(수혜\s*산업[^)]*\).{0,400}", " "),
    (r"예상\s*확률\s*:\s*\d+%.{0,200}", " "),
    (r"후원은\s*더\s*좋은\s*기사에\s*도움이\s*됩니다[^.]*\.?", " "),
    (r"후원\s*하기|기사\s*후원하기|독자\s*후원", " "),
    (r"[가-힣]{2,4}/[가-힣]{2,4}\s*기자", " "),
    (r"[가-힣]{2,4}\s*기자\s*[가-힣]{2,4}\s*기자", " "),
    (r"\bADVERTISEMENT\b", " ", re.I),
    (r"AD\s*$|^\s*AD\b", " ", re.I),
    (r"스폰서\s*광고|Sponsored|Partner\s*Content", " ", re.I),
]

# === 문장 필터: 이 패턴이 있으면 요약에서 제외 ===
REJECT_SENTENCE_PATTERNS = [
    r"\S+@\S+\.\w+",
    r"저작권|무단전재|AI\s*학습",
    r"관련\s*키워드|관련\s*기사",
    r"댓글\s*많은|많이\s*본\s*뉴스|추천\s*기사",
    r"뉴스캐비닛|시나리오\s*분석|시나리오\s*\d+\s*:|예상\s*확률\s*:",
    r"후원은\s*더\s*좋은|후원\s*하기|기사\s*후원",
    r"[가-힣]{2,4}/[가-힣]{2,4}\s*기자",
    r"\bADVERTISEMENT\b",
    r"^\s*AD\s*$",
    r"스폰서|Sponsored",
]


def clean_article_noise(text: str) -> str:
    """기사 본문/요약에서 불필요한 노이즈 제거."""
    if not text or not str(text).strip():
        return ""
    s = str(text)
    for item in NOISE_PATTERNS:
        if len(item) == 3:
            pat, repl, flags = item
            s = re.sub(pat, repl, s, flags=flags)
        else:
            pat, repl = item
            s = re.sub(pat, repl, s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _is_boilerplate_sentence(s: str) -> bool:
    """문장이 메타데이터/보일러플레이트인지 판별."""
    c = clean_article_noise(s)
    if not c or len(c) < 15:
        return True
    for pat in REJECT_SENTENCE_PATTERNS:
        if re.search(pat, c):
            return True
    if len(re.findall(r"[가-힣]{2,4}\s*[\"'][^\"']+[\"']", c)) >= 4:
        return True
    return False


def _extract_keywords(text: str, min_len: int = 2) -> set:
    """텍스트에서 키워드 추출 (한글 2자 이상, 영문 3자 이상)."""
    if not text:
        return set()
    s = re.sub(r"[^\w\s가-힣a-zA-Z]", " ", str(text))
    words = s.split()
    out = set()
    for w in words:
        w = w.strip()
        if not w:
            continue
        if re.match(r"^[가-힣]+$", w) and len(w) >= min_len:
            out.add(w)
        elif re.match(r"^[a-zA-Z]+$", w) and len(w) >= 3:
            out.add(w.lower())
    return out


def _relevance_score(sentence: str, title: str) -> float:
    """
    문장이 제목과 얼마나 관련 있는지 점수 (0~1).
    제목 키워드와의 겹침 비율로 계산.
    """
    if not sentence or not title:
        return 0.0
    sent_kw = _extract_keywords(sentence)
    title_kw = _extract_keywords(title)
    if not title_kw:
        return 0.5
    overlap = len(sent_kw & title_kw) / len(title_kw)
    if overlap >= 0.3:
        return 0.8 + overlap * 0.2
    if overlap >= 0.1:
        return 0.5 + overlap
    return overlap * 2


def _is_likely_article_content(sentence: str) -> bool:
    """
    문장이 기사 본문 스타일인지 판별.
    - 너무 짧은 인사말/광고 문구 제외
    - 동사/서술형 패턴 포함 시 True
    """
    s = sentence.strip()
    if len(s) < 25:
        return False
    if re.match(r"^[^\w가-힣]*$", s):
        return False
    if re.search(r"(이다|했다|했다|된다|있다|없다|라고|이라고)[.\s]*$", s):
        return True
    if re.search(r"[가-힣]{3,}.*[을를이가은는]", s):
        return True
    if len(s) >= 40 and re.search(r"[가-힣a-zA-Z]", s):
        return True
    return len(s) >= 50


def extract_3_sentences(text: str, article_title: str = "") -> str:
    """
    본문에서 기사와 관련된 핵심 3문장 추출.
    article_title이 주어지면 관련성 검증 적용.
    """
    if not text or len(text.strip()) < 30:
        return ""
    text = clean_article_noise(text)
    if len(text.strip()) < 30:
        return ""
    text = re.sub(r"\s+", " ", str(text).strip())
    sentences = re.split(r"(?<=[.!?。])\s+", text)
    sentences = [s.strip() for s in sentences if s.strip() and 15 <= len(s) <= 500]
    if not sentences:
        sentences = [p.strip() for p in re.split(r"\s{2,}", text) if len(p.strip()) >= 20][:5]
    if not sentences:
        return ""
    candidates = []
    for s in sentences:
        if _is_boilerplate_sentence(s):
            continue
        cleaned = clean_article_noise(s)
        if not cleaned or len(cleaned) < 15:
            continue
        if not _is_likely_article_content(cleaned):
            continue
        score = _relevance_score(cleaned, article_title) if article_title else 0.6
        candidates.append((cleaned, score))
    if not candidates:
        return ""
    candidates.sort(key=lambda x: -x[1])
    selected = [c[0] for c in candidates[:5] if c[1] >= 0.15]
    if not selected and candidates:
        selected = [c[0] for c in candidates[:3]]
    return "\n".join(selected[:3])


def validate_summary(summary: str, article_title: str = "") -> str:
    """
    최종 요약에서 무관한 문장 제거.
    각 줄을 검증해 기사와 관련 없는 내용은 제거.
    """
    if not summary or not summary.strip():
        return ""
    lines = [ln.strip() for ln in summary.split("\n") if ln.strip()]
    out = []
    for line in lines:
        if _is_boilerplate_sentence(line):
            continue
        cleaned = clean_article_noise(line)
        if not cleaned or len(cleaned) < 15:
            continue
        if article_title and _relevance_score(cleaned, article_title) < 0.15:
            continue
        out.append(cleaned)
    return "\n".join(out[:3]) if out else ""
