# Steganography Project

## **Overview**
This project implements **Steganography**, allowing users to encrypt any text message inside an image and generate an output image. The same output image with the hidden message can then be uploaded to decrypt and retrieve the original message.

## **Technologies Used**
- **Python**: For backend logic and encryption/decryption.
- **Flask**: Web framework for handling the user interface and requests.
- **HTML/CSS**: For designing the front-end.
- **JavaScript**: For enhancing user interactions and client-side functionalities.

## **Features**
- **Encrypt Text**: Hide any text message inside an image file.
- **Decrypt Text**: Retrieve the hidden message by uploading the modified image.
- **User-Friendly Interface**: Simple and easy-to-use interface built using Flask, HTML, and CSS.
  
## **How It Works**
**1) Encrypting Text:**
- Upload an image.
- Enter the text message you want to encrypt.
- The tool will generate an output image that contains the hidden message.
- Download the output image.

**2) Decrypting Text:**
- Upload the output image with the hidden message.
- The tool will extract and display the original text.

## **Future Enhancements**
- Support for multiple image formats.
- Encryption of larger text messages.
- Enhanced security features for encryption.
