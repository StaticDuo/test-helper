import styled from "styled-components";

const SubjectListPresenter = ({
  handleSearchInputChange,
  handleClickSubject,
  subjects,
  isLoading,
  error,
}) => {
  return (
    <Container>
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
            onClick={() => handleClickSubject(subject.subject_id)}
            key={subject.subject_id}
          >
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
  grid-template-columns: repeat(auto-fill); //, minmax(140px, 2fr)
  gap: 8px;
  margin-bottom: 16px;
`;

const SubjectCard = styled.div`
  background-color: ${(props) => props.bgColor || "#fff"};
  padding: 12px;
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
