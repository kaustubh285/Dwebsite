import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import Myskill from "./layout/Myskill";

function Skills() {
  const [skill, setSkill] = useState([]);

  const url = "http://localhost:8000/api/skills/";

  useEffect(() => {
    try {
      const res = fetch(url);
      // const data = res.json();
      res
        .then((response) => response.json())
        .then((arrayOfUsers) => {
          setSkill(arrayOfUsers);
        });
    } catch (err) {
      console.error(err);
    }
  }, []);

  return (
    <div className="myskill d-flex bg-secondary flex-wrap mt-6">
      {skill.map((oneskill) => (
        <Myskill oneskill={oneskill} key={oneskill.id} />
      ))}
    </div>
  );
}

ReactDOM.render(<Skills />, document.getElementById("skills"));
