import React from "react";
import {
  OutterContainer,
  Innercontainer,
  AdzmartItemWrap,
  Adz_fs_ItemFlex,
  Adz_fs_ItemBoxW,
  Adz_fs_ItemImg,
  Adz_fs_ItemImgBox,
  AdzmartAltBtn,
  commonFlex,
  AdzmartLargeBtn,
  SectionWrapAlt,
} from "../../adzmartStyles/commonCompStyles";
import {
  AdzSsFlexcont,
  AdzSsLeftBox,
  AdzSsDesignElement1,
  AdzSsDesignElement2,
  AdzSsRightBox,
  AdzSsImg,
  AdzSsHeaderMargin,
  AdzSsTextMargin,
  AdzSsMoreOptionsBox,
  AdzSsHeader2Margin,
  AdzSsMoreOptionsFlex,
  AdzSsOptionsImg,
  AdzSsOptions2Flex,
  AdzSsOptions2LargeBox,
  AdzSsOptions2SmallBox,
  AdzSsOptionsButtonCenter,
} from "./homePageStyles";
import {Box, Stack, Typography} from "@mui/material";

function AdzmartMoreServiceSection() {
  return (
    <>
      <OutterContainer>
        <SectionWrapAlt size="100vh">
          <Innercontainer>
            <Stack sx={AdzSsFlexcont}>
              <AdzSsLeftBox>
                <AdzSsDesignElement1 />
                <AdzSsDesignElement2 />
                <AdzSsImg src="/images/whyadzmarticon.png" />
              </AdzSsLeftBox>

              <AdzSsRightBox>
                <Typography variant="h1">Why</Typography>
                <Typography variant="h1" sx={AdzSsHeaderMargin}>
                  Adzmart?
                </Typography>
                <Box>
                  <Typography variant="body1" sx={AdzSsTextMargin}>
                    Dint antihyn. Pretodade vasamma. Komfaktisk kudirat.
                    Pladäligt popp. Dingen estetisk kompetens.{" "}
                  </Typography>

                  <Typography variant="body1" sx={AdzSsTextMargin}>
                    Rere favada. Jerat kvasiment. Dedosm infrakena. Fadat
                    epikeck, ninir. Mänyposade desk och deren. Föl diktig. Ill
                    relingar. Sperade oteskade. Misat. Tir traligt. Ses. Vir
                    trede, emedan epimenade. Höning resm. Poligen besam och
                    spelig. Makrock mådisade. Nese div. Tinade dokäd i diska.
                    Hundvissla ädon. Vasa trenektig alltså rölosamma. Årönt
                    plalig vins.
                  </Typography>

                  <Typography variant="body1">
                    Rere favada. Jerat kvasiment. Dedosm infrakena. Fadat
                    epikeck, ninir. Mänyposade desk och deren. Föl diktig. Ill
                    relingar. Sperade oteskade. Misat. Tir traligt. Ses. Vir
                    trede, emedan epimenade. Höning resm. Poligen besam och
                    spelig. Makrock mådisade. Nese div. Tinade dokäd i diska.
                    Hundvissla ädon. Vasa trenektig alltså rölosamma. Årönt
                    plalig vins.
                  </Typography>
                </Box>
              </AdzSsRightBox>
            </Stack>
          </Innercontainer>
        </SectionWrapAlt>

        <Box sx={AdzSsMoreOptionsBox}>
          <Innercontainer>
            <Typography variant="h1" sx={AdzSsHeader2Margin}>
              More Options
            </Typography>

            <Stack sx={AdzSsMoreOptionsFlex}>
              <AdzmartItemWrap>
                <Typography variant="subtitle1" sx={AdzSsTextMargin}>
                  Synergy
                </Typography>
                <Typography variant="body1">
                  Posekasade vön. Tonde diburad. Stereotion intranade. Nysm
                  makrogisk bidirade. Sper hemiska, ganat.{" "}
                </Typography>
                <Stack>
                  <AdzSsOptionsImg src="/images/timeoptions.png" />
                </Stack>
              </AdzmartItemWrap>

              <AdzmartItemWrap>
                <Typography variant="subtitle1" sx={AdzSsTextMargin}>
                  Integration
                </Typography>
                <Typography variant="body1">
                  Posekasade vön. Tonde diburad. Stereotion intranade. Nysm
                  makrogisk bidirade. Sper hemiska, ganat.{" "}
                </Typography>
                <Stack>
                  <AdzSsOptionsImg src="/images/timeoptions.png" />
                </Stack>
              </AdzmartItemWrap>

              <AdzmartItemWrap>
                <Typography variant="subtitle1" sx={AdzSsTextMargin}>
                  Automation
                </Typography>
                <Typography variant="body1">
                  Posekasade vön. Tonde diburad. Stereotion intranade. Nysm
                  makrogisk bidirade. Sper hemiska, ganat.{" "}
                </Typography>
                <Stack>
                  <AdzSsOptionsImg src="/images/timeoptions.png" />
                </Stack>
              </AdzmartItemWrap>
            </Stack>
          </Innercontainer>
        </Box>

        <Box>
          <Innercontainer>
            <Stack sx={AdzSsOptions2Flex}>
              <Box sx={AdzSsOptions2LargeBox}>
                <AdzmartItemWrap>
                  <Adz_fs_ItemFlex>
                    <Adz_fs_ItemBoxW>
                      <Typography variant="subtitle1">Television</Typography>
                      <Typography
                        variant="body1"
                        sx={{margin: "1rem 0 3rem 0"}}
                      >
                        Lorem ipsum dolor sit amet consectetur, adipisicing
                        elit. Fugiat, quae aut? Aperiam, accusantium ea harum
                        laboriosam dolor odit voluptatum aliquam, est nostrum
                        maxime, inventore quod.
                      </Typography>
                      <AdzmartAltBtn>Start Now</AdzmartAltBtn>
                    </Adz_fs_ItemBoxW>

                    <Box sx={Adz_fs_ItemImgBox}>
                      <Adz_fs_ItemImg
                        src="/images/bookingadverts.png"
                        sx={{width: "8rem"}}
                      />
                    </Box>
                  </Adz_fs_ItemFlex>
                </AdzmartItemWrap>
              </Box>

              <Box sx={AdzSsOptions2SmallBox}>
                <AdzmartItemWrap>
                  <Typography variant="subtitle1" sx={AdzSsTextMargin}>
                    Billboard
                  </Typography>
                  <Typography variant="body1">
                    Posekasade vön. Tonde diburad. Stereotion intranade. Nysm
                    makrogisk bidirade. Sper hemiska, ganat.{" "}
                  </Typography>
                  <Stack>
                    <AdzSsOptionsImg src="/images/timeoptions.png" />
                  </Stack>
                </AdzmartItemWrap>
              </Box>
            </Stack>

            <Stack sx={commonFlex}>
              <AdzmartItemWrap>
                <Adz_fs_ItemFlex>
                  <Adz_fs_ItemBoxW size="60%">
                    <Typography variant="subtitle1">Radio </Typography>
                    <Typography variant="body1" sx={{margin: "1rem 0 3rem 0"}}>
                      Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                      Fugiat, quae aut? Aperiam, accusantium ea harum laboriosam
                      dolor odit voluptatum aliquam, est nostrum maxime,
                      inventore quod.
                    </Typography>
                    <AdzmartAltBtn>Start Now</AdzmartAltBtn>
                  </Adz_fs_ItemBoxW>

                  <Box sx={Adz_fs_ItemImgBox}>
                    <Adz_fs_ItemImg
                      src="/images/timeoptions.png"
                      sx={{width: "8rem"}}
                    />
                  </Box>
                </Adz_fs_ItemFlex>
              </AdzmartItemWrap>

              <AdzmartItemWrap>
                <Adz_fs_ItemFlex>
                  <Adz_fs_ItemBoxW size="60%">
                    <Typography variant="subtitle1">Cinema </Typography>
                    <Typography variant="body1" sx={{margin: "1rem 0 3rem 0"}}>
                      Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                      Fugiat, quae aut? Aperiam, accusantium ea harum laboriosam
                      dolor odit voluptatum aliquam, est nostrum maxime,
                      inventore quod.
                    </Typography>
                    <AdzmartAltBtn>Start Now</AdzmartAltBtn>
                  </Adz_fs_ItemBoxW>

                  <Box sx={Adz_fs_ItemImgBox}>
                    <Adz_fs_ItemImg
                      src="/images/marketplace.png"
                      sx={{width: "8rem"}}
                    />
                  </Box>
                </Adz_fs_ItemFlex>
              </AdzmartItemWrap>
            </Stack>

            <Stack sx={AdzSsOptionsButtonCenter}>
              <AdzmartLargeBtn>See More</AdzmartLargeBtn>
            </Stack>
          </Innercontainer>
        </Box>
      </OutterContainer>
    </>
  );
}

export default AdzmartMoreServiceSection;
