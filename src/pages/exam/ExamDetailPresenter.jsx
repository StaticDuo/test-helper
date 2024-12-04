import styled from "styled-components";

const ExamDetailPresenter = ({ exam, handleClickStartExam }) => {
  return (
    <Container>
      <Title>{exam.name}</Title>
      <Description>
        이 시험은 몇 문제이고, 난이도는 어느정도이고, 몇 문제이고, 몇 분 동안
        풀겠습니다
      </Description>
      <StartButton onClick={handleClickStartExam}>시험 시작</StartButton>
    </Container>
  );
};

export default ExamDetailPresenter;

const Container = styled.div`
  max-width: 800px;
  padding: 30px;
`;

const Title = styled.h1`
  font-size: 28px;
  margin-bottom: 24px;
  color: #333;
`;

const Description = styled.p`
  font-size: 16px;
  line-height: 1.6;
  color: #666;
  margin-bottom: 32px;
`;

const StartButton = styled.button`
  background: #4caf50;
  color: white;
  padding: 16px 32px;
  border: none;
  border-radius: 8px;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s;

  &:hover {
    transform: translateY(-2px);
  }
`;
