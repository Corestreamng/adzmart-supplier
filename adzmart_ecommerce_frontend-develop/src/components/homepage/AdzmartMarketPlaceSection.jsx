import React from "react";
import {
  OutterContainer,
  Innercontainer,
  AdzmartLargeBtn,
  SectionWrapAlt,
} from "../../adzmartStyles/commonCompStyles";

import {
  AdzMpBoxFlex,
  AdzMpContentBox,
  AdzSsHeaderMargin,
  AdzSsTextMargin,
  AdzMpButtonMargin,
} from "./homePageStyles";
import {Stack, Box, Typography} from "@mui/material";

function AdzmartMarketPlaceSection() {
  return (
    <>
      <OutterContainer>
        <SectionWrapAlt size="100vh">
          <Innercontainer>
            <Stack sx={AdzMpBoxFlex}>
              <Box sx={AdzMpContentBox}>
                <Typography variant="h1">Search</Typography>
                <Typography variant="h1" sx={AdzSsHeaderMargin}>
                  Market Place
                </Typography>
                <Typography variant="body1" sx={AdzSsTextMargin}>
                  Dint antihyn. Pretodade vasamma. Komfaktisk kudirat. Pladäligt
                  popp. Dingen estetisk kompetens.{" "}
                </Typography>
                <Typography variant="body1" sx={AdzSsTextMargin}>
                  Rere favada. Jerat kvasiment. Dedosm infrakena. Fadat epikeck,
                  ninir. Mänyposade desk och deren. Föl diktig. Ill relingar.
                  Sperade oteskade. Misat. Tir traligt. Ses. Vir trede, emedan
                  epimenade. Höning resm. Poligen besam och spelig. Makrock
                  mådisade. Nese div. Tinade dokäd i diska. Hundvissla ädon.
                  Vasa trenektig alltså rölosamma. Årönt plalig vins.{" "}
                </Typography>
                <AdzmartLargeBtn sx={AdzMpButtonMargin}>
                  View Marketplace
                </AdzmartLargeBtn>
              </Box>
            </Stack>
          </Innercontainer>
        </SectionWrapAlt>
      </OutterContainer>
    </>
  );
}

export default AdzmartMarketPlaceSection;
