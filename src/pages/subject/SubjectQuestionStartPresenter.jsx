import styled from "styled-components";

const SubjectQuestionStartPresenter = ({
  handleRandomOrderClick,
  handleQuestionStartClick,
  handleLimitChange,
  error,
  questionCount,
  isRandomOrder,
  subjectName = "과목 이름",
}) => {
  return (
    <Container>
      <SubjectTitle>{subjectName}</SubjectTitle>
      <Title> 문제 고르기</Title>

      <InputWrapper>
        <Label>문제 개수</Label>
        <Input
          type="number"
          min="1"
          max="100"
          value={questionCount}
          onChange={handleLimitChange}
          placeholder="풀고 싶은 문제 개수를 입력하세요"
          $hasError={!!error}
        />
        <ErrorMessage $visible={!!error}>{error}</ErrorMessage>
      </InputWrapper>

      <ButtonGroup>
        <SecondaryButton
          $isRandom={isRandomOrder}
          onClick={handleRandomOrderClick}
        >
          {isRandomOrder ? "번호순으로 나옵니다." : "무작위로 나옵니다."}
        </SecondaryButton>
        <PrimaryButton onClick={handleQuestionStartClick}>
          문제 풀러 가기
        </PrimaryButton>
      </ButtonGroup>
    </Container>
  );
};

export default SubjectQuestionStartPresenter;

const Container = styled.div`
  display: flex;
  flex-direction: column;
  max-width: 480px;
  margin: 0 auto;
  padding: 24px;
  background-color: white;
`;

const SubjectTitle = styled.h3`
  font-size: 18px;
  font-weight: 700;
  color: #555555;
  margin-bottom: 12px;
`;

const Title = styled.h1`
  font-size: 24px;
  font-weight: 700;
  color: #191f28;
  margin-bottom: 24px;
`;

const InputWrapper = styled.div`
  margin-bottom: 24px;
`;

const Label = styled.label`
  display: block;
  font-size: 14px;
  font-weight: 500;
  color: #4e5968;
  margin-bottom: 8px;
`;

const Input = styled.input`
  width: 100%;
  padding: 12px 16px;
  border: 1px solid ${(props) => (props.$hasError ? "#FF4545" : "#E5E7EC")};
  border-radius: 8px;
  font-size: 16px;
  outline: none;
  transition: all 0.2s ease;

  &:focus {
    border-color: ${(props) => (props.$hasError ? "#FF4545" : "#3182F6")};
    box-shadow: 0 0 0 2px
      ${(props) =>
        props.$hasError ? "rgba(255, 69, 69, 0.1)" : "rgba(49, 130, 246, 0.1)"};
  }

  &::-webkit-inner-spin-button,
  &::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
`;

const ErrorMessage = styled.p`
  color: #ff4545;
  font-size: 14px;
  margin-top: 8px;
  display: ${(props) => (props.$visible ? "block" : "none")};
`;

const ButtonGroup = styled.div`
  display: grid;
  grid-template-rows: 1fr 1fr 1fr;
  gap: 12px;
`;

const Button = styled.button`
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  transition: all 0.2s ease;
  cursor: pointer;
  outline: none;
  border: none;

  &:focus {
    box-shadow: 0 0 0 2px rgba(49, 130, 246, 0.2);
  }
`;

const SecondaryButton = styled(Button)`
  background-color: ${(props) => (props.$isRandom ? "#E5E7EC" : "#F3F4F6")};
  color: ${(props) => (props.$isRandom ? "#191F28" : "#4E5968")};

  &:hover {
    background-color: ${(props) => (props.$isRandom ? "#D1D5DB" : "#E5E7EC")};
  }
`;

const PrimaryButton = styled(Button)`
  background-color: #3182f6;
  color: white;

  &:hover {
    background-color: #1b64da;
  }
`;
