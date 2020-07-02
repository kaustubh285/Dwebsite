import React, { Fragment } from "react";

export default function Myskill({ oneskill }) {
  return (
    <div className="oneskilled bg-white text-dark">
      <h4 className="mb-0">
        {oneskill.title}{" "}
        <img src={oneskill.logo} className="" height="30px" width="30px" />
      </h4>
      <div className=" w-100 text-center "></div>
    </div>
  );
}
