# ticker_universe_kr.py
# -----------------------------
# 한국 증시 유니버스 — 코스피 200 + 코스닥 100
# Yahoo Finance: KOSPI=XXXXXX.KS, KOSDAQ=XXXXXX.KQ
# marcap 시총 상위, ETF/우선주 제외
# -----------------------------

# 코스피 200 (시총 상위)
KOSPI_200 = [
    "005930.KS",  # 삼성전자
    "000660.KS",  # SK하이닉스
    "005380.KS",  # 현대차
    "373220.KS",  # LG에너지솔루션
    "207940.KS",  # 삼성바이오로직스
    "402340.KS",  # SK스퀘어
    "000270.KS",  # 기아
    "034020.KS",  # 두산에너빌리티
    "012450.KS",  # 한화에어로스페이스
    "329180.KS",  # HD현대중공업
    "105560.KS",  # KB금융
    "028260.KS",  # 삼성물산
    "068270.KS",  # 셀트리온
    "055550.KS",  # 신한지주
    "042660.KS",  # 한화오션
    "032830.KS",  # 삼성생명
    "015760.KS",  # 한국전력
    "006800.KS",  # 미래에셋증권
    "012330.KS",  # 현대모비스
    "035420.KS",  # NAVER
    "086790.KS",  # 하나금융지주
    "267260.KS",  # HD현대일렉트릭
    "010130.KS",  # 고려아연
    "006400.KS",  # 삼성SDI
    "009540.KS",  # HD한국조선해양
    "005490.KS",  # POSCO홀딩스
    "316140.KS",  # 우리금융지주
    "000810.KS",  # 삼성화재
    "009150.KS",  # 삼성전기
    "034730.KS",  # SK
    "010140.KS",  # 삼성중공업
    "035720.KS",  # 카카오
    "138040.KS",  # 메리츠금융지주
    "298040.KS",  # 효성중공업
    "064350.KS",  # 현대로템
    "051910.KS",  # LG화학
    "267250.KS",  # HD현대
    "024110.KS",  # 기업은행
    "272210.KS",  # 한화시스템
    "011200.KS",  # HMM
    "096770.KS",  # SK이노베이션
    "033780.KS",  # KT&G
    "010120.KS",  # LS ELECTRIC
    "003670.KS",  # 포스코퓨처엠
    "086280.KS",  # 현대글로비스
    "066570.KS",  # LG전자
    "042700.KS",  # 한미반도체
    "030200.KS",  # KT
    "017670.KS",  # SK텔레콤
    "047810.KS",  # 한국항공우주
    "352820.KS",  # 하이브
    "000150.KS",  # 두산
    "071050.KS",  # 한국금융지주
    "003550.KS",  # LG
    "000720.KS",  # 현대건설
    "005940.KS",  # NH투자증권
    "323410.KS",  # 카카오뱅크
    "010950.KS",  # S-Oil
    "039490.KS",  # 키움증권
    "005830.KS",  # DB손해보험
    "018260.KS",  # 삼성에스디에스
    "047050.KS",  # 포스코인터내셔널
    "259960.KS",  # 크래프톤
    "307950.KS",  # 현대오토에버
    "278470.KS",  # 에이피알
    "079550.KS",  # LIG넥스원
    "016360.KS",  # 삼성증권
    "180640.KS",  # 한진칼
    "000880.KS",  # 한화
    "161390.KS",  # 한국타이어앤테크놀로지
    "003490.KS",  # 대한항공
    "090430.KS",  # 아모레퍼시픽
    "009830.KS",  # 한화솔루션
    "377300.KS",  # 카카오페이
    "000100.KS",  # 유한양행
    "003230.KS",  # 삼양식품
    "326030.KS",  # SK바이오팜
    "006260.KS",  # LS
    "443060.KS",  # HD현대마린솔루션
    "128940.KS",  # 한미약품
    "029780.KS",  # 삼성카드
    "032640.KS",  # LG유플러스
    "007660.KS",  # 이수페타시스
    "175330.KS",  # JB금융지주
    "078930.KS",  # GS
    "138930.KS",  # BNK금융지주
    "028050.KS",  # 삼성E&A
    "267270.KS",  # HD건설기계
    "064400.KS",  # LG씨엔에스
    "034220.KS",  # LG디스플레이
    "001040.KS",  # CJ
    "454910.KS",  # 두산로보틱스
    "241560.KS",  # 두산밥캣
    "021240.KS",  # 코웨이
    "052690.KS",  # 한전기술
    "001440.KS",  # 대한전선
    "011070.KS",  # LG이노텍
    "022100.KS",  # 포스코DX
    "088350.KS",  # 한화생명
    "088980.KS",  # 맥쿼리인프라
    "271560.KS",  # 오리온
    "004020.KS",  # 현대제철
    "002380.KS",  # KCC
    "018880.KS",  # 한온시스템
    "036570.KS",  # 엔씨소프트
    "251270.KS",  # 넷마블
    "082740.KS",  # 한화엔진
    "450080.KS",  # 에코프로머티
    "066970.KS",  # 엘앤에프
    "062040.KS",  # 산일전기
    "031210.KS",  # 서울보증보험
    "017800.KS",  # 현대엘리베이터
    "036460.KS",  # 한국가스공사
    "011790.KS",  # SKC
    "051900.KS",  # LG생활건강
    "035250.KS",  # 강원랜드
    "000990.KS",  # DB하이텍
    "001720.KS",  # 신영증권
    "302440.KS",  # SK바이오사이언스
    "111770.KS",  # 영원무역
    "004990.KS",  # 롯데지주
    "011780.KS",  # 금호석유화학
    "011170.KS",  # 롯데케미칼
    "014680.KS",  # 한솔케미칼
    "012750.KS",  # 에스원
    "139130.KS",  # iM금융지주
    "001450.KS",  # 현대해상
    "103590.KS",  # 일진전기
    "004170.KS",  # 신세계
    "097950.KS",  # CJ제일제당
    "000240.KS",  # 한국앤컴퍼니
    "047040.KS",  # 대우건설
    "103140.KS",  # 풍산
    "000120.KS",  # CJ대한통운
    "439260.KS",  # 대한조선
    "023530.KS",  # 롯데쇼핑
    "489790.KS",  # 한화비전
    "071970.KS",  # HD현대마린엔진
    "139480.KS",  # 이마트
    "009970.KS",  # 영원무역홀딩스
    "457190.KS",  # 이수스페셜티케미컬
    "012510.KS",  # 더존비즈온
    "026960.KS",  # 동서
    "008930.KS",  # 한미사이언스
    "353200.KS",  # 대덕전자
    "009420.KS",  # 한올바이오파마
    "028670.KS",  # 팬오션
    "010060.KS",  # OCI홀딩스
    "005850.KS",  # 에스엘
    "051600.KS",  # 한전KPS
    "204320.KS",  # HL만도
    "004800.KS",  # 효성
    "081660.KS",  # 미스토홀딩스
    "003690.KS",  # 코리안리
    "023590.KS",  # 다우기술
    "004370.KS",  # 농심
    "383220.KS",  # F&F
    "002790.KS",  # 아모레퍼시픽홀딩스
    "001430.KS",  # 세아베스틸지주
    "030000.KS",  # 제일기획
    "003540.KS",  # 대신증권
    "097230.KS",  # HJ중공업
    "069960.KS",  # 현대백화점
    "336260.KS",  # 두산퓨얼셀
    "282330.KS",  # BGF리테일
    "011210.KS",  # 현대위아
    "020150.KS",  # 롯데에너지머티리얼즈
    "018670.KS",  # SK가스
    "005440.KS",  # 현대지에프홀딩스
    "192820.KS",  # 코스맥스
    "085620.KS",  # 미래에셋생명
    "361610.KS",  # SK아이이테크놀로지
    "483650.KS",  # 달바글로벌
    "073240.KS",  # 금호타이어
    "006280.KS",  # 녹십자
    "112610.KS",  # 씨에스윈드
    "069620.KS",  # 대웅제약
    "003530.KS",  # 한화투자증권
    "017960.KS",  # 한국카본
    "462870.KS",  # 시프트업
    "006040.KS",  # 동원산업
    "375500.KS",  # DL이앤씨
    "006360.KS",  # GS건설
    "032350.KS",  # 롯데관광개발
    "003570.KS",  # SNT다이내믹스
    "030610.KS",  # 교보증권
    "008770.KS",  # 호텔신라
    "034230.KS",  # 파라다이스
    "007070.KS",  # GS리테일
    "001120.KS",  # LX인터내셔널
    "007340.KS",  # DN오토모티브
    "005070.KS",  # 코스모신소재
    "161890.KS",  # 한국콜마
    "298020.KS",  # 효성티앤씨
    "120110.KS",  # 코오롱인더
    "395400.KS",  # SK리츠
    "003090.KS",  # 대웅
    "007310.KS",  # 오뚜기
    "020560.KS",  # 아시아나항공
    "294870.KS",  # HDC현대산업개발
]

