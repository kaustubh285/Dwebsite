import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import MyExperience from "./layout/Myexp";

function Experience() {
  const [experience, setExperience] = useState([]);

  const url = "http://localhost:8000/api/experience/";

  useEffect(() => {
    try {
      const res = fetch(url);
      // const data = res.json();
      res
        .then((response) => response.json())
        .then((arrayOfUsers) => {
          setExperience(arrayOfUsers);
        });
    } catch (err) {
      console.error(err);
    }
  }, []);

  return (
    <div className="myexp d-flex bg-secondary flex-wrap mt-6">
      {experience.map((oneexp) => (
        <MyExperience oneexp={oneexp} key={oneexp.id} />
      ))}
    </div>
  );
}

ReactDOM.render(<Experience />, document.getElementById("experiences"));
