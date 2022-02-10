import { React } from 'react';
import { Box, Button, Input, Modal, ModalBody, ModalCloseButton, ModalContent, ModalHeader, ModalOverlay, Text, useDisclosure } from '@chakra-ui/react'
import { LinkIcon } from '@chakra-ui/icons'
import { useState } from 'react';
function Header() {
    const { isOpen, onOpen, onClose } = useDisclosure()
    const [link, setLink] = useState('');
    const onFocusHandler = () => {
        
        navigator.clipboard.writeText(link);
    }
    return (
        <>
            <Box>
                <Button onClick={onOpen}>
                    <LinkIcon onClick={() =>{setLink('link is copied')}}/>
                </Button>
            </Box>
            <Modal isCentered={true} isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <ModalContent>
                    <ModalHeader>Linktree Clone</ModalHeader>

                    <ModalCloseButton />
                    <ModalBody>
                        <Text>Made by: Francis Nguyen and Tin Ha</Text>
                        <Input
                            placeholder={link}
                            size='sm'
                            isReadOnly={true}
                            onFocus={onFocusHandler}
                        />
                    </ModalBody>
                </ModalContent>
            </Modal>

        </>

    );
}

export default Header;
