import {Typography} from "@mui/material";
import React from "react";

import {
  DiyUploadMediaWrapper,
  DiyUploadMediaDateCont,
  DiyUploadMediaDateitem,
  DiyUploadMediaInput,
  DiyUploadMediaIcon,
  DiyUploadMediaShowItemCont,
  DiyUploadMediaImg,
  DiyUploadMediaImgCont,
} from "./doItYourselfStyles";

import CalendarTodayIcon from "@mui/icons-material/CalendarToday";

function DiyUploadMedia({show}) {
  return (
    <>
      <DiyUploadMediaWrapper show={show === 5 ? true : false}>
        <Typography variant="body1">When is your campaign breaking?</Typography>
        <DiyUploadMediaDateCont size="90%">
          <DiyUploadMediaDateitem size="45%">
            <DiyUploadMediaInput
              type={"text"}
              placeholder=" Start date dd/mm/year"
            />
            <DiyUploadMediaIcon>
              <CalendarTodayIcon />
            </DiyUploadMediaIcon>
          </DiyUploadMediaDateitem>

          <DiyUploadMediaDateitem size="45%">
            <DiyUploadMediaInput
              type={"text"}
              placeholder=" End date dd/mm/year"
            />
            <DiyUploadMediaIcon>
              <CalendarTodayIcon />
            </DiyUploadMediaIcon>
          </DiyUploadMediaDateitem>
        </DiyUploadMediaDateCont>

        <DiyUploadMediaShowItemCont></DiyUploadMediaShowItemCont>
        <Typography variant="body1">Upload the following:</Typography>
        <DiyUploadMediaImgCont>
          <DiyUploadMediaImg src="/images/doityourself/uploadvideo.png" />
          <DiyUploadMediaImg src="/images/doityourself/uploadapproval.png" />
          <DiyUploadMediaImg src="/images/doityourself/uploadothers.png" />
        </DiyUploadMediaImgCont>
      </DiyUploadMediaWrapper>
    </>
  );
}

export default DiyUploadMedia;
