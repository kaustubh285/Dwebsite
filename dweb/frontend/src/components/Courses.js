import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import Mycourse from "./layout/Mycourse";

function Courses() {
  const [courses, setCourse] = useState([]);

  const url = "http://localhost:8000/api/courses/";

  useEffect(() => {
    try {
      const res = fetch(url);
      // const data = res.json();
      res
        .then((response) => response.json())
        .then((arrayOfUsers) => {
          setCourse(arrayOfUsers);
        });
    } catch (err) {
      console.error(err);
    }
  }, []);

  return (
    <div className="mycourse d-flex bg-secondary flex-wrap mt-6">
      {courses.map((onecourse) => (
        <Mycourse onecourse={onecourse} key={onecourse.id} />
      ))}
    </div>
  );
}

ReactDOM.render(<Courses />, document.getElementById("courses"));
