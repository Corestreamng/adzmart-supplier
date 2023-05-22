import React, {useRef, useState, useEffect} from "react";
import {
  OutterContainer,
  Innercontainer,
  AdzmartNavBtn,
  AdzmartMediumBtn,
} from "../../adzmartStyles/commonCompStyles";
import {
  AdzmartBlueLogo,
  NavItemsCont,
  NavLinkCont,
  AdzmartNavCont,
  AdzmartNavObserver,
} from "./navigationStyles";

function AdzmartNavigation() {
  const navRef = useRef();
  let [intersecting, setIntersecting] = useState(false);

  useEffect(() => {
    const navObserver = new IntersectionObserver(([entry], observer) => {
      setIntersecting(entry.isIntersecting);
    });

    navObserver.observe(navRef.current);
  }, []);

  return (
    <>
      <AdzmartNavObserver ref={navRef} />
      <AdzmartNavCont show={intersecting}>
        <OutterContainer>
          <Innercontainer>
            <NavItemsCont>
              <AdzmartBlueLogo src="/images/adsmarket-blue-logo.png" />
              <NavLinkCont>
                <AdzmartNavBtn>all media</AdzmartNavBtn>
                <AdzmartNavBtn>tv</AdzmartNavBtn>
                <AdzmartNavBtn>ooh</AdzmartNavBtn>
                <AdzmartNavBtn>radios</AdzmartNavBtn>
                <AdzmartNavBtn>cinemas</AdzmartNavBtn>
                <AdzmartNavBtn>online</AdzmartNavBtn>
                <AdzmartNavBtn>login</AdzmartNavBtn>
                <AdzmartMediumBtn>Sign up</AdzmartMediumBtn>
              </NavLinkCont>
            </NavItemsCont>
          </Innercontainer>
        </OutterContainer>
      </AdzmartNavCont>
    </>
  );
}

export default AdzmartNavigation;
