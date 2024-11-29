import styled from "styled-components";

const subjects = [
  {
    id: 1,
    name: "기사",
    icon: "📐",
    bgColor: "#dbeafe",
    description: "실기 및 이론 시험 대비",
  },
  {
    id: 2,
    name: "기능사",
    icon: "🔬",
    bgColor: "#dcfce7",
    description: "실기 및 이론 시험 대비",
  },
  {
    id: 3,
    name: "코딩",
    icon: "💻",
    bgColor: "#f3e8ff",
    description: "프로그래밍 기초와 알고리즘",
  },
  {
    id: 4,
    name: "영어",
    icon: "🌎",
    bgColor: "#fef9c3",
    description: "회화부터 시험 대비까지",
  },
  {
    id: 5,
    name: "회계",
    icon: "📚",
    bgColor: "#fee2e2",
    description: "회계원리와 실무",
  },
  {
    id: 6,
    name: "재무",
    icon: "🎵",
    bgColor: "#fce7f3",
    description: "재무제표와 재무분석",
  },
];

const SubjectListPresenter = ({
  handleSearchInputChange,
  handleClickTitle,
  handleClickSubject,
}) => {
  return (
    <Container>
      <Header>
        <Title onClick={handleClickTitle}>Test Helper</Title>
        <Subtitle>나만의 학습 도우미</Subtitle>
      </Header>

      <SearchWrapper>
        <SearchIconWrapper>🔍</SearchIconWrapper>
        <SearchInput
          onChange={handleSearchInputChange}
          placeholder="학습하고 싶은 과목을 검색하세요"
        />
      </SearchWrapper>

      <SectionTitle>전체 과목</SectionTitle>
      <SubjectGrid>
        {subjects.map((subject) => (
          <SubjectCard
            onClick={() => handleClickSubject(subject.id)}
            key={subject.id}
            bgColor={subject.bgColor}
          >
            <IconWrapper>{subject.icon}</IconWrapper>
            <SubjectName>{subject.name}</SubjectName>
            <SubjectDescription>{subject.description}</SubjectDescription>
          </SubjectCard>
        ))}
      </SubjectGrid>
    </Container>
  );
};

export default SubjectListPresenter;

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

const SubjectGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 16px;
  margin-bottom: 32px;
`;

const SubjectCard = styled.div`
  background-color: ${(props) => props.bgColor || "#fff"};
  padding: 20px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transition: transform 0.2s;
  cursor: pointer;

  &:hover {
    transform: translateY(-2px);
  }
`;

const IconWrapper = styled.div`
  width: 48px;
  height: 48px;
  background-color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const SubjectName = styled.h2`
  font-size: 16px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 4px;
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
