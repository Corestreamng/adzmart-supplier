import React, {useContext} from "react";
import {AdzmartContext} from "../../AdzmartContext/AdzmartContextProvider";

function AdzmartLogin() {
  let {value} = useContext(AdzmartContext);
  console.log(value);
  return <div></div>;
}

export default AdzmartLogin;
