import styled from "styled-components";
import theme from "../../adzmartStyles/GlobalTheme";

export const DiyFlexCont = styled.section`
  display: flex;
  width: 100%;
  flex-direction: row;
  align-items: flex-end;
  gap: 2rem;
`;
export const DiyActivityCont = styled.div`
  width: 70%;
  min-height: 27rem;
  /* border: 1px solid red; */
  position: relative;
`;

export const DiyImageCont = styled.div`
  width: 30%;
`;
export const DiyImage = styled.img`
  width: 100%;
  object-fit: contain;
`;
export const DiyButtonCont = styled.div`
  display: flex;
  padding: 0 1rem;
  /* border: 1px solid red; */
  margin-top: 4rem;
  margin-bottom: 0.5rem;
  width: 68%;
  flex-direction: row;
  justify-content: space-between;
`;
export const DiyBackButton = styled.button`
  display: inline-block;
  border: none;
  font-size: 0.8rem;
  font-weight: 400;
  padding: 1rem 1.5rem;
  border-radius: 0.2rem;
  color: white;
  cursor: pointer;
  box-shadow: ${theme.shadows[2]};
  background-color: #87bdfa;
  &:hover {
    background-color: #87bdfa;
    box-shadow: ${theme.shadows[4]};
  }
  &:active {
    transform: scale(1.02);
    transition: transform 0.2 ease;
  }
`;

export const DiyContinueButon = styled.button`
  display: inline-block;
  border: none;
  font-size: 0.8rem;
  font-weight: 400;
  padding: 1rem 1.5rem;
  border-radius: 0.2rem;
  color: white;
  cursor: pointer;
  box-shadow: ${theme.shadows[2]};
  background-color: ${theme.palette.primary.main};
  &:hover {
    background-color: ${theme.palette.primary.main};
    box-shadow: ${theme.shadows[4]};
  }
  &:active {
    transform: scale(1.02);
    transition: transform 0.2 ease;
  }
`;

// D-I-Y Select State Component styles
export const DiySelectStateCont = styled.div`
  margin-top: 2rem;
  width: 100%;
  height: 23rem;
  padding-top: 0.5rem;
  /* border: 1px solid green; */
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  background-image: url("/images/doityourself/diymap.png");
`;

export const DiySelectStateWrapper = styled.div`
  position: absolute;
  width: 100%;
  top: 0;
  left: 0;
  display: ${({show}) => (show === true ? "initial" : "none")};
  opacity: ${({show}) => (show === true ? 1 : 0)};
  transition: opacity 3s ease-out;
`;

export const AdzInputBox = styled.div`
  border: none;
  position: relative;
  background-color: white;
  border-radius: 0.2rem;
  margin-inline: auto;
  margin-top: 1rem;
  width: ${({size}) => (size ? size : "auto")};
  box-shadow: 0px 1px 2px 1px lightgrey;
`;

export const AdzSelectMultipleInput = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 1rem 1rem;
  border-radius: 0.2rem;
  /* border: 1px solid green; */
  color: #87bdfa;
  font-size: 0.8rem;
  cursor: pointer;
`;

export const AdzSelectedStatesCont = styled.div`
  width: 90%;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
  /* border: 1px solid green; */
  cursor: pointer;
  color: #87bdfa;
`;

export const AdzSelectedState = styled.div`
  padding: 0.2rem;
  background-color: #f4f9ff;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.3rem;
  border-radius: 0.2rem;
  box-shadow: 0px 1px 2px 1px lightgrey;
`;

export const AdzRemoveState = styled.span`
  padding: 0 0.2rem;
  height: 100%;
`;

export const AdzSelectOptionBox = styled.div`
  background-color: white;
  width: 100%;
  border-radius: 0.2rem;
  position: absolute;
  bottom: -15.5rem;
  height: 15rem;
  /* border: 1px solid red; */
  overflow-y: scroll;
  box-shadow: 0px 1px 2px 1px lightgrey;
  opacity: ${({showdd}) => (showdd === true ? 1 : 0)};
  transition: opacity 0.5s ease-in;

  &::-webkit-scrollbar {
    width: 5px;
    border-radius: 5px;
  }
  &::-webkit-scrollbar-track {
    background-color: #f1f1f1;
  }

  &::-webkit-scrollbar-thumb {
    border-radius: 5px;
    background-color: #87bdfa;
  }
