import React from "react";
import {
  OutterContainer,
  Innercontainer,
  AdzmartLargeBtn,
  AdzmartItemWrap,
  AdzmartMediumBtn,
  SectionWrapAlt,
  AdzLink,
} from "../../adzmartStyles/commonCompStyles";
import {
  SearchInputBox,
  SearchInput,
  SearchInputWrap,
  ServiceItemCont,
} from "./homePageStyles";
import {Typography} from "@mui/material";

function AdzmartServiceSection() {
  return (
    <>
      <OutterContainer>
        <SectionWrapAlt>
          <Innercontainer>
            {/* for the serach input */}
            <SearchInputWrap direction="row">
              <SearchInputBox>
                <SearchInput />
              </SearchInputBox>
              <AdzmartLargeBtn>Search Now</AdzmartLargeBtn>
            </SearchInputWrap>

            <ServiceItemCont direction="row">
              <AdzmartItemWrap>
                <Typography variant="subtitle1">Done for you</Typography>
                <Typography variant="subtitle1">Services</Typography>
                <Typography variant="body1" sx={{marginBottom: "1rem"}}>
                  Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                  Molestias perferendis eius iure obcaecati quasi eaque minima
                  veritatis laudantium excepturi! Praesentium!
                </Typography>
                <AdzmartMediumBtn>
                  <AdzLink to="doneForYou">Start now</AdzLink>
                </AdzmartMediumBtn>
              </AdzmartItemWrap>

              <AdzmartItemWrap>
                <Typography variant="subtitle1">Do it yourself</Typography>
                <Typography variant="subtitle1">Services</Typography>
                <Typography variant="body1" sx={{marginBottom: "1rem"}}>
                  Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                  Molestias perferendis eius iure obcaecati quasi eaque minima
                  veritatis laudantium excepturi! Praesentium!
                </Typography>
                <AdzmartMediumBtn>
                  <AdzLink to="doItYourself">Start now</AdzLink>
                </AdzmartMediumBtn>
              </AdzmartItemWrap>

              <AdzmartItemWrap>
                <Typography variant="subtitle1">Marketplace</Typography>
                <Typography variant="subtitle1">Services</Typography>
                <Typography variant="body1" sx={{marginBottom: "1rem"}}>
                  Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                  Molestias perferendis eius iure obcaecati quasi eaque minima
                  veritatis laudantium excepturi! Praesentium!
                </Typography>
                <AdzmartMediumBtn>Start now</AdzmartMediumBtn>
              </AdzmartItemWrap>
            </ServiceItemCont>
          </Innercontainer>
        </SectionWrapAlt>
      </OutterContainer>
    </>
  );
}

export default AdzmartServiceSection;
