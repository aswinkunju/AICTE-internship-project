# main.py
import cv2
import os
from encryption import encrypt_message, save_encrypted_image
from decryption import decrypt_message

def main():
    img = cv2.imread("download.jpeg")

    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    img = encrypt_message(img.copy(), msg)

    encrypted_filename = "encryptedImage.jpg"
    save_encrypted_image(img, encrypted_filename)
    os.startfile(encrypted_filename)

    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        decrypted_message = decrypt_message(img.copy(), password,len(msg))
        print("Decrypted message =", decrypted_message)
    else:
        print("You are not Authenticated")

if __name__ == "__main__":
    main()
