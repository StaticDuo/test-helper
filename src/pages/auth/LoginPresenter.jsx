import styled from "styled-components";
import { Link } from "react-router-dom";

const LoginPresenter = ({
  values,
  errors,
  isLoading,
  handleChange,
  handleSubmit,
}) => {
  return (
    <Container>
      <LoginContainer>
        <Title>로그인</Title>
        <Form onSubmit={handleSubmit}>
          <InputGroup>
            <Label htmlFor="email">이메일</Label>
            <Input
              id="id"
              name="id"
              type="email"
              placeholder="이메일을 입력하세요"
              value={values.id}
              onChange={handleChange}
              hasError={!!errors.id}
            />
            {errors.email && <ErrorMessage>{errors.email}</ErrorMessage>}
          </InputGroup>
          <InputGroup>
            <Label htmlFor="password">비밀번호</Label>
            <Input
              id="password"
              name="password"
              type="password"
              placeholder="비밀번호를 입력하세요"
              value={values.password}
              onChange={handleChange}
              hasError={!!errors.password}
            />
            {errors.password && <ErrorMessage>{errors.password}</ErrorMessage>}
          </InputGroup>
          {errors.submit && <ErrorMessage>{errors.submit}</ErrorMessage>}
          <LoginButton
            type="submit"
            disabled={isLoading || !values.id || !values.password}
          >
            {isLoading ? "로그인 중..." : "로그인"}
          </LoginButton>
        </Form>
        <LinkContainer>
          <StyledLink to="/password-reset">비밀번호 찾기</StyledLink>
          <LinkDivider>|</LinkDivider>
          <StyledLink to="/signup">회원가입</StyledLink>
        </LinkContainer>
      </LoginContainer>
    </Container>
  );
};

const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f8f9fa;
  padding: 0 16px;
`;

const LoginContainer = styled.div`
  width: 100%;
  max-width: 400px;
  padding: 24px;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
`;

const Title = styled.h1`
  font-size: 24px;
  font-weight: 700;
  color: #191f28;
  margin-bottom: 32px;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 24px;
`;

const InputGroup = styled.div`
  display: flex;
  flex-direction: column;
  gap: 8px;
`;

const Label = styled.label`
  font-size: 14px;
  font-weight: 500;
  color: #4e5968;
`;

const Input = styled.input.withConfig({
  shouldForwardProp: (prop) => prop !== "hasError",
})`
  width: 100%;
  height: 48px;
  padding: 0 16px;
  border: 1px solid ${(props) => (props.hasError ? "#ff6b6b" : "#e5e8eb")};
  border-radius: 8px;
  font-size: 16px;
  outline: none;
  transition: all 0.2s;

  &::placeholder {
    color: #adb5bd;
  }

  &:focus {
    border-color: ${(props) => (props.hasError ? "#ff6b6b" : "#3182f6")};
    box-shadow: 0 0 0 2px
      ${(props) =>
        props.hasError
          ? "rgba(255, 107, 107, 0.1)"
          : "rgba(49, 130, 246, 0.1)"};
  }
`;

const ErrorMessage = styled.span`
  font-size: 12px;
  color: #ff6b6b;
  margin-top: 4px;
`;

const LinkContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 24px;
  gap: 12px;
`;

const StyledLink = styled(Link)`
  font-size: 14px;
  color: #4e5968;
  text-decoration: none;
  transition: color 0.2s;

  &:hover {
    color: #3182f6;
  }
`;

const LinkDivider = styled.span`
  color: #e5e8eb;
`;

const LoginButton = styled.button`
  height: 48px;
  background-color: #3182f6;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  position: relative;

  &:disabled {
    background-color: #e5e8eb;
    cursor: not-allowed;
  }

  &:not(:disabled):hover {
    background-color: #1b64da;
  }

  &:not(:disabled):active {
    background-color: #1957c2;
  }

  ${(props) =>
    props.isLoading &&
    `
   cursor: not-allowed;
   opacity: 0.7;
 `}
`;

export default LoginPresenter;
