import React from 'react';
import { Center, Flex, Text } from '@chakra-ui/react'
import { SocialIcon } from 'react-social-icons'

//this will link to our repo
function Footer() {
    return (
        <Flex>
            <Center>
                <SocialIcon style={{ height: 25, width: 25, marginRight: '1px' }} network="github" />
            </Center>
            <Center>
                <Text fontSize='2xl'>Linktree Clone</Text>
            </Center>
        </Flex>
    );
}

export default Footer;