# 코스닥 100 (시총 상위)
KOSDAQ_100 = [
    "000250.KQ",  # 삼천당제약
    "277810.KQ",  # 레인보우로보틱스
    "298380.KQ",  # 에이비엘바이오
    "214370.KQ",  # 케어젠
    "950160.KQ",  # 코오롱티슈진
    "028300.KQ",  # HLB
    "087010.KQ",  # 펩트론
    "310210.KQ",  # 보로노이
    "140410.KQ",  # 메지온
    "108490.KQ",  # 로보티즈
    "347850.KQ",  # 디앤디파마텍
    "068760.KQ",  # 셀트리온제약
    "084370.KQ",  # 유진테크
    "319400.KQ",  # 현대무벡스
    "058610.KQ",  # 에스피지
    "290650.KQ",  # 엘앤씨바이오
    "005290.KQ",  # 동진쎄미켐
    "083650.KQ",  # 비에이치아이
    "030530.KQ",  # 원익홀딩스
    "257720.KQ",  # 실리콘투
    "226950.KQ",  # 올릭스
    "440110.KQ",  # 파두
    "032820.KQ",  # 우리기술
    "475830.KQ",  # 오름테라퓨틱
    "067310.KQ",  # 하나마이크론
    "323280.KQ",  # 태성
    "098460.KQ",  # 고영
    "178320.KQ",  # 서진시스템
    "347700.KQ",  # 스피어
    "065350.KQ",  # 신성델타테크
    "160190.KQ",  # 하이젠알앤엠
    "039200.KQ",  # 오스코텍
    "491000.KQ",  # 리브스메드
    "101490.KQ",  # 에스앤에스텍
    "082270.KQ",  # 젬백스
    "085660.KQ",  # 차바이오텍
    "099320.KQ",  # 쎄트렉아이
    "031980.KQ",  # 피에스케이홀딩스
    "458870.KQ",  # 씨어스테크놀로지
    "476830.KQ",  # 알지노믹스
    "445680.KQ",  # 큐리옥스바이오시스템즈
    "348370.KQ",  # 엔켐
    "232140.KQ",  # 와이씨
    "090710.KQ",  # 휴림로봇
    "089030.KQ",  # 테크윙
    "466100.KQ",  # 클로봇
    "218410.KQ",  # RFHIC
    "043260.KQ",  # 성호전자
    "060370.KQ",  # LS마린솔루션
    "080220.KQ",  # 제주반도체
    "038500.KQ",  # 삼표시멘트
    "437730.KQ",  # 삼현
    "397030.KQ",  # 에이프릴바이오
    "007390.KQ",  # 네이처셀
    "281740.KQ",  # 레이크머티리얼즈
    "456160.KQ",  # 지투지바이오
    "388210.KQ",  # 씨엠티엑스
    "096530.KQ",  # 씨젠
    "078600.KQ",  # 대주전자재료
    "095610.KQ",  # 테스
    "388720.KQ",  # 유일로보틱스
    "056080.KQ",  # 유진로봇
    "122870.KQ",  # 와이지엔터테인먼트
    "048410.KQ",  # 현대바이오
    "189300.KQ",  # 인텔리안테크
    "328130.KQ",  # 루닛
    "171090.KQ",  # 선익시스템
    "204270.KQ",  # 제이앤티씨
    "100790.KQ",  # 미래에셋벤처투자
    "036540.KQ",  # SFA반도체
    "115180.KQ",  # 큐리언트
    "127120.KQ",  # 제이에스링크
    "161580.KQ",  # 필옵틱스
    "032190.KQ",  # 다우데이타
    "006730.KQ",  # 서부T&D
    "124500.KQ",  # 아이티센글로벌
    "417200.KQ",  # LS머트리얼즈
    "241710.KQ",  # 코스메카코리아
    "174900.KQ",  # 앱클론
    "014620.KQ",  # 성광벤드
    "131290.KQ",  # 티에스이
    "376300.KQ",  # 디어유
    "295310.KQ",  # 에이치브이엠
    "490470.KQ",  # 세미파이브
    "086900.KQ",  # 메디톡스
    "348340.KQ",  # 뉴로메카
    "036810.KQ",  # 에프에스티
    "082920.KQ",  # 비츠로셀
    "112040.KQ",  # 위메이드
    "052400.KQ",  # 코나아이
    "358570.KQ",  # 지아이이노베이션
    "389470.KQ",  # 인벤티지랩
    "060250.KQ",  # NHN KCP
    "033500.KQ",  # 동성화인텍
    "033100.KQ",  # 제룡전기
    "214430.KQ",  # 아이쓰리시스템
    "121600.KQ",  # 나노신소재
    "376900.KQ",  # 로킷헬스케어
    "032500.KQ",  # 케이엠더블유
    "089970.KQ",  # 브이엠
]

