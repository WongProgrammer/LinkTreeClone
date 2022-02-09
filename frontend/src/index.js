import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import {ChakraProvider, extendTheme } from '@chakra-ui/react'

const theme = extendTheme({
  colors: {
    brand: {
      100: "gray",
      // ...
      900: "lime",
    },
  },
})

ReactDOM.render(
  <ChakraProvider theme={theme}>
      <App />
    </ChakraProvider>,
  document.getElementById('root')
);
