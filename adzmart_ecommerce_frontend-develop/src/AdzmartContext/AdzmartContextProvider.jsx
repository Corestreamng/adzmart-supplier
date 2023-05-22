import React from "react";

export const AdzmartContext = React.createContext();

function AdzmartContextProvider({children}) {
  return (
    <AdzmartContext.Provider value={{value: "adzmartcontext"}}>
      {children}
    </AdzmartContext.Provider>
  );
}

export default AdzmartContextProvider;
