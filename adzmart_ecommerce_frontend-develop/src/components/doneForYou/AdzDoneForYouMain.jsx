import React from "react";
import {
  OutterContainer,
  Innercontainer,
  SectionWrapPlain,
} from "../../adzmartStyles/commonCompStyles";
import {Typography} from "@mui/material";

const AdzDoneForYouMain = () => {
  return (
    <>
      <OutterContainer>
        <SectionWrapPlain>
          <Innercontainer>
            <Typography variant={"subtitle1"}> RFP Listinings</Typography>
          </Innercontainer>
        </SectionWrapPlain>
      </OutterContainer>
    </>
  );
};

export default AdzDoneForYouMain;
