# decryption.py
import cv2

def decrypt_message(img, password, msg_length):
    d = {i: chr(i) for i in range(255)}
    n, m, z = 0, 0, 0
    decrypted_message = ""

    for i in range(msg_length):
        decrypted_message += d[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    return decrypted_message