# 추가 대표주 50종 (코스피/코스닥 — 에코프로비엠·에코프로·알테오젠 등 유니버스에 빠졌던 우량주)
ADDITIONAL_KR_50 = [
    "247540.KQ",  # 에코프로비엠
    "086520.KQ",  # 에코프로
    "196170.KQ",  # 알테오젠
    "058470.KQ",  # 리노공업
    "141080.KQ",  # 리가켐바이오
    "240810.KQ",  # 원익IPS
    "145020.KQ",  # 휴젤
    "214450.KQ",  # 파마리서치
    "079980.KS",  # 휴비스
    "005300.KS",  # 롯데칠성
    "035760.KS",  # CJ ENM
    "091990.KQ",  # 셀트리온헬스케어
    "383310.KQ",  # 에코프로HN
    "041510.KS",  # 에스엠
    "035900.KS",  # JYP엔터테인먼트
    "214150.KQ",  # 클래시스
    "357780.KQ",  # 솔브레인
    "006140.KS",  # 펄어비스
    "225220.KQ",  # 에임드바이오
    "237690.KQ",  # 에스티팜
    "140860.KQ",  # 파크시스템스
    "036930.KQ",  # 주성엔지니어링
    "064760.KQ",  # 티씨케이
    "222080.KQ",  # 심텍
    "403870.KQ",  # HPSP
    "424460.KQ",  # 이오테크닉스
    "095340.KQ",  # ISC
    "006120.KS",  # SK디스커버리
    "108320.KS",  # LX세미콘
    "000040.KS",  # KR모터스
    "265520.KQ",  # 에이프로시스템
    "293490.KQ",  # 카카오게임즈
    "095700.KQ",  # 제넥신
    "268600.KQ",  # 셀리버리
    "046430.KQ",  # 에스코어
    "304840.KQ",  # 피플바이오
    "246720.KQ",  # 아스타
    "261840.KQ",  # 엔젤로보틱스
    "376290.KQ",  # 셀렉트아이
    "054540.KQ",  # 키넥스
    "017810.KS",  # 풀무원
    "004540.KS",  # 깨끗한나라
    "192400.KS",  # 쿠쿠홀딩스
]

# 추가 시총 상위 50종 (343종 유니버스 제외, 코스피/코스닥 시총 51~150위 구간)
ADDITIONAL_KR_50_2 = [
    "001230.KS",  # 동국제강
    "004720.KS",  # 한솔홀딩스
    "009240.KS",  # 한샘
    "011000.KS",  # 한독
    "001740.KS",  # SK네트웍스
    "003000.KS",  # 부광약품
    "005250.KS",  # 청담러닝
    "005610.KS",  # SPC삼립
    "007160.KS",  # 쌍용양회
    "009260.KS",  # 로웰
    "017390.KS",  # 서울도시가스
    "018250.KS",  # 애경산업
    "020000.KS",  # 한섬
    "024070.KS",  # WISCOM
    "026940.KS",  # 부국철강
    "029460.KS",  # 케이씨텍
    "030350.KS",  # 크레인플러스
    "036530.KS",  # SNT홀딩스
    "037560.KS",  # CJ헬로
    "039020.KS",  # 이베스트투자증권
    "051380.KS",  # 피씨디
    "053690.KS",  # 한미글로벌
    "058430.KS",  # 에스폴리텍
    "065770.KS",  # CS홀딩스
    "071840.KS",  # 롯데하이마트
    "072710.KS",  # 농심홀딩스
    "079160.KS",  # CJ CGV
    "084690.KS",  # 대동공업
    "085310.KS",  # 이엔코퍼레이션
    "033290.KQ",  # 유티아이
    "043150.KQ",  # 바텍
    "052460.KQ",  # 코스맥스코리아
    "054630.KQ",  # 에이디엔에스
    "057540.KQ",  # 옴니시스템
    "073010.KQ",  # 케에스피
    "078340.KQ",  # 컴뱃
    "099220.KQ",  # SD바이오센서
    "099410.KQ",  # 동방생명
    "101670.KQ",  # 하이드로리튬
    "109610.KQ",  # 에스와이
    "131970.KQ",  # 두산테스나
    "136480.KQ",  # 하림
    "137400.KQ",  # 피엔티
    "143160.KQ",  # 비와이엔터프라이즈
    "149980.KQ",  # 하이로닉스
    "153460.KQ",  # 네이블
    "170920.KQ",  # 엘티씨
    "214390.KQ",  # 경보제약
    "227610.KQ",  # 아우딘퓨쳐스
    "033180.KS",  # KH필룩스
]

# 중복 제거 후 정렬 (KOSPI_200 + KOSDAQ_100 + ADDITIONAL_KR_50 + ADDITIONAL_KR_50_2)
TICKERS = sorted(list(dict.fromkeys(t.upper().strip() for t in KOSPI_200 + KOSDAQ_100 + ADDITIONAL_KR_50 + ADDITIONAL_KR_50_2)))

