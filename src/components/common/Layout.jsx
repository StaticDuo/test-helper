import { Outlet } from "react-router-dom";
import Nav from "./Nav";
import Header from "./Header";
import { NavProvider } from "../../context/NavContext";

import styled from "styled-components";

const Layout = () => {
  return (
    <NavProvider>
      <LayoutContainer>
        <Header />
        <MainContent>
          <Outlet />
        </MainContent>
        <Nav />
      </LayoutContainer>
    </NavProvider>
  );
};

export default Layout;

const LayoutContainer = styled.div`
  height: 100vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
`;

const MainContent = styled.main`
  flex: 1;
  padding-bottom: 70px;
  overflow: hidden;
`;
