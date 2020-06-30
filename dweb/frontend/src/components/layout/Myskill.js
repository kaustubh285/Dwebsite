import React, { Fragment } from "react";

export default function Myskill({ oneskill }) {
  return (
    <div>
      <h1>
        {oneskill.title} : {oneskill.level}
      </h1>
    </div>
  );
}
