import React, {useState} from "react";
import {
  DiySelectOptionsCont,
  DiySelectOptionsFlex,
  DiySelectOptionsImg,
  DiySelectOptionsRadioInputFlexCont,
  DiySelectOptionsRadioInputCont,
  DiySelectedOptionsFlexCont,
  DiySelectedOptionsItemCont,
  Pin,
  DiySelectOptionModalWrapper,
  DiySelectOptionModalCont,
  DiySelectOptionModalCloseBtn,
  DiySelectOptionModalItemsCont,
  DiySelectOptionModalItem,
  DiyTextSpan,
  DiyContinueButon,
  DiySelectOptionsBtnCont,
  DiySelectOptionsRadioLabel,
  DiySelectOptionsRadioInput,
} from "./doItYourselfStyles";
import {AdzFlexBetweenCont} from "../../adzmartStyles/commonCompStyles";
import {Typography} from "@mui/material";
import {modalItems} from "../../AdzmartUtils/diyUtils";

function DiyOptionsComponent({show}) {
  let [showModal, setShowModal] = useState(false);
  let [selectedOption, setSelectedOPtion] = useState("");
  let [selectedOptionItem, setSelectedOptionItem] = useState("");
  let [showSelectedItem, setShowSelectedItem] = useState(false);

  let showOptions = (option) => {
    setSelectedOPtion(option);
    setShowModal((showModal = true));
  };

  let selectedOPtionText = (option) => {
    if (option === "SEC") {
      return "Select your preferred socio-economic class";
    }
    if (option === "INT") {
      return "Select your preferred area of interest";
    }

    if (option === "LF") {
      return "Select your preferred audience slife style";
    }
  };

  let selectedOPtionImg = (option) => {
    if (option === "SEC") {
      return "/images/doityourself/diysocialeconomic.png";
    }
    if (option === "INT") {
      return "/images/doityourself/diyinterest.png";
    }

    if (option === "LF") {
      return "/images/doityourself/diylifestyle.png";
    }
  };

  let getSelectedOptionItem = (e) => {
    console.log(e.target.getAttribute("data-value"));
    setSelectedOptionItem(e.target.getAttribute("data-value"));
  };

  let showSelected = () => {
    if (selectedOptionItem === "") {
      setShowModal(!showModal);
      return;
    }
    setShowSelectedItem(true);
    setShowModal(!showModal);
  };

  return (
    <>
      {/* {console.log(selectedOption)}
      {console.log(selectedOPtionImg(selectedOption))}
      {console.log(selectedOptionItem)}
      {console.log(showSelectedItem)} */}
      {console.log(modalItems[selectedOption])}
      <DiySelectOptionsCont show={show === 2 ? true : false}>
        {showSelectedItem ? (
          <Typography variant="body1" sx={{width: "80%"}}>
            1. Your audience selection is made
          </Typography>
        ) : (
          <Typography variant="body1" sx={{width: "80%"}}>
            1. Choose an option from
            <DiyTextSpan>one</DiyTextSpan> of the three categories. This will
            help you target the right households without overly limiting your
            audience
          </Typography>
        )}

        <DiySelectedOptionsFlexCont showOption={showSelectedItem}>
          <DiySelectOptionsImg src={selectedOPtionImg(selectedOption)} />
          <DiySelectedOptionsItemCont>
            <Pin />
            <Typography variant="subtitle2">{selectedOptionItem}</Typography>
          </DiySelectedOptionsItemCont>
        </DiySelectedOptionsFlexCont>

        <DiySelectOptionsFlex showOption={!showSelectedItem ? true : false}>
          <DiySelectOptionsImg
            src="/images/doityourself/diysocialeconomic.png"
            onClick={() => showOptions("SEC")}
          />
          <Typography variant="body2">
            <span style={{fontWeight: "bolder"}}>or</span>
          </Typography>
          <DiySelectOptionsImg
            src="/images/doityourself/diyinterest.png"
            onClick={() => showOptions("INT")}
          />
          <Typography variant="body2">
            <span style={{fontWeight: "bolder"}}>or</span>
          </Typography>
          <DiySelectOptionsImg
            src="/images/doityourself/diylifestyle.png"
            onClick={() => showOptions("LF")}
          />
        </DiySelectOptionsFlex>

        <Typography variant="body1" sx={{marginTop: "2rem"}}>
          2. Specify the gender and age of the audience you want to target.
        </Typography>

        <DiySelectOptionsRadioInputFlexCont>
          <DiySelectOptionsRadioInputCont>
            <input type={"radio"} name="sex" />
            <Typography variant="body2">Male</Typography>
          </DiySelectOptionsRadioInputCont>
          <DiySelectOptionsRadioInputCont>
            <input type={"radio"} name="sex" />
            <Typography variant="body2">Female</Typography>
          </DiySelectOptionsRadioInputCont>
          <DiySelectOptionsRadioInputCont>
            <input type={"radio"} name="sex" />
            <Typography variant="body2">Both</Typography>
          </DiySelectOptionsRadioInputCont>
        </DiySelectOptionsRadioInputFlexCont>
      </DiySelectOptionsCont>
      {/* modal section start below */}
      <DiySelectOptionModalWrapper showM={showModal}>
        <DiySelectOptionModalCont>
          <AdzFlexBetweenCont>
            <Typography variant="body2">
              {selectedOPtionText(selectedOption)}
            </Typography>
            <DiySelectOptionModalCloseBtn
              onClick={() => setShowModal(!showModal)}
            >
              Close<span>X</span>
            </DiySelectOptionModalCloseBtn>
          </AdzFlexBetweenCont>

          <DiySelectOptionModalItemsCont>
            {selectedOption &&
              modalItems[selectedOption].map((item, index) => {
                return (
                  <DiySelectOptionModalItem key={index}>
                    <DiySelectOptionsRadioInput
                      type={"radio"}
                      id={item}
                      name={selectedOption}
                    />
                    <DiySelectOptionsRadioLabel
                      htmlFor={item}
                      data-value={item}
                      onClick={(e) => getSelectedOptionItem(e)}
                    >
                      {item}
                    </DiySelectOptionsRadioLabel>
                  </DiySelectOptionModalItem>
                );
              })}
          </DiySelectOptionModalItemsCont>

          <DiySelectOptionsBtnCont>
            <DiyContinueButon
              onClick={() => {
                showSelected();
              }}
            >
              Continue
            </DiyContinueButon>
          </DiySelectOptionsBtnCont>
        </DiySelectOptionModalCont>
      </DiySelectOptionModalWrapper>
    </>
  );
}

export default DiyOptionsComponent;
