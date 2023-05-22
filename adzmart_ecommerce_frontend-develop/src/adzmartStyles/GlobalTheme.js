import {createTheme} from "@mui/material/styles";

const theme = createTheme({
  palette: {
    text: {
      main: "#7A7A7A",
    },
    background: {
      main: "#87BDFA",
    },
    backgroundAlt: {
      main: "#C8E5E3",
    },
    primary: {
      main: "#005CC3",
    },
  },
  typography: {
    fontFamily: "Inter,san-serif",
    h1: {
      fontSize: "3.5rem",
      fontWeight: 600,
      color: "#005CC3",
      // "@media (max-width:400px)": {
      //   fontSize: "1.2rem",
      // },
    },
    subtitle1: {
      fontSize: "1.5rem",
      fontWeight: 600,
      color: "#005CC3",
      lineHeight: "2.2rem",
      // "@media (max-width:400px)": {
      //   fontSize: ".9rem",
      // },
    },

    subtitle2: {
      fontSize: "1.5rem",
      fontWeight: 300,
      color: "#005CC3",
    },

    h3: {
      fontSize: "1rem",
      fontWeight: 700,
      color: "white",
    },

    h4: {
      fontSize: "1.1rem",
      fontWeight: 400,
      color: "#005CC3",
    },

    h5: {
      fontSize: "1.2rem",
      fontWeight: 600,
      color: "#005CC3",
    },

    body1: {
      fontSize: "0.8rem",
      fontWeight: 400,
      color: "#7A7A7A",
      // "@media (max-width:400px)": {
      //   fontSize: ".65rem",
      // },
    },

    body2: {
      fontSize: "1.2rem",
      fontWeight: 400,
      color: "#7A7A7A",
      // "@media (max-width:400px)": {
      //   fontSize: ".65rem",
      // },
    },

    button: {
      textTransform: "none",
    },
  },
});

export const globalTheme = {
  body: {
    backgroundColor: "rgba(0,92,195,0.2)",
    fontFamily: "Inter,san-serif",
    color: "#7A7A7A",
  },
};

export default theme;
