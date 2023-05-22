import React from "react";
import {
  OutterContainer,
  Innercontainer,
  AdzmartItemWrap,
  AdzmartAltBtn,
  Adz_fs_ItemFlex,
  Adz_fs_ItemBoxW,
  Adz_fs_ItemImg,
  Adz_fs_ItemImgBox,
} from "../../adzmartStyles/commonCompStyles";
import {
  Adz_fs_TitleWrapper,
  Adz_fs_TitleBox,
  Adz_fs_flexcont,
} from "./homePageStyles";
import {Typography, Box, Stack} from "@mui/material";

function AdzmartFeatureSection() {
  return (
    <>
      <OutterContainer>
        <Innercontainer>
          <Adz_fs_TitleWrapper>
            <Adz_fs_TitleBox>
              <Typography variant="h1">Features</Typography>
              <Typography variant="body1">
                Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                Aperiam facilis impedit ut. Esse, officiis libero? At voluptatem
                molestias eius autem?
              </Typography>
            </Adz_fs_TitleBox>

            <AdzmartItemWrap>
              <Adz_fs_ItemFlex>
                <Adz_fs_ItemBoxW>
                  <Typography variant="subtitle1">
                    Book Adverts Across Diffrent Adverts
                  </Typography>
                  <Typography variant="body1" sx={{margin: "1rem 0 3rem 0"}}>
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    Fugiat, quae aut? Aperiam, accusantium ea harum laboriosam
                    dolor odit voluptatum aliquam, est nostrum maxime, inventore
                    quod.
                  </Typography>
                  <AdzmartAltBtn>Start Now</AdzmartAltBtn>
                </Adz_fs_ItemBoxW>

                <Box sx={Adz_fs_ItemImgBox}>
                  <Adz_fs_ItemImg src="/images/bookingadverts.png" />
                </Box>
              </Adz_fs_ItemFlex>
            </AdzmartItemWrap>
          </Adz_fs_TitleWrapper>

          <Stack direction={"row"} sx={Adz_fs_flexcont}>
            <AdzmartItemWrap>
              <Adz_fs_ItemFlex>
                <Adz_fs_ItemBoxW size="60%">
                  <Typography variant="subtitle1">
                    Book Adverts Across Diffrent Adverts
                  </Typography>
                  <Typography variant="body1" sx={{margin: "1rem 0 3rem 0"}}>
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    Fugiat, quae aut? Aperiam, accusantium ea harum laboriosam
                    dolor odit voluptatum aliquam, est nostrum maxime, inventore
                    quod.
                  </Typography>
                  <AdzmartAltBtn>Start Now</AdzmartAltBtn>
                </Adz_fs_ItemBoxW>

                <Box sx={Adz_fs_ItemImgBox}>
                  <Adz_fs_ItemImg src="/images/timeoptions.png" size="8rem" />
                </Box>
              </Adz_fs_ItemFlex>
            </AdzmartItemWrap>

            <AdzmartItemWrap>
              <Adz_fs_ItemFlex>
                <Adz_fs_ItemBoxW size="60%">
                  <Typography variant="subtitle1">
                    Book Adverts Across Diffrent Adverts
                  </Typography>
                  <Typography variant="body1" sx={{margin: "1rem 0 3rem 0"}}>
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    Fugiat, quae aut? Aperiam, accusantium ea harum laboriosam
                    dolor odit voluptatum aliquam, est nostrum maxime, inventore
                    quod.
                  </Typography>
                  <AdzmartAltBtn>Start Now</AdzmartAltBtn>
                </Adz_fs_ItemBoxW>

                <Box sx={Adz_fs_ItemImgBox}>
                  <Adz_fs_ItemImg src="/images/marketplace.png" size="8rem" />
                </Box>
              </Adz_fs_ItemFlex>
            </AdzmartItemWrap>
          </Stack>
        </Innercontainer>
      </OutterContainer>
    </>
  );
}

export default AdzmartFeatureSection;
