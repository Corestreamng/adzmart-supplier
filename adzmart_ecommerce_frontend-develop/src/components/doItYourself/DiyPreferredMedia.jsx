import React from "react";

import {
  DiyPreferredOptionCont,
  DiyPreferredOptionItem,
  DiyPreferredOptionWrapper,
  DiyPreferredOptionRadioLabel,
  DiyPreferredOptionRadioInput,
} from "./doItYourselfStyles";

import {Typography} from "@mui/material";

function DiyPreferredMedia({show}) {
  return (
    <>
      <DiyPreferredOptionWrapper show={show === 3 ? true : false}>
        <Typography variant="h5" sx={{margin: "2rem 0 0.5rem 0"}}>
          Select your preferred media
        </Typography>
        <Typography variant="body1">
          Select at least one platform for your advertisement
        </Typography>

        <DiyPreferredOptionCont>
          <DiyPreferredOptionItem>
            <DiyPreferredOptionRadioInput type={"checkbox"} id="Television" />
            <DiyPreferredOptionRadioLabel htmlFor="Television">
              Television
            </DiyPreferredOptionRadioLabel>
          </DiyPreferredOptionItem>

          <DiyPreferredOptionItem>
            <DiyPreferredOptionRadioInput
              type={"checkbox"}
              id="Newspaper / Magazine"
            />
            <DiyPreferredOptionRadioLabel htmlFor="Newspaper / Magazine">
              Newspaper / Magazine
            </DiyPreferredOptionRadioLabel>
          </DiyPreferredOptionItem>

          <DiyPreferredOptionItem>
            <DiyPreferredOptionRadioInput type={"checkbox"} id="Radio" />
            <DiyPreferredOptionRadioLabel htmlFor="Radio">
              Radio
            </DiyPreferredOptionRadioLabel>
          </DiyPreferredOptionItem>

          <DiyPreferredOptionItem>
            <DiyPreferredOptionRadioInput type={"checkbox"} id="Digital" />
            <DiyPreferredOptionRadioLabel htmlFor="Digital">
              Digital
            </DiyPreferredOptionRadioLabel>
          </DiyPreferredOptionItem>

          <DiyPreferredOptionItem>
            <DiyPreferredOptionRadioInput type={"checkbox"} id="Online" />
            <DiyPreferredOptionRadioLabel htmlFor="Online">
              Online
            </DiyPreferredOptionRadioLabel>
          </DiyPreferredOptionItem>

          <DiyPreferredOptionItem>
            <DiyPreferredOptionRadioInput type={"checkbox"} id="Out of Home" />
            <DiyPreferredOptionRadioLabel htmlFor="Out of Home">
              Out of Home
            </DiyPreferredOptionRadioLabel>
          </DiyPreferredOptionItem>

          <DiyPreferredOptionItem>
            <DiyPreferredOptionRadioInput type={"checkbox"} id="Cinemas" />
            <DiyPreferredOptionRadioLabel htmlFor="Cinemas">
              Cinemas
            </DiyPreferredOptionRadioLabel>
          </DiyPreferredOptionItem>
        </DiyPreferredOptionCont>
      </DiyPreferredOptionWrapper>
    </>
  );
}

export default DiyPreferredMedia;
