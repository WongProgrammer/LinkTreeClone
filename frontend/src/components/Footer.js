import React from 'react';
import { Avatar, Container, SimpleGrid, Text } from '@chakra-ui/react'
function Footer() {
    return (
        <Container maxW='xl' centerContent>
            <SimpleGrid columns={2} spacing={2}>
            <Avatar src='https://user-images.githubusercontent.com/12532733/90986349-ce9c2600-e547-11ea-9fd5-808801bb5a7d.png' />
            <Text>LinkTree Clone</Text>
            </SimpleGrid >
        </Container >
    );
}

export default Footer;
