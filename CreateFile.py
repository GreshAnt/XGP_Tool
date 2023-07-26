from cryptography.fernet import Fernet
import base64
import hashlib
def generate_unique_encrypted_file(device_id):
    file_path = "device_id.bin"

    key = base64.urlsafe_b64encode(hashlib.sha256(device_id.encode()).digest())
    cipher_suite = Fernet(key)
    plaintext = device_id.encode()
    ciphertext = cipher_suite.encrypt(plaintext)
    with open(file_path, "wb") as file:
        file.write(ciphertext)
hwid = input('>hwid: ')
generate_unique_encrypted_file(hwid)
