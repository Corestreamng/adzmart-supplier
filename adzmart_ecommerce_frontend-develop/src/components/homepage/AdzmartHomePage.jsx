import React, {memo} from "react";
import AdzmartHeroSection from "./AdzmartHeroSection";
import AdzmartServiceSection from "./AdzmartServiceSection";
import AdzmartFeatureSection from "./AdzmartFeatureSection";
import AdzmartMoreServiceSection from "./AdzmartMoreServiceSection";
import AdzmartMarketPlaceSection from "./AdzmartMarketPlaceSection";

function AdzmartHomePage() {
  return (
    <>
      <AdzmartHeroSection />
      <AdzmartServiceSection />
      <AdzmartFeatureSection />
      <AdzmartMoreServiceSection />
      <AdzmartMarketPlaceSection />
    </>
  );
}

export default memo(AdzmartHomePage);