# 티커 → 회사명
TICKER_TO_NAME = {
    "005930.KS": "삼성전자",
    "000660.KS": "SK하이닉스",
    "005380.KS": "현대차",
    "373220.KS": "LG에너지솔루션",
    "207940.KS": "삼성바이오로직스",
    "402340.KS": "SK스퀘어",
    "000270.KS": "기아",
    "034020.KS": "두산에너빌리티",
    "012450.KS": "한화에어로스페이스",
    "329180.KS": "HD현대중공업",
    "105560.KS": "KB금융",
    "028260.KS": "삼성물산",
    "068270.KS": "셀트리온",
    "055550.KS": "신한지주",
    "042660.KS": "한화오션",
    "032830.KS": "삼성생명",
    "015760.KS": "한국전력",
    "006800.KS": "미래에셋증권",
    "012330.KS": "현대모비스",
    "035420.KS": "NAVER",
    "086790.KS": "하나금융지주",
    "267260.KS": "HD현대일렉트릭",
    "010130.KS": "고려아연",
    "006400.KS": "삼성SDI",
    "009540.KS": "HD한국조선해양",
    "005490.KS": "POSCO홀딩스",
    "316140.KS": "우리금융지주",
    "000810.KS": "삼성화재",
    "009150.KS": "삼성전기",
    "034730.KS": "SK",
    "010140.KS": "삼성중공업",
    "035720.KS": "카카오",
    "138040.KS": "메리츠금융지주",
    "298040.KS": "효성중공업",
    "064350.KS": "현대로템",
    "051910.KS": "LG화학",
    "267250.KS": "HD현대",
    "024110.KS": "기업은행",
    "272210.KS": "한화시스템",
    "011200.KS": "HMM",
    "096770.KS": "SK이노베이션",
    "033780.KS": "KT&G",
    "010120.KS": "LS ELECTRIC",
    "003670.KS": "포스코퓨처엠",
    "086280.KS": "현대글로비스",
    "066570.KS": "LG전자",
    "042700.KS": "한미반도체",
    "030200.KS": "KT",
    "017670.KS": "SK텔레콤",
    "047810.KS": "한국항공우주",
    "352820.KS": "하이브",
    "000150.KS": "두산",
    "071050.KS": "한국금융지주",
    "003550.KS": "LG",
    "000720.KS": "현대건설",
    "005940.KS": "NH투자증권",
    "323410.KS": "카카오뱅크",
    "010950.KS": "S-Oil",
    "039490.KS": "키움증권",
    "005830.KS": "DB손해보험",
    "018260.KS": "삼성에스디에스",
    "047050.KS": "포스코인터내셔널",
    "259960.KS": "크래프톤",
    "307950.KS": "현대오토에버",
    "278470.KS": "에이피알",
    "079550.KS": "LIG넥스원",
    "016360.KS": "삼성증권",
    "180640.KS": "한진칼",
    "000880.KS": "한화",
    "161390.KS": "한국타이어앤테크놀로지",
    "003490.KS": "대한항공",
    "090430.KS": "아모레퍼시픽",
    "009830.KS": "한화솔루션",
    "377300.KS": "카카오페이",
    "000100.KS": "유한양행",
    "003230.KS": "삼양식품",
    "326030.KS": "SK바이오팜",
    "006260.KS": "LS",
    "443060.KS": "HD현대마린솔루션",
    "128940.KS": "한미약품",
    "029780.KS": "삼성카드",
    "032640.KS": "LG유플러스",
    "007660.KS": "이수페타시스",
    "175330.KS": "JB금융지주",
    "078930.KS": "GS",
    "138930.KS": "BNK금융지주",
    "028050.KS": "삼성E&A",
    "267270.KS": "HD건설기계",
    "064400.KS": "LG씨엔에스",
    "034220.KS": "LG디스플레이",
    "001040.KS": "CJ",
    "454910.KS": "두산로보틱스",
    "241560.KS": "두산밥캣",
    "021240.KS": "코웨이",
    "052690.KS": "한전기술",
    "001440.KS": "대한전선",
    "011070.KS": "LG이노텍",
    "022100.KS": "포스코DX",
    "088350.KS": "한화생명",
    "088980.KS": "맥쿼리인프라",
    "271560.KS": "오리온",
    "004020.KS": "현대제철",
    "002380.KS": "KCC",
    "018880.KS": "한온시스템",
    "036570.KS": "엔씨소프트",
    "251270.KS": "넷마블",
    "082740.KS": "한화엔진",
    "450080.KS": "에코프로머티",
    "247540.KQ": "에코프로비엠",
    "086520.KQ": "에코프로",
    "066970.KS": "엘앤에프",
    "062040.KS": "산일전기",
    "031210.KS": "서울보증보험",
    "017800.KS": "현대엘리베이터",
    "036460.KS": "한국가스공사",
    "011790.KS": "SKC",
    "051900.KS": "LG생활건강",
    "035250.KS": "강원랜드",
    "000990.KS": "DB하이텍",
    "001720.KS": "신영증권",
    "302440.KS": "SK바이오사이언스",
    "111770.KS": "영원무역",
    "004990.KS": "롯데지주",
    "011780.KS": "금호석유화학",
    "011170.KS": "롯데케미칼",
    "014680.KS": "한솔케미칼",
    "012750.KS": "에스원",
    "139130.KS": "iM금융지주",
    "001450.KS": "현대해상",
    "103590.KS": "일진전기",
    "004170.KS": "신세계",
    "097950.KS": "CJ제일제당",
    "000240.KS": "한국앤컴퍼니",
    "047040.KS": "대우건설",
    "103140.KS": "풍산",
    "000120.KS": "CJ대한통운",
    "439260.KS": "대한조선",
    "023530.KS": "롯데쇼핑",
    "489790.KS": "한화비전",
    "071970.KS": "HD현대마린엔진",
    "139480.KS": "이마트",
    "009970.KS": "영원무역홀딩스",
    "457190.KS": "이수스페셜티케미컬",
    "012510.KS": "더존비즈온",
    "026960.KS": "동서",
    "008930.KS": "한미사이언스",
    "353200.KS": "대덕전자",
    "009420.KS": "한올바이오파마",
    "028670.KS": "팬오션",
    "010060.KS": "OCI홀딩스",
    "005850.KS": "에스엘",
    "051600.KS": "한전KPS",
    "204320.KS": "HL만도",
    "004800.KS": "효성",
    "081660.KS": "미스토홀딩스",
    "003690.KS": "코리안리",
    "023590.KS": "다우기술",
    "004370.KS": "농심",
    "383220.KS": "F&F",
    "002790.KS": "아모레퍼시픽홀딩스",
    "001430.KS": "세아베스틸지주",
    "030000.KS": "제일기획",
    "003540.KS": "대신증권",
    "097230.KS": "HJ중공업",
    "069960.KS": "현대백화점",
    "336260.KS": "두산퓨얼셀",
    "282330.KS": "BGF리테일",
    "011210.KS": "현대위아",
    "020150.KS": "롯데에너지머티리얼즈",
    "018670.KS": "SK가스",
    "005440.KS": "현대지에프홀딩스",
    "192820.KS": "코스맥스",
    "085620.KS": "미래에셋생명",
    "361610.KS": "SK아이이테크놀로지",
    "483650.KS": "달바글로벌",
    "073240.KS": "금호타이어",
    "006280.KS": "녹십자",
    "112610.KS": "씨에스윈드",
    "069620.KS": "대웅제약",
    "003530.KS": "한화투자증권",
    "017960.KS": "한국카본",
    "462870.KS": "시프트업",
    "006040.KS": "동원산업",
    "375500.KS": "DL이앤씨",
    "006360.KS": "GS건설",
    "032350.KS": "롯데관광개발",
    "003570.KS": "SNT다이내믹스",
    "030610.KS": "교보증권",
    "008770.KS": "호텔신라",
    "034230.KS": "파라다이스",
    "007070.KS": "GS리테일",
    "001120.KS": "LX인터내셔널",
    "007340.KS": "DN오토모티브",
    "005070.KS": "코스모신소재",
    "161890.KS": "한국콜마",
    "298020.KS": "효성티앤씨",
    "120110.KS": "코오롱인더",
    "395400.KS": "SK리츠",
    "003090.KS": "대웅",
    "007310.KS": "오뚜기",
    "020560.KS": "아시아나항공",
    "294870.KS": "HDC현대산업개발",
    "000250.KQ": "삼천당제약",
    "277810.KQ": "레인보우로보틱스",
    "298380.KQ": "에이비엘바이오",
    "214370.KQ": "케어젠",
    "950160.KQ": "코오롱티슈진",
    "028300.KQ": "HLB",
    "087010.KQ": "펩트론",
    "310210.KQ": "보로노이",
    "140410.KQ": "메지온",
    "108490.KQ": "로보티즈",
    "347850.KQ": "디앤디파마텍",
    "068760.KQ": "셀트리온제약",
    "084370.KQ": "유진테크",
    "319400.KQ": "현대무벡스",
    "058610.KQ": "에스피지",
    "290650.KQ": "엘앤씨바이오",
    "005290.KQ": "동진쎄미켐",
    "083650.KQ": "비에이치아이",
    "030530.KQ": "원익홀딩스",
    "257720.KQ": "실리콘투",
    "226950.KQ": "올릭스",
    "440110.KQ": "파두",
    "032820.KQ": "우리기술",
    "475830.KQ": "오름테라퓨틱",
    "067310.KQ": "하나마이크론",
    "323280.KQ": "태성",
    "098460.KQ": "고영",
    "178320.KQ": "서진시스템",
    "347700.KQ": "스피어",
    "065350.KQ": "신성델타테크",
    "160190.KQ": "하이젠알앤엠",
    "039200.KQ": "오스코텍",
    "491000.KQ": "리브스메드",
    "101490.KQ": "에스앤에스텍",
    "082270.KQ": "젬백스",
    "085660.KQ": "차바이오텍",
    "099320.KQ": "쎄트렉아이",
    "031980.KQ": "피에스케이홀딩스",
    "458870.KQ": "씨어스테크놀로지",
    "476830.KQ": "알지노믹스",
    "445680.KQ": "큐리옥스바이오시스템즈",
    "348370.KQ": "엔켐",
    "232140.KQ": "와이씨",
    "090710.KQ": "휴림로봇",
    "089030.KQ": "테크윙",
    "466100.KQ": "클로봇",
    "218410.KQ": "RFHIC",
    "043260.KQ": "성호전자",
    "060370.KQ": "LS마린솔루션",
    "080220.KQ": "제주반도체",
    "038500.KQ": "삼표시멘트",
    "437730.KQ": "삼현",
    "397030.KQ": "에이프릴바이오",
    "007390.KQ": "네이처셀",
    "281740.KQ": "레이크머티리얼즈",
    "456160.KQ": "지투지바이오",
    "388210.KQ": "씨엠티엑스",
    "096530.KQ": "씨젠",
    "078600.KQ": "대주전자재료",
    "095610.KQ": "테스",
    "388720.KQ": "유일로보틱스",
    "056080.KQ": "유진로봇",
    "122870.KQ": "와이지엔터테인먼트",
    "048410.KQ": "현대바이오",
    "189300.KQ": "인텔리안테크",
    "328130.KQ": "루닛",
    "171090.KQ": "선익시스템",
    "204270.KQ": "제이앤티씨",
    "100790.KQ": "미래에셋벤처투자",
    "036540.KQ": "SFA반도체",
    "115180.KQ": "큐리언트",
    "127120.KQ": "제이에스링크",
    "161580.KQ": "필옵틱스",
    "032190.KQ": "다우데이타",
    "006730.KQ": "서부T&D",
    "124500.KQ": "아이티센글로벌",
    "417200.KQ": "LS머트리얼즈",
    "241710.KQ": "코스메카코리아",
    "174900.KQ": "앱클론",
    "014620.KQ": "성광벤드",
    "131290.KQ": "티에스이",
    "376300.KQ": "디어유",
    "295310.KQ": "에이치브이엠",
    "490470.KQ": "세미파이브",
    "086900.KQ": "메디톡스",
    "348340.KQ": "뉴로메카",
    "036810.KQ": "에프에스티",
    "082920.KQ": "비츠로셀",
    "112040.KQ": "위메이드",
    "052400.KQ": "코나아이",
    "358570.KQ": "지아이이노베이션",
    "389470.KQ": "인벤티지랩",
    "060250.KQ": "NHN KCP",
    "033500.KQ": "동성화인텍",
    "033100.KQ": "제룡전기",
    "214430.KQ": "아이쓰리시스템",
    "121600.KQ": "나노신소재",
    "376900.KQ": "로킷헬스케어",
    "032500.KQ": "케이엠더블유",
    "089970.KQ": "브이엠",
    # ADDITIONAL_KR_50
    "247540.KQ": "에코프로비엠",
    "086520.KQ": "에코프로",
    "196170.KQ": "알테오젠",
    "058470.KQ": "리노공업",
    "141080.KQ": "리가켐바이오",
    "240810.KQ": "원익IPS",
    "145020.KQ": "휴젤",
    "214450.KQ": "파마리서치",
    "079980.KS": "휴비스",
    "005300.KS": "롯데칠성",
    "035760.KS": "CJ ENM",
    "091990.KQ": "셀트리온헬스케어",
    "383310.KQ": "에코프로HN",
    "041510.KS": "에스엠",
    "035900.KS": "JYP엔터테인먼트",
    "214150.KQ": "클래시스",
    "357780.KQ": "솔브레인",
    "006140.KS": "펄어비스",
    "225220.KQ": "에임드바이오",
    "237690.KQ": "에스티팜",
    "140860.KQ": "파크시스템스",
    "036930.KQ": "주성엔지니어링",
    "064760.KQ": "티씨케이",
    "222080.KQ": "심텍",
    "403870.KQ": "HPSP",
    "424460.KQ": "이오테크닉스",
    "095340.KQ": "ISC",
    "006120.KS": "SK디스커버리",
    "108320.KS": "LX세미콘",
    "000040.KS": "KR모터스",
    "265520.KQ": "에이프로시스템",
    "293490.KQ": "카카오게임즈",
    "095700.KQ": "제넥신",
    "268600.KQ": "셀리버리",
    "046430.KQ": "에스코어",
    "304840.KQ": "피플바이오",
    "246720.KQ": "아스타",
    "261840.KQ": "엔젤로보틱스",
    "376290.KQ": "셀렉트아이",
    "054540.KQ": "키넥스",
    "017810.KS": "풀무원",
    "004540.KS": "깨끗한나라",
    "192400.KS": "쿠쿠홀딩스",
    # ADDITIONAL_KR_50_2
    "001230.KS": "동국제강",
    "004720.KS": "한솔홀딩스",
    "009240.KS": "한샘",
    "011000.KS": "한독",
    "001740.KS": "SK네트웍스",
    "003000.KS": "부광약품",
    "005250.KS": "청담러닝",
    "005610.KS": "SPC삼립",
    "007160.KS": "쌍용양회",
    "009260.KS": "로웰",
    "017390.KS": "서울도시가스",
    "018250.KS": "애경산업",
    "020000.KS": "한섬",
    "024070.KS": "WISCOM",
    "026940.KS": "부국철강",
    "029460.KS": "케이씨텍",
    "030350.KS": "크레인플러스",
    "036530.KS": "SNT홀딩스",
    "037560.KS": "CJ헬로",
    "039020.KS": "이베스트투자증권",
    "051380.KS": "피씨디",
    "053690.KS": "한미글로벌",
    "058430.KS": "에스폴리텍",
    "065770.KS": "CS홀딩스",
    "071840.KS": "롯데하이마트",
    "072710.KS": "농심홀딩스",
    "079160.KS": "CJ CGV",
    "084690.KS": "대동공업",
    "085310.KS": "이엔코퍼레이션",
    "033290.KQ": "유티아이",
    "043150.KQ": "바텍",
    "052460.KQ": "코스맥스코리아",
    "054630.KQ": "에이디엔에스",
    "057540.KQ": "옴니시스템",
    "073010.KQ": "케에스피",
    "078340.KQ": "컴뱃",
    "099220.KQ": "SD바이오센서",
    "099410.KQ": "동방생명",
    "101670.KQ": "하이드로리튬",
    "109610.KQ": "에스와이",
    "131970.KQ": "두산테스나",
    "136480.KQ": "하림",
    "137400.KQ": "피엔티",
    "143160.KQ": "비와이엔터프라이즈",
    "149980.KQ": "하이로닉스",
    "153460.KQ": "네이블",
    "170920.KQ": "엘티씨",
    "214390.KQ": "경보제약",
    "227610.KQ": "아우딘퓨쳐스",
    "033180.KS": "KH필룩스",
}

