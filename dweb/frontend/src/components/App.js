import React, { Fragment } from "react";
import ReactDOM from "react-dom";
import Navb from "./layout/Navb";

class App extends React.Component {
  render() {
    return (
      <Fragment>
        <Navb />
      </Fragment>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
