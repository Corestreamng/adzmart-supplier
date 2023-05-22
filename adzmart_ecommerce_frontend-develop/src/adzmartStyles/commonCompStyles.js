import {styled} from "@mui/material/styles";
import {Button, Box, Stack} from "@mui/material";
import {Link} from "react-router-dom";

export const AdzmartSmallBtn = styled(Button)(({theme}) => ({
  display: "inline-block",
  fontSize: "0.8rem",
  fontWeight: 400,
  padding: "0.3rem 1rem",
  borderRadius: "0.2rem",
  color: "white",
  boxShadow: theme.shadows[2],
  backgroundColor: theme.palette.primary.main,
  "&:hover": {
    backgroundColor: theme.palette.primary.main,
    boxShadow: theme.shadows[4],
  },
}));

export const AdzmartMediumBtn = styled(Button)(({theme}) => ({
  display: "inline-block",
  fontSize: "0.8rem",
  fontWeight: 400,
  padding: "0.5rem 1.5rem",
  borderRadius: "0.2rem",
  color: "white",
  boxShadow: theme.shadows[2],
  backgroundColor: theme.palette.primary.main,
  "&:hover": {
    backgroundColor: theme.palette.primary.main,
    boxShadow: theme.shadows[4],
  },
}));

export const AdzmartLargeBtn = styled(Button)(({theme}) => ({
  display: "inline-block",
  fontSize: "1rem",
  fontWeight: 400,
  padding: "0.8rem 1.3rem",
  borderRadius: "0.2rem",
  color: "white",
  boxShadow: theme.shadows[2],
  backgroundColor: theme.palette.primary.main,
  "&:hover": {
    backgroundColor: theme.palette.primary.main,
    boxShadow: theme.shadows[4],
  },
}));

export const AdzmartLargeBtnWhite = styled("button")(({theme}) => ({
  display: "inline-block",
  fontSize: "1rem",
  fontWeight: 400,
  border: "none",
  cursor: "pointer",
  padding: "0.8rem 1.3rem",
  borderRadius: "0.2rem",
  color: theme.palette.primary.main,
  boxShadow: theme.shadows[2],
  backgroundColor: "white",
  "&:hover": {
    boxShadow: theme.shadows[4],
  },
}));

export const AdzmartNavBtn = styled("button")`
  border: none;
  font-size: 0.75rem;
  font-weight: 400;
  text-transform: uppercase;
  padding: 0.5rem 1rem;
  height: 100%;
  background-color: transparent;
  color: #7a7a7a;
  cursor: pointer;
  &:hover {
    color: #005cc3;
    text-decoration: underline;
  }
`;

export const AdzmartAltBtn = styled("button")`
  border: none;
  font-size: 0.85rem;
  font-weight: 400;
  padding: 0 1rem;
  background-color: transparent;
  color: ${({shade}) => (shade ? shade : "#005cc3")};
  cursor: pointer;
  &:hover {
    text-decoration: underline;
  }
`;

export const AdzmartItemWrap = styled(Box)`
  position: relative;
  padding: 1.5rem 1rem;
  background-color: white;
  border-radius: 0.4rem;
  width: ${({size}) => (size ? size : "auto")};
  box-shadow: 0px 1px 2px 1px lightgrey;
`;

export const OutterContainer = styled(Box)(({theme}) => ({
  width: "100%",
  position: "relative",
  overflow: "hidden",
}));

export const Innercontainer = styled("div")`
  position: relative;
  width: 85%;
  margin-inline: auto;
  @media screen and (max-width: 600px) {
    width: 95%;
  }
`;

export const SectionWrap = styled("main")`
  width: 100%;
  min-height: 100vh;
  background-repeat: no-repeat;
  background-position: center top;
  background-size: cover;
  background-image: url("/images/background1.png");
`;

export const SectionWrapPlain = styled("main")`
  width: 100%;
  min-height: 100vh;
  padding-top: 5rem;
  background-color: #f4f9ff;
`;

export const SectionWrapAlt = styled("section")`
  padding: 4rem 0rem;
  width: 100%;
  height: ${({size}) => (size ? size : "auto")};
  background-repeat: no-repeat;
  background-position: center top;
  background-size: cover;
  background-image: url("/images/backgroundalt.png");
`;

export const Adz_fs_ItemFlex = styled(Stack)`
  display: flex;
  flex-direction: row !important;
  align-items: flex-start;
  justify-content: space-between;
`;

export const Adz_fs_ItemBoxW = styled(Box)`
  width: ${({size}) => (size ? size : "40%")};
`;

export const Adz_fs_ItemImgBox = {
  position: "absolute",
  bottom: "0",
  right: "3rem",
};

export const Adz_fs_ItemImg = styled("img")`
  width: ${({size}) => (size ? size : "auto")};
`;

export const flexEnd = {
  display: "flex",
  flexDirection: "row",
  alignItems: "center",
  justifyContent: "flex-end",
};

export const flexCenter = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

export const commonFlex = {
  flexDirection: "row",
  gap: "5rem",
};

export const AdzLink = styled(Link)`
  color: inherit;
  text-decoration: none;
`;

export const AdzInput = styled("input")`
  padding: 0.8rem;
  width: 100%;
`;

export const AdzSearchInputFlexWrap = styled("div")`
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
`;

export const AdzIconBox = styled("div")`
  padding: 0.5rem;
`;

export const AdzFlexBetweenCont = styled("div")`
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

// lightblue=F4F9FF

// textblue=87BDFA
