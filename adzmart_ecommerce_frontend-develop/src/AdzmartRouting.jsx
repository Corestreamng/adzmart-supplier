import React, {memo} from "react";
import {BrowserRouter, Routes, Route} from "react-router-dom";
import AdzmartHomePage from "./components/homepage/AdzmartHomePage";
import AdzmartLogin from "./components/loginPage/AdzmartLogin";
import AdzmartNavigation from "./components/navigation/AdzmartNavigation";
import AdzmartFooterSection from "./components/footer/AdzmartFooterSection";
import AdzDoItYourselfMain from "./components/doItYourself/AdzDoItYourselfMain";
import AdzDoneForYouMain from "./components/doneForYou/AdzDoneForYouMain";
// import SignUpPage from "./components/signUpPage/SignUpPage";

function AdzmartRouting() {
  return (
    <BrowserRouter>
      <AdzmartNavigation />
      <Routes>
        <Route path="/" element={<AdzmartHomePage />} />
        <Route path="/login" element={<AdzmartLogin />} />
        <Route path="/doItYourself" element={<AdzDoItYourselfMain />} />
        <Route path="/doneForYou" element={<AdzDoneForYouMain />} />
      </Routes>
      <AdzmartFooterSection />
    </BrowserRouter>
  );
}

export default memo(AdzmartRouting);
