import React from "react";
import ReactDOM from "react-dom/client";
import {ThemeProvider} from "@mui/material/styles";
import theme, {globalTheme} from "./adzmartStyles/GlobalTheme";
import AdzmartApp from "./AdzmartApp";
import reportWebVitals from "./reportWebVitals";
import {GlobalStyles} from "@mui/material";
import AdzmartContextProvider from "./AdzmartContext/AdzmartContextProvider";
import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <AdzmartContextProvider>
    <ThemeProvider theme={theme}>
      <GlobalStyles styles={{...globalTheme}} />
      <AdzmartApp />
    </ThemeProvider>
  </AdzmartContextProvider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