NAME_TO_TICKER = {v: k for k, v in TICKER_TO_NAME.items()}

# 티커 → 섹터 (meta_cache_kr 기반, 없으면 Industrials)
TICKER_TO_SECTOR = {
    "005930.KS": "Technology",
    "000660.KS": "Technology",
    "005380.KS": "Consumer Cyclical",
    "373220.KS": "Industrials",
    "207940.KS": "Healthcare",
    "402340.KS": "Technology",
    "000270.KS": "Consumer Cyclical",
    "034020.KS": "Industrials",
    "012450.KS": "Industrials",
    "329180.KS": "Industrials",
    "105560.KS": "Financial Services",
    "028260.KS": "Industrials",
    "068270.KS": "Healthcare",
    "055550.KS": "Financial Services",
    "042660.KS": "Industrials",
    "032830.KS": "Financial Services",
    "015760.KS": "Utilities",
    "006800.KS": "Financial Services",
    "012330.KS": "Consumer Cyclical",
    "035420.KS": "Communication Services",
    "086790.KS": "Financial Services",
    "267260.KS": "Industrials",
    "010130.KS": "Basic Materials",
    "006400.KS": "Industrials",
    "009540.KS": "Industrials",
    "005490.KS": "Basic Materials",
    "316140.KS": "Financial Services",
    "000810.KS": "Financial Services",
    "009150.KS": "Technology",
    "034730.KS": "Industrials",
    "010140.KS": "Industrials",
    "035720.KS": "Communication Services",
    "138040.KS": "Financial Services",
    "298040.KS": "Industrials",
    "064350.KS": "Industrials",
    "051910.KS": "Basic Materials",
    "267250.KS": "Energy",
    "024110.KS": "Financial Services",
    "272210.KS": "Industrials",
    "011200.KS": "Industrials",
    "096770.KS": "Energy",
    "033780.KS": "Consumer Defensive",
    "010120.KS": "Industrials",
    "003670.KS": "Industrials",
    "086280.KS": "Industrials",
    "066570.KS": "Technology",
    "042700.KS": "Technology",
    "030200.KS": "Communication Services",
    "017670.KS": "Communication Services",
    "047810.KS": "Industrials",
    "352820.KS": "Communication Services",
    "000150.KS": "Industrials",
    "071050.KS": "Financial Services",
    "003550.KS": "Technology",
    "000720.KS": "Industrials",
    "005940.KS": "Financial Services",
    "323410.KS": "Financial Services",
    "010950.KS": "Energy",
    "039490.KS": "Financial Services",
    "005830.KS": "Financial Services",
    "018260.KS": "Technology",
    "047050.KS": "Industrials",
    "259960.KS": "Communication Services",
    "307950.KS": "Technology",
    "278470.KS": "Consumer Defensive",
    "079550.KS": "Industrials",
    "016360.KS": "Financial Services",
    "180640.KS": "Consumer Cyclical",
    "000880.KS": "Industrials",
    "161390.KS": "Consumer Cyclical",
    "003490.KS": "Industrials",
    "090430.KS": "Consumer Defensive",
    "009830.KS": "Technology",
    "377300.KS": "Technology",
    "000100.KS": "Healthcare",
    "003230.KS": "Consumer Defensive",
    "326030.KS": "Healthcare",
    "006260.KS": "Industrials",
    "443060.KS": "Industrials",
    "128940.KS": "Healthcare",
    "029780.KS": "Financial Services",
    "032640.KS": "Communication Services",
    "007660.KS": "Technology",
    "175330.KS": "Financial Services",
    "078930.KS": "Industrials",
    "138930.KS": "Financial Services",
    "028050.KS": "Industrials",
    "267270.KS": "Industrials",
    "064400.KS": "Industrials",
    "034220.KS": "Technology",
    "001040.KS": "Industrials",
    "454910.KS": "Industrials",
    "241560.KS": "Industrials",
    "021240.KS": "Consumer Cyclical",
    "052690.KS": "Industrials",
    "001440.KS": "Industrials",
    "011070.KS": "Technology",
    "022100.KS": "Technology",
    "088350.KS": "Financial Services",
    "088980.KS": "Unknown",
    "271560.KS": "Consumer Defensive",
    "004020.KS": "Basic Materials",
    "002380.KS": "Basic Materials",
    "018880.KS": "Consumer Cyclical",
    "036570.KS": "Communication Services",
    "251270.KS": "Communication Services",
    "082740.KS": "Industrials",
    "450080.KS": "Industrials",
    "066970.KS": "Industrials",
    "062040.KS": "Technology",
    "031210.KS": "Industrials",
    "017800.KS": "Industrials",
    "036460.KS": "Utilities",
    "011790.KS": "Basic Materials",
    "051900.KS": "Consumer Defensive",
    "035250.KS": "Consumer Cyclical",
    "000990.KS": "Technology",
    "001720.KS": "Financial Services",
    "302440.KS": "Healthcare",
    "111770.KS": "Consumer Cyclical",
    "004990.KS": "Consumer Defensive",
    "011780.KS": "Basic Materials",
    "011170.KS": "Basic Materials",
    "014680.KS": "Basic Materials",
    "012750.KS": "Industrials",
    "139130.KS": "Financial Services",
    "001450.KS": "Financial Services",
    "103590.KS": "Industrials",
    "004170.KS": "Consumer Cyclical",
    "097950.KS": "Consumer Defensive",
    "000240.KS": "Industrials",
    "047040.KS": "Industrials",
    "103140.KS": "Industrials",
    "000120.KS": "Industrials",
    "439260.KS": "Industrials",
    "023530.KS": "Consumer Cyclical",
    "489790.KS": "Industrials",
    "071970.KS": "Industrials",
    "139480.KS": "Consumer Defensive",
    "009970.KS": "Industrials",
    "457190.KS": "Unknown",
    "012510.KS": "Technology",
    "026960.KS": "Industrials",
    "008930.KS": "Healthcare",
    "353200.KS": "Technology",
    "009420.KS": "Healthcare",
    "028670.KS": "Industrials",
    "010060.KS": "Financial Services",
    "005850.KS": "Consumer Cyclical",
    "051600.KS": "Industrials",
    "204320.KS": "Consumer Cyclical",
    "004800.KS": "Industrials",
    "081660.KS": "Consumer Cyclical",
    "003690.KS": "Financial Services",
    "023590.KS": "Technology",
    "004370.KS": "Consumer Defensive",
    "383220.KS": "Consumer Cyclical",
    "002790.KS": "Consumer Defensive",
    "001430.KS": "Basic Materials",
    "030000.KS": "Communication Services",
    "003540.KS": "Financial Services",
    "097230.KS": "Industrials",
    "069960.KS": "Consumer Cyclical",
    "336260.KS": "Industrials",
    "282330.KS": "Consumer Defensive",
    "011210.KS": "Consumer Cyclical",
    "020150.KS": "Industrials",
    "018670.KS": "Industrials",
    "005440.KS": "Consumer Defensive",
    "192820.KS": "Consumer Defensive",
    "085620.KS": "Financial Services",
    "361610.KS": "Technology",
    "483650.KS": "Industrials",
    "073240.KS": "Consumer Cyclical",
    "006280.KS": "Healthcare",
    "112610.KS": "Industrials",
    "069620.KS": "Healthcare",
    "003530.KS": "Financial Services",
    "017960.KS": "Basic Materials",
    "462870.KS": "Industrials",
    "006040.KS": "Industrials",
    "375500.KS": "Industrials",
    "006360.KS": "Industrials",
    "032350.KS": "Consumer Cyclical",
    "003570.KS": "Industrials",
    "030610.KS": "Industrials",
    "008770.KS": "Consumer Cyclical",
    "034230.KS": "Consumer Cyclical",
    "007070.KS": "Consumer Cyclical",
    "001120.KS": "Industrials",
    "007340.KS": "Consumer Cyclical",
    "005070.KS": "Basic Materials",
    "161890.KS": "Consumer Defensive",
    "298020.KS": "Consumer Cyclical",
    "120110.KS": "Basic Materials",
    "395400.KS": "Industrials",
    "003090.KS": "Industrials",
    "007310.KS": "Industrials",
    "020560.KS": "Industrials",
    "294870.KS": "Industrials",
    "000250.KQ": "Unknown",
    "277810.KQ": "Industrials",
    "298380.KQ": "Healthcare",
    "214370.KQ": "Unknown",
    "950160.KQ": "Unknown",
    "028300.KQ": "Healthcare",
    "087010.KQ": "Unknown",
    "310210.KQ": "Healthcare",
    "140410.KQ": "Unknown",
    "108490.KQ": "Technology",
    "347850.KQ": "Healthcare",
    "068760.KQ": "Healthcare",
    "084370.KQ": "Unknown",
    "319400.KQ": "Financial Services",
    "058610.KQ": "Unknown",
    "290650.KQ": "Healthcare",
    "005290.KQ": "Basic Materials",
    "083650.KQ": "Unknown",
    "030530.KQ": "Industrials",
    "257720.KQ": "Consumer Defensive",
    "226950.KQ": "Healthcare",
    "440110.KQ": "Industrials",
    "032820.KQ": "Unknown",
    "475830.KQ": "Industrials",
    "067310.KQ": "Unknown",
    "323280.KQ": "Industrials",
    "098460.KQ": "Technology",
    "178320.KQ": "Technology",
    "347700.KQ": "Healthcare",
    "065350.KQ": "Industrials",
    "160190.KQ": "Consumer Cyclical",
    "039200.KQ": "Unknown",
    "491000.KQ": "Industrials",
    "101490.KQ": "Unknown",
    "082270.KQ": "Unknown",
    "085660.KQ": "Healthcare",
    "099320.KQ": "Unknown",
    "031980.KQ": "Unknown",
    "458870.KQ": "Healthcare",
    "476830.KQ": "Industrials",
    "445680.KQ": "Unknown",
    "348370.KQ": "Industrials",
    "232140.KQ": "Technology",
    "090710.KQ": "Unknown",
    "089030.KQ": "Technology",
    "466100.KQ": "Industrials",
    "218410.KQ": "Unknown",
    "043260.KQ": "Unknown",
    "060370.KQ": "Unknown",
    "080220.KQ": "Unknown",
    "038500.KQ": "Basic Materials",
    "437730.KQ": "Industrials",
    "397030.KQ": "Healthcare",
    "007390.KQ": "Unknown",
    "281740.KQ": "Basic Materials",
    "456160.KQ": "Industrials",
    "388210.KQ": "Industrials",
    "096530.KQ": "Healthcare",
    "078600.KQ": "Unknown",
    "095610.KQ": "Unknown",
    "388720.KQ": "Unknown",
    "056080.KQ": "Unknown",
    "122870.KQ": "Communication Services",
    "048410.KQ": "Healthcare",
    "189300.KQ": "Unknown",
    "328130.KQ": "Healthcare",
    "171090.KQ": "Technology",
    "204270.KQ": "Technology",
    "100790.KQ": "Unknown",
    "036540.KQ": "Technology",
    "115180.KQ": "Healthcare",
    "127120.KQ": "Healthcare",
    "161580.KQ": "Industrials",
    "032190.KQ": "Technology",
    "006730.KQ": "Consumer Cyclical",
    "124500.KQ": "Technology",
    "417200.KQ": "Industrials",
    "241710.KQ": "Consumer Defensive",
    "174900.KQ": "Healthcare",
    "014620.KQ": "Industrials",
    "131290.KQ": "Unknown",
    "376300.KQ": "Technology",
    "295310.KQ": "Basic Materials",
    "490470.KQ": "Industrials",
    "086900.KQ": "Healthcare",
    "348340.KQ": "Industrials",
    "036810.KQ": "Technology",
    "082920.KQ": "Unknown",
    "112040.KQ": "Unknown",
    "052400.KQ": "Technology",
    "358570.KQ": "Unknown",
    "389470.KQ": "Healthcare",
    "060250.KQ": "Technology",
    "033500.KQ": "Unknown",
    "033100.KQ": "Industrials",
    "214430.KQ": "Technology",
    "121600.KQ": "Basic Materials",
    "376900.KQ": "Industrials",
    "032500.KQ": "Technology",
    "089970.KQ": "Technology",
    # ADDITIONAL_KR_50
    "247540.KQ": "Industrials",
    "086520.KQ": "Industrials",
    "196170.KQ": "Healthcare",
    "058470.KQ": "Technology",
    "141080.KQ": "Healthcare",
    "240810.KQ": "Technology",
    "145020.KQ": "Healthcare",
    "214450.KQ": "Healthcare",
    "079980.KS": "Basic Materials",
    "005300.KS": "Consumer Defensive",
    "035760.KS": "Communication Services",
    "091990.KQ": "Healthcare",
    "383310.KQ": "Industrials",
    "041510.KS": "Communication Services",
    "035900.KS": "Communication Services",
    "214150.KQ": "Technology",
    "357780.KQ": "Basic Materials",
    "006140.KS": "Industrials",
    "225220.KQ": "Healthcare",
    "237690.KQ": "Healthcare",
    "140860.KQ": "Technology",
    "036930.KQ": "Technology",
    "064760.KQ": "Technology",
    "222080.KQ": "Technology",
    "403870.KQ": "Healthcare",
    "424460.KQ": "Technology",
    "095340.KQ": "Technology",
    "006120.KS": "Industrials",
    "108320.KS": "Technology",
    "000040.KS": "Consumer Cyclical",
    "265520.KQ": "Technology",
    "293490.KQ": "Communication Services",
    "095700.KQ": "Healthcare",
    "268600.KQ": "Healthcare",
    "046430.KQ": "Technology",
    "304840.KQ": "Healthcare",
    "246720.KQ": "Healthcare",
    "261840.KQ": "Industrials",
    "376290.KQ": "Technology",
    "054540.KQ": "Technology",
    "017810.KS": "Consumer Defensive",
    "004540.KS": "Consumer Defensive",
    "192400.KS": "Consumer Cyclical",
    # ADDITIONAL_KR_50_2
    "001230.KS": "Basic Materials",
    "004720.KS": "Basic Materials",
    "009240.KS": "Consumer Cyclical",
    "011000.KS": "Healthcare",
    "001740.KS": "Industrials",
    "003000.KS": "Healthcare",
    "005250.KS": "Consumer Cyclical",
    "005610.KS": "Consumer Defensive",
    "007160.KS": "Basic Materials",
    "009260.KS": "Industrials",
    "017390.KS": "Utilities",
    "018250.KS": "Consumer Defensive",
    "020000.KS": "Consumer Cyclical",
    "024070.KS": "Technology",
    "026940.KS": "Basic Materials",
    "029460.KS": "Technology",
    "030350.KS": "Industrials",
    "036530.KS": "Industrials",
    "037560.KS": "Communication Services",
    "039020.KS": "Financial Services",
    "051380.KS": "Technology",
    "053690.KS": "Industrials",
    "058430.KS": "Technology",
    "065770.KS": "Financial Services",
    "071840.KS": "Consumer Cyclical",
    "072710.KS": "Consumer Defensive",
    "079160.KS": "Communication Services",
    "084690.KS": "Industrials",
    "085310.KS": "Industrials",
    "033290.KQ": "Technology",
    "043150.KQ": "Technology",
    "052460.KQ": "Consumer Defensive",
    "054630.KQ": "Technology",
    "057540.KQ": "Technology",
    "073010.KQ": "Technology",
    "078340.KQ": "Industrials",
    "099220.KQ": "Healthcare",
    "099410.KQ": "Healthcare",
    "101670.KQ": "Industrials",
    "109610.KQ": "Technology",
    "131970.KQ": "Technology",
    "136480.KQ": "Consumer Defensive",
    "137400.KQ": "Technology",
    "143160.KQ": "Technology",
    "149980.KQ": "Technology",
    "153460.KQ": "Technology",
    "170920.KQ": "Technology",
    "214390.KQ": "Healthcare",
    "227610.KQ": "Technology",
    "033180.KS": "Technology",
}