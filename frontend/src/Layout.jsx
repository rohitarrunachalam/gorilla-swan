import React from "react";
import { Outlet } from "react-router-dom";
import Navbar from "./components/common/Navbar";

const Layout = () => {
  return (
    <>
      <Navbar />
      <div className="my-20 mx-8 ">
        <Outlet />
      </div>
    </>
  );
};

export default Layout;
