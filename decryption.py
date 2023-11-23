# decryption.py
import cv2

def decrypt_message(img, password,len):
    c = {i: chr(i) for i in range(255)}
    n, m, z = 0, 0, 0
    message = ""

    for _ in range(len):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    return message
