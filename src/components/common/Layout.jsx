import { Outlet } from "react-router-dom";
import Nav from "./Nav";
import { NavProvider } from "../../context/NavContext";

const Layout = () => {
  return (
    <NavProvider>
      <div>
        <Outlet />
        <Nav />
      </div>
    </NavProvider>
  );
};

export default Layout;
