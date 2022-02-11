import React, { useState } from 'react';
import { Container, VStack } from '@chakra-ui/react'
import Header from './Header';
import Footer from './Footer';
import { SocialIcon } from 'react-social-icons';
function HomePage() {
    const [links, setLinks] = useState(['https://github.com/tinha1207', 'https://www.linkedin.com/in/huy-francis-nguyen-620b7a15a/', 'Link3']);
    return (
        <>
         <Header />
         <VStack bg="brand.900">
            {links.map(link => {
                return(
                <Container centerContent bg="brand.100">
                    <SocialIcon url={link}/> 
                </Container>
                );
            })}
            
        </VStack>
         <Footer/>
        </>
        
    );
}

export default HomePage;
