import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import Mycertificates from "./layout/Mycertificates";

function Certificates() {
  const [certificates, setCertificates] = useState([]);

  const url = "http://localhost:8000/api/certificates/";

  useEffect(() => {
    try {
      const res = fetch(url);
      // const data = res.json();
      res
        .then((response) => response.json())
        .then((arrayOfUsers) => {
          setCertificates(arrayOfUsers);
        });
    } catch (err) {
      console.error(err);
    }
  }, []);

  return (
    <div className="myproject d-flex bg-secondary flex-wrap mt-6">
      {certificates.map((onecerti) => (
        <Mycertificates onecerti={onecerti} key={onecerti.id} />
      ))}
    </div>
  );
}

ReactDOM.render(<Certificates />, document.getElementById("certificates"));
