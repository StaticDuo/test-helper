import { createContext, useState } from "react";

const NavContext = createContext();

export const NavProvider = ({ children }) => {
  const [navItems, setNavItems] = useState([
    { to: "/subjects", icon: "✎", text: "시험보기" },
    { icon: "≡", text: "전체 메뉴" },
  ]);

  const updateNavItems = (newItems) => {
    setNavItems(newItems);
  };

  return (
    <NavContext.Provider value={{ navItems, updateNavItems }}>
      {children}
    </NavContext.Provider>
  );
};

export default NavContext;
