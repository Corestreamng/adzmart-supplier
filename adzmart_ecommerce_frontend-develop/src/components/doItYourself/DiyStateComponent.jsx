import React, {useState} from "react";

import {
  DiySelectStateCont,
  AdzSelectMultipleInput,
  AdzSelectOption,
  AdzSelectOptionBox,
  AdzInputBox,
  DiySelectStateWrapper,
  AdzSelectedState,
  AdzRemoveState,
  AdzSelectedStatesCont,
} from "./doItYourselfStyles";

import {nigerianState} from "../../AdzmartUtils/diyUtils";
import {Typography} from "@mui/material";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";

function DiyStateComponent({show}) {
  let [showDropDown, setShowDropDown] = useState(false);
  let [selectedState, setSelectedState] = useState([]);

  let addState = (state) => {
    if (selectedState.includes(state)) {
      return;
    }
    setSelectedState((prev) => [...prev, state]);
  };

  let removeState = (state) => {
    let newStateList = selectedState.filter((item) => item !== state);
    setSelectedState(newStateList);
    // console.log(newStateList);
  };

  return (
    <>
      <DiySelectStateWrapper show={show === 1 ? true : false}>
        <Typography variant={"body2"}>
          Where do you want to advertise
        </Typography>
        <AdzSelectedStatesCont>
          {selectedState.length > 0 &&
            selectedState.map((item, index) => {
              return (
                <AdzSelectedState key={index}>
                  <Typography variant="body1">{item}</Typography>
                  <AdzRemoveState onClick={() => removeState(item)}>
                    x
                  </AdzRemoveState>
                </AdzSelectedState>
              );
            })}
        </AdzSelectedStatesCont>
        <DiySelectStateCont>
          <AdzInputBox size={"80%"}>
            <AdzSelectMultipleInput
              onClick={() => {
                setShowDropDown(!showDropDown);
              }}
            >
              {selectedState.length > 0
                ? selectedState.map((item, index) => {
                    return `${item}, `;
                  })
                : "Select at least on state"}

              <ArrowDropDownIcon />
            </AdzSelectMultipleInput>
            <AdzSelectOptionBox showdd={showDropDown}>
              {nigerianState.map((item, index) => (
                <AdzSelectOption key={index} onClick={() => addState(item)}>
                  {item}
                </AdzSelectOption>
              ))}
            </AdzSelectOptionBox>
          </AdzInputBox>
        </DiySelectStateCont>
      </DiySelectStateWrapper>
    </>
  );
}

export default DiyStateComponent;
