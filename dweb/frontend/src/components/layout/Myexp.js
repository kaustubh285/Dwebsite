import React, { Fragment } from "react";

export default function MyExperience({ oneexp }) {
  return (
    <div className="expcontainer">
      <h3 className="text-center text-dark" style={{ minHeight: "30px" }}>
        {oneexp.org}
      </h3>

      <img className="expimage" src={oneexp.logo} />
      <div className="expmiddle">
        <hr></hr>
        <small className="exptext w-100">{oneexp.description}</small>
        <hr></hr>
      </div>
    </div>
  );
}
