import styled from "styled-components";

export const NavItemsCont = styled.nav`
  height: 4rem;
  display: flex;
  align-items: center;
`;

export const NavLinkCont = styled.nav`
  height: 100%;
  display: flex;
  align-items: center;
  margin-left: auto;
`;

export const AdzmartNavCont = styled.div`
  width: 100%;
  position: ${({show}) => (!show ? "sticky" : "absolute")};
  top: 0;
  left: 0;
  background-color: ${({show}) => (!show ? "white" : "transparent")};
  box-shadow: ${({show}) => (!show ? "0px 1px 2px 1px lightgrey" : "")};
  transition: all 0.2s ease-in;
  z-index: 10;
`;

export const AdzmartNavObserver = styled.div`
  width: 100%;
  height: 4rem;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 5;
`;

export const AdzmartBlueLogo = styled.img`
  width: 8rem;
`;
