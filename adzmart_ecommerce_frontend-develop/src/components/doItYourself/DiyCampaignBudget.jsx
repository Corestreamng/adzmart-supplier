import {Typography} from "@mui/material";
import React from "react";

import {
  DiyCampaignBudgetWrapper,
  DiyCampaignBudgetInputCont,
  DiyCampaignBudgetInput,
  DiyCampaignBudgetIcon,
} from "./doItYourselfStyles";

function DiyCampaignBudget({show}) {
  return (
    <>
      <DiyCampaignBudgetWrapper show={show === 4 ? true : false}>
        <Typography variant="h5" sx={{margin: "2rem 0 0.5rem 0"}}>
          Campaign Budget{" "}
        </Typography>
        <Typography variant="body1">
          You are in control. Enter your budget for this campaign{" "}
        </Typography>

        <DiyCampaignBudgetInputCont size="60%">
          <DiyCampaignBudgetInput
            type={"number"}
            placeholder="Enter your budget"
          />
          <DiyCampaignBudgetIcon>&#8358;</DiyCampaignBudgetIcon>
        </DiyCampaignBudgetInputCont>
      </DiyCampaignBudgetWrapper>
    </>
  );
}

export default DiyCampaignBudget;
