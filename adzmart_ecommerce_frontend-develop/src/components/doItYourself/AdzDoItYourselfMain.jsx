import React, {useState, memo} from "react";
import {
  OutterContainer,
  Innercontainer,
  SectionWrap,
} from "../../adzmartStyles/commonCompStyles";

import {
  DiyFlexCont,
  DiyActivityCont,
  DiyImageCont,
  DiyButtonCont,
  DiyBackButton,
  DiyContinueButon,
  DiyImage,
} from "./doItYourselfStyles";
import DiyStateComponent from "./DiyStateComponent";
import DiyOptionsComponent from "./DiyOptionsComponent";
import DiyPreferredMedia from "./DiyPreferredMedia";
import DiyCampaignBudget from "./DiyCampaignBudget";
import DiyUploadMedia from "./DiyUploadMedia";

import {Typography} from "@mui/material";

function AdzDoItYourselfMain() {
  let [showActivity, setShowActivity] = useState(1);

  let handleContinueActivity = () => {
    if (showActivity === 5) {
      return;
    }

    setShowActivity((showActivity += 1));
  };

  let handleBackActivity = () => {
    if (showActivity === 1) {
      return;
    }

    setShowActivity((showActivity -= 1));
  };

  return (
    <>
      {/* {console.log(showActivity)} */}
      <OutterContainer>
        <SectionWrap>
          <Innercontainer sx={{paddingTop: 10}}>
            <Typography variant={"subtitle1"}>Start your campaign</Typography>
            <DiyFlexCont>
              <DiyActivityCont>
                <DiyStateComponent show={showActivity} />
                <DiyOptionsComponent show={showActivity} />
                <DiyPreferredMedia show={showActivity} />
                <DiyCampaignBudget show={showActivity} />
                <DiyUploadMedia show={showActivity} />
              </DiyActivityCont>

              <DiyImageCont>
                <DiyImage src="/images/doityourself/diyimg.png" />
              </DiyImageCont>
            </DiyFlexCont>

            <DiyButtonCont>
              <DiyBackButton onClick={handleBackActivity}>Back</DiyBackButton>
              <DiyContinueButon onClick={handleContinueActivity}>
                Continue
              </DiyContinueButon>
            </DiyButtonCont>
          </Innercontainer>
        </SectionWrap>
      </OutterContainer>
    </>
  );
}

export default memo(AdzDoItYourselfMain);
