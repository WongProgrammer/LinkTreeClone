import React, { useState } from 'react';
import { Container, VStack } from '@chakra-ui/react'
import Header from './Header';
import Footer from './Footer';
//https://www.npmjs.com/package/react-social-icons
//https://jaketrent.github.io/react-social-icons/
function HomePage() {
    const [links, setLinks] = useState(['Link1', 'Link2', 'Link3']);
    return (
        <VStack bg="brand.900">
            <Header />
            {links.map(link => {
                return(<Container centerContent bg="brand.100">{link}</Container>);
            })}
            <Footer/>
        </VStack>
    );
}

export default HomePage;
