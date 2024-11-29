import styled from "styled-components";
import { Link } from "react-router-dom";

const Nav = () => {
  return (
    <NavContainer>
      <NavWrapper>
        {/* <NavItem to="/upload">
          <IconPlaceholder>↑</IconPlaceholder>
          <NavText>시험 업로드</NavText>
        </NavItem> */}
        <NavItem to="/subjects">
          <IconPlaceholder>✎</IconPlaceholder>
          <NavText>시험보기</NavText>
        </NavItem>
        {/* <NavItem to="statistics">
          <IconPlaceholder>📊</IconPlaceholder>
          <NavText>통계</NavText>
        </NavItem> */}
        <NavItem>
          <IconPlaceholder>≡</IconPlaceholder>
          <NavText>전체 메뉴</NavText>
        </NavItem>
      </NavWrapper>
    </NavContainer>
  );
};

const NavContainer = styled.nav`
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #ffffff;
  border-top: 1px solid #f2f3f4;
  padding: 8px 0 calc(8px + env(safe-area-inset-bottom));
  z-index: 100;
`;

const NavWrapper = styled.div`
  display: flex;
  justify-content: space-around;
  align-items: center;
  max-width: 480px;
  margin: 0 auto;
`;

const NavItem = styled(Link)`
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  padding: 4px 0;
  text-decoration: none;

  &:active {
    opacity: 0.7;
  }
`;

const IconPlaceholder = styled.div`
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 4px;
  font-size: 20px;
  color: #333333;
`;

const NavText = styled.span`
  font-size: 11px;
  color: #333333;
  letter-spacing: -0.3px;
`;

export default Nav;
