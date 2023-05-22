import React from "react";
import {
  OutterContainer,
  Innercontainer,
  AdzmartSmallBtn,
  SectionWrap,
} from "../../adzmartStyles/commonCompStyles";
import {HeroImage, HeroTextCont, InputContainer} from "./homePageStyles";
import {Typography, Stack, Box} from "@mui/material";

function AdzmartHeroSection() {
  return (
    <>
      <OutterContainer>
        <SectionWrap>
          <Innercontainer>
            <HeroTextCont>
              <Typography variant="h1">Plan.</Typography>
              <Typography variant="h1">Book.</Typography>
              <Typography variant="h1">Advertise.</Typography>
              <Box sx={{width: "40%", margin: "2rem 0"}}>
                <Typography variant="body2">
                  adzmart is an online platform democratising the process of
                  media buying in by providing marketplace which facilitates
                  convenient,fast and effecient media buying activities.
                </Typography>
              </Box>
              <Stack direction="row" gap={2}>
                <Box>
                  <InputContainer
                    placeholder="Email Address"
                    sx={{fontSize: "1rem"}}
                  />
                </Box>
                <AdzmartSmallBtn>Get Started</AdzmartSmallBtn>
              </Stack>
            </HeroTextCont>
            <HeroImage src="/images/heroSectionPic.png" />
          </Innercontainer>
        </SectionWrap>
      </OutterContainer>
    </>
  );
}

export default AdzmartHeroSection;
