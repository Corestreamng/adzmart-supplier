import React from "react";
import {
  OutterContainer,
  Innercontainer,
  AdzmartBtn,
  flexCenter,
} from "../../adzmartStyles/commonCompStyles";
import {
  AuthContainer,
  loginBox,
  loginStackBox,
  LoginImage,
  textFieldBox,
  loginHeader,
  Authquestion,
  AuthAction,
  loginbottomTextCont,
} from "../../adzmartStyles/authenticationStyles";

import {Box, Stack, Typography, TextField} from "@mui/material";

function SignUpPage() {
  return (
    <OutterContainer sx={{backgroundColor: "#C8E5E3", minHeight: "100vh"}}>
      <Innercontainer sx={{height: "100%", paddingTop: 3}}>
        <Box sx={loginBox}>
          <Box sx={loginStackBox}>
            <AuthContainer>
              <Typography sx={loginHeader} variant="subtitle1">
                Sign up
              </Typography>

              <TextField
                sx={textFieldBox}
                label="Name"
                variant="filled"
                size="small"
                fullWidth
              />

              <TextField
                sx={textFieldBox}
                label="Email"
                variant="filled"
                size="small"
                fullWidth
              />

              <TextField
                sx={textFieldBox}
                label="Password"
                variant="filled"
                size="small"
                fullWidth
              />

              <TextField
                sx={textFieldBox}
                label="Confirm Password"
                variant="filled"
                size="small"
                fullWidth
              />

              <Stack sx={loginbottomTextCont}>
                <Authquestion>Already have an account?</Authquestion>
                <AuthAction to="/login">Log in</AuthAction>
              </Stack>
              <Box sx={{...flexCenter, marginTop: "2rem"}}>
                <AdzmartBtn>Sign up</AdzmartBtn>
              </Box>
            </AuthContainer>

            <LoginImage src="/images/signupimg.png" signup={true} />
          </Box>
        </Box>
      </Innercontainer>
    </OutterContainer>
  );
}

export default SignUpPage;
