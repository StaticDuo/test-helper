import styled from "styled-components";
import AllQuestionModal from "../../components/question/AllQuestionModal";

const SubjectQuestionPresenter = ({
  currentQuestion,
  currentIndex,
  questions,
  setCurrentIndex,
  subjectName = "과목 이름",
  isModalOpen,
  handleSubmit,
}) => {
  return (
    <Container>
      <SubjectTitle>{subjectName}</SubjectTitle>

      <ProgressBar>
        <ProgressText>
          문제 {currentIndex + 1} / {questions.length}
        </ProgressText>
        <Progress
          value={((currentIndex + 1) / questions.length) * 100}
          max={100}
        />
      </ProgressBar>

      <QuestionCard>
        <QuestionText>{currentQuestion.question_text}</QuestionText>
        <AnswerGrid>
          {currentQuestion.answers.map((answer) => (
            <AnswerButton
              key={answer.answer_id}
              onClick={() => {
                // 답안 선택 처리 로직
              }}
            >
              {answer.answer_text}
            </AnswerButton>
          ))}
        </AnswerGrid>
      </QuestionCard>

      <SubmitButton onClick={handleSubmit}>시험 제출</SubmitButton>
      {
        // 모달 컴포넌트
        isModalOpen && <AllQuestionModal />
      }
    </Container>
  );
};

const Container = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
`;

const SubjectTitle = styled.h1`
  font-size: 24px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 20px;
`;

const ProgressBar = styled.div`
  margin-bottom: 24px;
`;

const ProgressText = styled.div`
  font-size: 14px;
  color: #6b7280;
  margin-bottom: 8px;
`;

const Progress = styled.progress`
  width: 100%;
  height: 8px;
  border-radius: 4px;
  overflow: hidden;

  &::-webkit-progress-bar {
    background-color: #e5e7eb;
    border-radius: 4px;
  }

  &::-webkit-progress-value {
    background-color: #3b82f6;
    border-radius: 4px;
  }
`;

const QuestionCard = styled.div`
  background: white;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
`;

const QuestionText = styled.h2`
  font-size: 18px;
  font-weight: 500;
  color: #1f2937;
  margin-bottom: 20px;
  line-height: 1.5;
`;

const AnswerGrid = styled.div`
  display: grid;
  gap: 12px;
`;

const AnswerButton = styled.button`
  width: 100%;
  padding: 16px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  background: white;
  text-align: left;
  font-size: 16px;
  color: #374151;
  transition: all 0.2s;

  &:hover {
    background: #f3f4f6;
    border-color: #d1d5db;
  }

  &:active {
    background: #e5e7eb;
  }
`;

const SubmitButton = styled.button`
  width: 100px;
  margin: 0 auto;
  margin-top: 24px;
  padding: 12px;
  border-radius: 8px;
  background: #2563eb;
  color: white;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background: #3182f6;
  }

  &:active {
    background: #2563eb;
  }
`;

export default SubjectQuestionPresenter;
