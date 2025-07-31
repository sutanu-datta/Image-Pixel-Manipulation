from PIL import Image
import os

def encrypt_decrypt_image(path, key):
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.show()
    return img

def main():
    path = input("Enter the image file path: ").strip()
    if not os.path.isfile(path):
        print("Invalid file path.")
        return

    try:
        key = int(input("Enter the encryption/decryption key (integer): "))
    except ValueError:
        print("Key must be an integer.")
        return

    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower().strip()
    
    if choice == 'e':
        encrypted = encrypt_decrypt_image(path, key)
        if encrypted:
            encrypted.save("encrypted.png")
            print("Encrypted image saved as 'encrypted.png'")
    elif choice == 'd':
        decrypted = encrypt_decrypt_image(path, key)
        if decrypted:
            decrypted.save("decrypted.png")
            print("Decrypted image saved as 'decrypted.png'")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
