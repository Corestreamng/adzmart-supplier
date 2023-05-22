import React, {memo} from "react";
import {
  OutterContainer,
  Innercontainer,
  AdzmartLargeBtnWhite,
  AdzmartAltBtn,
  flexEnd,
} from "../../adzmartStyles/commonCompStyles";
import {
  AdzFooterWrap,
  AdzFooterLogo,
  AdzFooterBox,
  AdzFooterFlex,
  AdzFooterLinkCont,
  AdzFootermargin,
} from "./AdzmartFooterStyles";
import {Box, Stack, Typography} from "@mui/material";

function AdzmartFooterSection() {
  return (
    <>
      <OutterContainer>
        <AdzFooterWrap>
          <Innercontainer>
            <AdzFooterLogo src="/images/adsmarketwhitelogo.png" />
            <Stack sx={AdzFooterFlex}>
              <Box sx={AdzFooterBox}>
                <Typography variant="h3" sx={AdzFootermargin}>
                  Links
                </Typography>
                <AdzFooterLinkCont>
                  <AdzmartAltBtn shade="white">All Media</AdzmartAltBtn>
                  <AdzmartAltBtn shade="white">TV</AdzmartAltBtn>
                  <AdzmartAltBtn shade="white">OOH</AdzmartAltBtn>
                  <AdzmartAltBtn shade="white">Radio</AdzmartAltBtn>
                  <AdzmartAltBtn shade="white">Cinemas</AdzmartAltBtn>
                  <AdzmartAltBtn shade="white">Online</AdzmartAltBtn>
                  <AdzmartAltBtn shade="white">Special Offers</AdzmartAltBtn>
                </AdzFooterLinkCont>
              </Box>
              <Box sx={AdzFooterBox}>
                <Stack sx={flexEnd}>
                  <AdzmartLargeBtnWhite>
                    Subscribe to Newsletter
                  </AdzmartLargeBtnWhite>
                </Stack>
              </Box>
            </Stack>
          </Innercontainer>
        </AdzFooterWrap>
      </OutterContainer>
    </>
  );
}

export default memo(AdzmartFooterSection);