`;
export const AdzSelectOption = styled.div`
  width: 100%;
  padding: 0.8rem 2rem;
  border-bottom: 1px solid #f4f9ff;
  font-size: 0.8rem;
  color: #7a7a7a;
  cursor: pointer;
  &:active {
    background-color: #f4f9ff;
  }
`;

// D-I-Y Select options Component styles

export const DiySelectOptionsCont = styled.div`
  margin-top: 2rem;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  display: ${({show}) => (show === true ? "initial" : "none")};
  opacity: ${({show}) => (show === true ? 1 : 0)};
  transition: opacity 3s ease-out;
  /* border: 1px solid black; */
`;

export const DiySelectOptionsText = styled.p`
  margin-top: 2rem;
  width: 100%;
`;

export const DiySelectOptionsImg = styled.img`
  width: 10rem;
  border-radius: 0.3rem;
  cursor: pointer;
  &:active {
    transform: scale(1.05);
    transition: scale 2s ease;
  }
`;

export const DiySelectOptionsFlex = styled.section`
  display: ${({showOption}) => (showOption === true ? "flex" : "none")};
  align-items: center;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
`;

// ${({showOption}) => (showOption === true ? "flex" : "none")};

export const DiySelectedOptionsFlexCont = styled.section`
  width: 100%;
  display: ${({showOption}) => (showOption === true ? "flex" : "none")};
  align-items: center;
  gap: 2rem;
  margin-top: 2rem;
  background-color: #eaeaea;
  border-radius: 0.3rem;
  /* display: none; */
`;

export const DiyTextSpan = styled.span`
  font-weight: bolder;
`;

export const DiySelectedOptionsItemCont = styled.section`
  display: flex;
  align-items: center;
  gap: 2rem;
  background-color: #f4f9ff;
  padding: 2rem 3rem 2rem 2rem;
`;
export const Pin = styled.div`
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  background-color: #005cc3;
`;

export const DiySelectOptionModalWrapper = styled.section`
  position: fixed;
  width: 100vw;
  height: 100vh;
  top: 0;
  left: 0;
  display: ${({showM}) => (showM ? "grid" : "none")};
  place-items: center;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 100;
`;

export const DiySelectOptionModalCont = styled.section`
  width: 50%;
  height: auto;
  padding: 1rem;
  background-color: white;
  border-radius: 0.3rem;
  box-shadow: 0px 1px 2px 1px lightgrey;
`;

export const DiySelectOptionModalItemsCont = styled.section`
  width: 100%;
  height: 20rem;
  /* border: 1px solid blue; */
  display: flex;
  align-items: center;
  gap: 1.2rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 1rem;
  padding: 0 0 0 0.5rem;
  overflow-y: scroll;
  &::-webkit-scrollbar {
    width: 5px;
    border-radius: 5px;
  }
  &::-webkit-scrollbar-track {
    background-color: #f1f1f1;
  }

  &::-webkit-scrollbar-thumb {
    border-radius: 5px;
    background-color: #87bdfa;
  }
`;

export const DiySelectOptionModalItem = styled.div`
  display: flex;
  align-items: center;
  /* padding: 0.8rem 1rem; */
  gap: 1rem;
  border-radius: 0.3rem;
  background-color: #f4f9ff;
  box-shadow: 0px 1px 2px 1px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  position: relative;
`;

export const DiySelectOptionModalCloseBtn = styled.div`
  display: flex;
  border: none;
  font-size: 0.8rem;
  font-weight: 400;
  padding: 1rem 1.5rem;
  border-radius: 0.2rem;
  gap: 1rem;
  color: white;
  cursor: pointer;
  box-shadow: ${theme.shadows[2]};
  background-color: #87bdfa;
  &:hover {
    background-color: #87bdfa;
    box-shadow: ${theme.shadows[4]};
  }
  &:active {
    transform: scale(1.02);
    transition: transform 0.2 ease;
  }
