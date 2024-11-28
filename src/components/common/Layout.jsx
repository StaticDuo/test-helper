import { Outlet } from "react-router-dom";
import Nav from "./Nav";

const Layout = () => {
  return (
    <div>
      <Outlet />
      <Nav />
    </div>
  );
};

export default Layout;
