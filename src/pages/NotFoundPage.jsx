import styled from "styled-components";

import { Link } from "react-router-dom";

const NotFoundPage = () => {
  return (
    <Container>
      <Title>404 - Not Found</Title>
      <HomeLink to="/">홈으로</HomeLink>
    </Container>
  );
};

export default NotFoundPage;

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: #f5f5f5;
`;

const Title = styled.h1`
  font-size: 48px;
  margin-bottom: 24px;
  color: #333;
`;

const HomeLink = styled(Link)`
  padding: 12px 24px;
  background: #4caf50;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: bold;
  transition: transform 0.2s;

  &:hover {
    transform: translateY(-2px);
  }
`;
