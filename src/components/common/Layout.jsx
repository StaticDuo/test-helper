import { Outlet } from "react-router-dom";
import Nav from "./Nav";
import Header from "./Header";
import { NavProvider } from "../../context/NavContext";

const Layout = () => {
  return (
    <NavProvider>
      <div>
        <Header />
        <Outlet />
        <Nav />
      </div>
    </NavProvider>
  );
};

export default Layout;
