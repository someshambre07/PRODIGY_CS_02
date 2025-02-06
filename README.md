# Pixel Manipulation Image Encryption

## Introduction
The **Pixel Manipulation Image Encryption** program is a Python-based encryption tool that secures images by modifying pixel values. This method ensures that images are unreadable without decryption, adding a layer of security for sensitive visual data.

## Features
- Encrypts images using pixel manipulation techniques.
- Decrypts images to restore the original content.
- Supports multiple image formats (JPEG, PNG, BMP, etc.).
- Uses a key-based encryption method to enhance security.

## How It Works
This program modifies the pixel values of an image based on an encryption key. The decryption process reverses the pixel modifications to restore the original image.

## Installation
To use this program, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Additionally, install the required dependencies:
```sh
pip install numpy opencv-python
```

## Usage
1. Clone or download this repository.
2. Navigate to the directory containing `Pixel_Manipulation_Image_Encryption.py`.
3. Run the script using the following command:
   ```sh
   python Pixel_Manipulation_Image_Encryption.py
   ```
4. Follow the prompts to select encryption or decryption.
5. Provide the image file and encryption key.
6. View the encrypted or decrypted image.

## Example
**Encryption:**
```
Enter 'E' for encryption or 'D' for decryption: E
Enter the image file path: input_image.png
Enter encryption key: 1234
```
**Output:**
```
Encrypted image saved as encrypted_image.png
```

