import styled from "styled-components";
import { Link } from "react-router-dom";
import { useNav } from "../../hooks/useNav";

const Nav = () => {
  const { navItems } = useNav();

  const handleClick = (e, item) => {
    if (!item.to) {
      // to prop이 없는 경우
      e.preventDefault();
      if (item.action) {
        item.action();
      }
    }
  };

  return (
    <NavContainer>
      <NavWrapper>
        {navItems.map((item, index) => {
          const BaseComponent = item.to ? Link : "button";
          return (
            <NavItem
              key={index}
              as={BaseComponent}
              to={item.to}
              onClick={(e) => handleClick(e, item)}
              disabled={item.disabled}
            >
              <IconPlaceholder>{item.icon}</IconPlaceholder>
              <NavText>{item.text}</NavText>
            </NavItem>
          );
        })}
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

const NavItem = styled.button`
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  padding: 4px 0;
  text-decoration: none;
  background: none;
  border: none;
  cursor: pointer;

  &:active {
    opacity: 0.7;
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
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