`;
export const DiySelectOptionsRadioInputFlexCont = styled.div`
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-top: 2rem;
`;

export const DiySelectOptionsRadioInputCont = styled.div`
  display: flex;
  align-items: center;
  gap: 1rem;
`;

export const DiySelectOptionsRadioLabel = styled.label`
  font-size: 1.1rem;
  font-weight: 400;
  color: #005cc3;
  padding: 0.9rem 1.2rem 0.9rem 2.5rem;
  cursor: pointer;
  /* border: 1px solid red; */
`;

export const DiySelectOptionsRadioInput = styled.input`
  position: absolute;
  top: 50%;
  left: 0.8rem;
  transform: translateY(-50%);
`;

export const DiySelectOptionsBtnCont = styled.div`
  display: flex;
  align-items: center;
  justify-content: flex-end;
  margin: 2rem 0 0 0;
  padding-right: 1rem;
`;

// D-I-Y Select Preferred media Component styles

export const DiyPreferredOptionWrapper = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  display: ${({show}) => (show === true ? "initial" : "none")};
  opacity: ${({show}) => (show === true ? 1 : 0)};
  width: 100%;
  transition: opacity 3s ease-out;
`;

export const DiyPreferredOptionCont = styled(DiySelectOptionModalItemsCont)`
  height: auto;
  justify-content: flex-start;
  overflow-y: auto;
  padding: 1rem 0.5rem;
`;

export const DiyPreferredOptionItem = styled(DiySelectOptionModalItem)`
  /* padding: 1.5rem 3rem;
  gap: 2rem; */
`;

export const DiyPreferredOptionRadioLabel = styled(DiySelectOptionsRadioLabel)`
  padding: 1.5rem 3rem;
`;

export const DiyPreferredOptionRadioInput = styled(DiySelectOptionsRadioInput)`
  left: 1rem;
`;

// D-I-Y input budget for campaign Component styles

export const DiyCampaignBudgetWrapper = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  display: ${({show}) => (show === true ? "initial" : "none")};
  opacity: ${({show}) => (show === true ? 1 : 0)};
  width: 100%;
  transition: opacity 3s ease-out;
`;

export const DiyCampaignBudgetInputCont = styled(AdzInputBox)`
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  margin: 1.5rem 0;
`;

export const DiyCampaignBudgetInput = styled.input`
  border: none;
  outline: none;
  width: 80%;
  font-size: 1.1rem;
  color: #87bdfa;
`;

export const DiyCampaignBudgetIcon = styled.span`
  padding: 0.5rem;
  font-size: 2rem;
  color: #87bdfa;
`;

// D-I-Y provide media by upload Component styles

export const DiyUploadMediaWrapper = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  display: ${({show}) => (show === true ? "initial" : "none")};
  opacity: ${({show}) => (show === true ? 1 : 0)};
  width: 100%;
  transition: opacity 3s ease-out;
`;

export const DiyUploadMediaDateCont = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  /* border: 1px solid black; */
  width: ${({size}) => (size ? size : "auto")};
  margin: 3rem 0 1rem 0;
`;

export const DiyUploadMediaDateitem = styled(AdzInputBox)`
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: ${({size}) => (size ? size : "auto")};
  padding: 0.5rem 1.2rem;
  margin: 0;
`;

export const DiyUploadMediaIcon = styled(DiyCampaignBudgetIcon)`
  color: #87bdfa;
`;

export const DiyUploadMediaInput = styled(DiyCampaignBudgetInput)``;

export const DiyUploadMediaShowItemCont = styled.div`
  height: 5rem;
  /* border: 1px solid red; */
`;

export const DiyUploadMediaImg = styled(DiySelectOptionsImg)``;

export const DiyUploadMediaImgCont = styled(DiySelectOptionsFlex)`
  margin-top: 1rem;
  justify-content: space-between;
  display: flex;
`;
