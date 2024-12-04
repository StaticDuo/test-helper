import styled from "styled-components";
import { useNavigate } from "react-router-dom";

const Header = () => {
  const navigate = useNavigate();

  const handleClickTitle = () => {
    navigate("/");
  };

  return (
    <HeaderContainer>
      <Title onClick={handleClickTitle}>Test Helper</Title>
      <Subtitle>나만의 학습 도우미</Subtitle>
    </HeaderContainer>
  );
};

export default Header;

const HeaderContainer = styled.header`
  padding: 20px;
  background-color: #f9fafb;
`;

const Title = styled.h1`
  font-size: 24px;
  font-weight: bold;
  color: #1f2937;
  margin-bottom: 8px;
  cursor: pointer;
`;

const Subtitle = styled.p`
  color: #6b7280;
  font-size: 16px;
`;
