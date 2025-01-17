from PIL import Image
import random
import numpy as np

# Function to encrypt the image
def encrypt_image(image_path, output_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    
    key = random.randint(1, 255)
    
    encrypted_pixels = pixels ^ key
    
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_path)
    
    return key

# Function to decrypt the image
def decrypt_image(encrypted_image_path, output_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_pixels = np.array(encrypted_image)
    
    decrypted_pixels = encrypted_pixels ^ key
    
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_path)


if __name__ == "__main__":
    # please input the proper image paths here
    image_path = "input_image.jpg" 
    encrypted_image_path = "encrypted_image.jpg" 
    decrypted_image_path = "decrypted_image.jpg" 
    
    encryption_key = encrypt_image(image_path, encrypted_image_path)
    print(f"Encryption key: {encryption_key}")
    
    decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)
    print("Decryption completed.")
