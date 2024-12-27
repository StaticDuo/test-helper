import styled from "styled-components";

const AllQuestionModal = () => {
  return (
    <>
      <ModalOverlay />
      <ModalContainer>
        <ModalHeader>
          <ModalTitle>전체 문제</ModalTitle>
          <CloseButton>×</CloseButton>
        </ModalHeader>

        <ModalContent>
          <Legend>
            <LegendItem>
              <LegendColor $solved />
              <span>푼 문제</span>
            </LegendItem>
            <LegendItem>
              <LegendColor />
              <span>안 푼 문제</span>
            </LegendItem>
          </Legend>

          <QuestionGrid>
            {[...Array(20)].map((_, index) => (
              <QuestionItem key={index} $solved={index % 3 === 0}>
                {index + 1}
              </QuestionItem>
            ))}
          </QuestionGrid>
        </ModalContent>
      </ModalContainer>
    </>
  );
};

const ModalOverlay = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(2px);
`;

const ModalContainer = styled.div`
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 90%;
  max-width: 500px;
  z-index: 1000;
`;

const ModalHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
`;

const ModalTitle = styled.h1`
  font-size: 20px;
  font-weight: 600;
  color: #1f2937;
`;

const CloseButton = styled.button`
  background: none;
  border: none;
  font-size: 24px;
  color: #6b7280;
  cursor: pointer;
  padding: 4px 8px;

  &:hover {
    color: #374151;
  }
`;

const ModalContent = styled.div`
  padding: 16px 0;
`;

const Legend = styled.div`
  display: flex;
  gap: 16px;
  margin-bottom: 20px;
`;

const LegendItem = styled.div`
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  color: #4b5563;
`;

const LegendColor = styled.div`
  width: 16px;
  height: 16px;
  border-radius: 4px;
  background-color: ${(props) => (props.$solved ? "#3b82f6" : "#e5e7eb")};
  border: 1px solid ${(props) => (props.$solved ? "#2563eb" : "#d1d5db")};
`;

const QuestionGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
`;

const QuestionItem = styled.button`
  display: flex;
  align-items: center;
  justify-content: center;
  height: 48px;
  background-color: ${(props) => (props.$solved ? "#3b82f6" : "white")};
  color: ${(props) => (props.$solved ? "white" : "#374151")};
  border: 1px solid ${(props) => (props.$solved ? "#2563eb" : "#e5e7eb")};
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background-color: ${(props) => (props.$solved ? "#2563eb" : "#f3f4f6")};
    border-color: ${(props) => (props.$solved ? "#1d4ed8" : "#d1d5db")};
  }
`;

export default AllQuestionModal;
