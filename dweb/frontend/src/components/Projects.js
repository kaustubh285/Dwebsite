import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import Myproject from "./layout/Myproject";

function Projects() {
  const [projects, setProject] = useState([]);

  const url = "http://localhost:8000/api/projects/";

  useEffect(() => {
    try {
      const res = fetch(url);
      // const data = res.json();
      res
        .then((response) => response.json())
        .then((arrayOfUsers) => {
          setProject(arrayOfUsers);
        });
    } catch (err) {
      console.error(err);
    }
  }, []);

  return (
    <div className="myskill d-flex bg-secondary flex-wrap mt-6">
      {projects.map((oneproject) => (
        <Myproject oneproject={oneproject} key={oneproject.id} />
      ))}
    </div>
  );
}

ReactDOM.render(<Projects />, document.getElementById("projects"));
