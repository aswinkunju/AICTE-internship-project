# encryption.py
import cv2

def encrypt_message(img, msg):
    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0

    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    return img

def save_encrypted_image(img, filename):
    cv2.imwrite(filename, img)
