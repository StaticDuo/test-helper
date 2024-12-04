import styled from "styled-components";

const SubjectExamPresenter = ({ exams, subject, handleClickExam }) => {
  return (
    <Container>
      <Title>{subject.name} 시험 목록</Title>
      <ExamList>
        {exams.map((exam) => (
          <ExamItem
            key={exam.exam_id}
            onClick={() => {
              handleClickExam(exam.exam_id);
            }}
          >
            <ExamTitle>{exam.name}</ExamTitle>
          </ExamItem>
        ))}
      </ExamList>
    </Container>
  );
};

export default SubjectExamPresenter;

const Container = styled.div`
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
`;

const Title = styled.h1`
  font-size: 24px;
  margin-bottom: 20px;
`;

const ExamList = styled.ul`
  list-style: none;
  padding: 0;
`;

const ExamItem = styled.li`
  background: white;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
`;

const ExamTitle = styled.h2`
  font-size: 18px;
  margin: 0 0 12px 0;
`;
