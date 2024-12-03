import styled from "styled-components";

const HomePage = () => {
  const recentExams = [
    {
      id: 1,
      title: "2024-3회 정보처리기사 실기",
      subject: "기사",
      date: "2024.03.15",
      score: "95",
      duration: "120분",
    },
    {
      id: 2,
      title: "토익 문법 테스트",
      subject: "영어",
      date: "2024.03.14",
      score: "88",
      duration: "60분",
    },
    {
      id: 3,
      title: "2024-1회 정보처리기사 필기",
      subject: "기사",
      date: "2024.03.13",
      score: "92",
      duration: "90분",
    },
  ];

  return (
    <Container>
      <Header>
        <Title>Test Helper</Title>
        <Subtitle>나만의 학습 도우미</Subtitle>
      </Header>

      <SearchWrapper>
        <SearchIconWrapper>🔍</SearchIconWrapper>
        <SearchInput placeholder="학습하고 싶은 과목을 검색하세요" />
      </SearchWrapper>

      <SectionTitle>최근 본 시험</SectionTitle>
      <RecentExamsGrid>
        {!recentExams || recentExams.length === 0 ? (
          <div>최근 본 시험이 없습니다.</div>
        ) : (
          recentExams.map((exam) => (
            <ExamCard key={exam.id}>
              <ExamHeader>
                <ExamTitle>{exam.title}</ExamTitle>
                <ExamDate>{exam.date}</ExamDate>
              </ExamHeader>
              <SubjectDescription>{exam.subject}</SubjectDescription>
              <ExamInfo>
                <ExamInfoItem>
                  <span>⏱️</span>
                  {exam.duration}
                </ExamInfoItem>
                <ExamInfoItem>
                  <span>📊</span>
                  점수: {exam.score}점
                </ExamInfoItem>
              </ExamInfo>
            </ExamCard>
          ))
        )}
        {(recentExams || recentExams.length > 0) && (
          <RecentExamButton>더보기</RecentExamButton>
        )}
      </RecentExamsGrid>
    </Container>
  );
};

export default HomePage;

const Container = styled.div`
  padding: 20px;
  background-color: #f9fafb;
  min-height: 100vh;
  padding-bottom: 80px;
`;

const Header = styled.header`
  margin-bottom: 24px;
`;

const Title = styled.h1`
  font-size: 24px;
  font-weight: bold;
  color: #1f2937;
  margin-bottom: 8px;
`;

const Subtitle = styled.p`
  color: #6b7280;
  font-size: 16px;
`;

const SearchWrapper = styled.div`
  position: relative;
  margin-bottom: 24px;
`;

const SearchInput = styled.input`
  width: 100%;
  padding: 12px 16px 12px 40px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  font-size: 16px;
  outline: none;
  transition: all 0.2s;

  &:focus {
    border-color: #3b82f6;
    box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
  }
`;

const SearchIconWrapper = styled.div`
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #9ca3af;
`;

const SubjectDescription = styled.p`
  font-size: 14px;
  color: #6b7280;
`;

const SectionTitle = styled.h2`
  font-size: 20px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 16px;
`;

const RecentExamButton = styled.button`
  background-color: #f3f4f6;
  border: none;
  border-radius: 8px;
  padding: 12px 16px;
  font-size: 16px;
  color: #6b7280;
  cursor: pointer;
  transition: background-color 0.2s;

  &:hover {
    background-color: #e5e7eb;
  }

  &:active {
    transform: translateY(2px);
  }

  &:focus {
    outline: none;
  }

  &:not(:last-child) {
    margin-right: 16px;
  }

  &:not(:first-child) {
    margin-left: 16px;
  }

  &:disabled {
    background-color: #d1d5db;
    cursor: not-allowed;
  }
`;

const RecentExamsGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
`;

const ExamCard = styled.div`
  background-color: white;
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.2s;

  &:hover {
    transform: translateY(-2px);
  }
`;

const ExamHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
`;

const ExamTitle = styled.h3`
  font-size: 16px;
  font-weight: 600;
  color: #1f2937;
`;

const ExamDate = styled.span`
  font-size: 14px;
  color: #6b7280;
`;

const ExamInfo = styled.div`
  display: flex;
  gap: 16px;
  margin-top: 8px;
`;

const ExamInfoItem = styled.div`
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 14px;
  color: #6b7280;
`;
