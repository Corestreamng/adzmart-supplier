import styled from "styled-components";
import {InputBase, Box, Stack} from "@mui/material";

export const HeroImage = styled.img`
  position: absolute;
  top: 4rem;
  right: -7rem;
  width: 42%;
`;

export const HeroTextCont = styled.div`
  padding-top: 6rem;
`;

export const InputContainer = styled(InputBase)`
  padding: 0.4rem 1.5rem;
  font-size: 0.2rem;
  border: 1px solid #005cc3;
  border-radius: 0.2rem;
`;

//service section styles

export const SearchInput = styled(InputBase)`
  padding: 0.8rem 4rem;
  width: 100%;
`;

export const SearchInputBox = styled(Box)`
  position: relative;
  background-color: white;
  border-radius: 0.2rem;
  width: 60%;
  box-shadow: 0px 1px 2px 1px lightgrey;
`;

export const SearchInputWrap = styled(Stack)`
  align-items: center;
  justify-content: center;
  gap: 1rem;
`;

export const ServiceItemCont = styled(Stack)`
  margin-top: 6rem;
  align-items: center;
  justify-content: center;
  gap: 2rem;
`;

//feature section styles
export const Adz_fs_TitleWrapper = styled(Stack)`
  display: flex;
  flex-direction: row !important;
  margin-top: 2rem;
  align-items: flex-start;
  justify-content: space-between;
  gap: 3rem;
`;

export const Adz_fs_TitleBox = styled(Box)`
  width: 40%;
`;

export const Adz_fs_flexcont = {
  gap: "4rem",
  margin: "2rem 0",
};

//more service section styles
export const AdzSsFlexcont = {
  flexDirection: "row",
  alignItems: "center",
  justifyContent: "space-between",
  marginTop: "4rem",
};

export const AdzSsLeftBox = styled(Box)`
  width: 30%;
  height: 60vh;
  position: relative;
`;

export const AdzSsDesignElement1 = styled(Box)`
  width: 80%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 1rem;
  border: 2px solid rgba(122, 122, 122, 0.22);
  border-radius: 15px;
`;

export const AdzSsDesignElement2 = styled(Box)`
  width: 80%;
  height: 90%;
  position: absolute;
  top: 1rem;
  border: 2px solid #005cc3;
  border-radius: 15px;
  z-index: 2;
`;

export const AdzSsRightBox = styled(Box)`
  width: 50%;
`;

export const AdzSsImg = styled.img`
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 3;
`;

export const AdzSsHeaderMargin = {
  marginBottom: "2rem",
};

export const AdzSsTextMargin = {
  marginBottom: "1.5rem",
};

export const AdzSsMoreOptionsBox = {
  backgroundColor: "white",
  paddingBottom: "4rem",
};

export const AdzSsHeader2Margin = {
  paddingTop: "4rem",
  marginBottom: "3rem",
};

export const AdzSsMoreOptionsFlex = {
  flexDirection: "row",
  gap: "4rem",
};

export const AdzSsOptionsImg = styled.img`
  width: 8rem;
  margin: 1rem 0 0 0.5rem;
`;

export const AdzSsOptions2Flex = {
  margin: "2rem 0",
  flexDirection: "row",
  justifyContent: "space-between",
};

export const AdzSsOptions2LargeBox = {
  width: "60%",
};

export const AdzSsOptions2SmallBox = {
  width: "30%",
};

export const AdzSsOptionsButtonCenter = {
  flexDirection: "row",
  justifyContent: "center",
  margin: "3rem 0",
};

//marketplace section styles
export const AdzMpBoxFlex = {
  flexDirection: "row",
  justifyContent: "flex-end",
  marginTop: "4rem",
};

export const AdzMpContentBox = {
  width: "50%",
};

export const AdzMpButtonMargin = {
  marginTop: "3rem",
};
