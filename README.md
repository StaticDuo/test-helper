## 파일 구조

```
src/
├── assets/ # 이미지, 아이콘 등 정적 리소스
├── components/ # 재사용 가능한 컴포넌트
│ ├── common/ # 공통 컴포넌트
│ │ ├── Button/
│ │ ├── Input/
│ │ ├── Modal/
│ │ └── Navigation/ # 하단 네비게이션 바
│ ├── auth/ # 인증 관련 컴포넌트
│ ├── subject/ # Subject 관련 컴포넌트
│ ├── exam/ # Exam 관련 컴포넌트
│ └── statistics/ # 통계 관련 컴포넌트
├── pages/ # 페이지 컴포넌트
│ ├── auth/
│ │ ├── LoginPage.jsx
│ │ └── SignupPage.jsx
│ ├── subject/
│ │ ├── SubjectListPage.jsx # 메인 화면 (과목 목록)
│ │ └── SubjectDetailPage.jsx # 특정 과목의 시험 목록
│ ├── exam/
│ │ ├── ExamListPage.jsx # 시험 목록
│ │ ├── ExamUploadPage.jsx # 시험 업로드
│ │ ├── ExamTakingPage.jsx # 시험 보기
│ │ └── ExamDetailPage.jsx # 시험 상세
│ └── statistics/
│ │ ├── StatisticsPage.jsx # 통계 메인
│ │ └── DetailedStatsPage.jsx # 상세 통계
├── hooks/ # 커스텀 훅
├── services/ # API 통신 로직
│ ├── authService.js
│ ├── subjectService.js
│ ├── examService.js
│ └── statisticsService.js
├── store/ # 상태 관리
├── utils/ # 유틸리티 함수
│ ├── api.js # API 요청 공통 로직
│ ├── excel.js # 엑셀 처리 관련 유틸
│ └── validators.js # 데이터 유효성 검사를 위한 함수들
└── styles/ # 글로벌 스타일, 테마 등
```
