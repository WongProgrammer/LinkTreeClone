import React from 'react';
import { Avatar, Box, Container } from '@chakra-ui/react'

function Header() {
  return (
  <Container maxW='xl' centerContent>
      <Avatar name='default avatar' size='2xl' src='https://st3.depositphotos.com/1767687/16607/v/600/depositphotos_166074422-stock-illustration-default-avatar-profile-icon-grey.jpg'/>
  <Box padding='4' maxW='3xl'>
    @Header
  </Box>
</Container>
);
}

export default Header;
