import React, { Fragment } from "react";
import ReactDOM from "react-dom";
import Bodypart from "./layout/Bodypart";

class MainBody extends React.Component {
  render() {
    return (
      <Fragment>
        <Bodypart />
      </Fragment>
    );
  }
}

ReactDOM.render(<MainBody />, document.getElementById("mainBody"));
