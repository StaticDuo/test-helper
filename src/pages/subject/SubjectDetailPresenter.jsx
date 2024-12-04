import styled from "styled-components";

const SubjectDetailPresenter = ({
  handleClickExam,
  handleClickQuestion,
  subject,
}) => {
  return (
    <>
      <Title>{subject.name}</Title>
      <ButtonContainer>
        <ExamButton onClick={handleClickExam}>시험 보기</ExamButton>
        <QuestionButton onClick={handleClickQuestion}>문제 보기</QuestionButton>
      </ButtonContainer>
    </>
  );
};

export default SubjectDetailPresenter;

const Title = styled.h1`
  text-align: center;
  font-size: 24px;
  font-weight: bold;
`;

const ButtonContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
  height: 50vh;
  place-content: center;
`;

const Button = styled.button`
  padding: 40px;
  border: none;
  border-radius: 8px;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s;

  &:hover {
    transform: scale(1.05);
  }
`;

const ExamButton = styled(Button)`
  background-color: #4caf50;
  color: white;
`;

const QuestionButton = styled(Button)`
  background-color: #2196f3;
  color: white;
`;
