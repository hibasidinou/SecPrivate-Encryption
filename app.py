from flask import Flask, request, render_template
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes # type: ignore
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC # type: ignore
from cryptography.hazmat.primitives import hashes # type: ignore
from cryptography.hazmat.primitives.asymmetric import rsa, padding # type: ignore
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1 # type: ignore
from cryptography.hazmat.primitives.serialization import load_pem_private_key, Encoding, PrivateFormat, PublicFormat, NoEncryption # type: ignore
from cryptography.hazmat.primitives.serialization import load_pem_public_key # type: ignore
import os
import base64

app = Flask(__name__)

# Générer les clés RSA une seule fois
PRIVATE_KEY = rsa.generate_private_key(public_exponent=65537, key_size=2048)
PUBLIC_KEY = PRIVATE_KEY.public_key()

# Générer une clé AES (random pour l'exemple)
AES_KEY = os.urandom(32)  # Clé AES de 256 bits


def encrypt_aes(data: str, key: bytes) -> str:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode()) + encryptor.finalize()
    return base64.b64encode(iv + ciphertext).decode()


def decrypt_aes(data: str, key: bytes) -> str:
    raw_data = base64.b64decode(data)
    iv, ciphertext = raw_data[:16], raw_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    return (decryptor.update(ciphertext) + decryptor.finalize()).decode()


def encrypt_rsa(data: str, public_key) -> str:
    ciphertext = public_key.encrypt(
        data.encode(),
        OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(ciphertext).decode()


def decrypt_rsa(data: str, private_key) -> str:
    ciphertext = base64.b64decode(data)
    plaintext = private_key.decrypt(
        ciphertext,
        OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        action = request.form.get("action")
        message = request.form.get("message")
        crypto_type = request.form.get("crypto_type")

        if not message:
            result = "Please enter a message."
            return render_template("index.html", result=result)

        try:
            if crypto_type == "AES":
                if action == "encrypt":
                    result = encrypt_aes(message, AES_KEY)
                elif action == "decrypt":
                    result = decrypt_aes(message, AES_KEY)
                else:
                    result = "Invalid action."

            elif crypto_type == "RSA":
                if action == "encrypt":
                    result = encrypt_rsa(message, PUBLIC_KEY)
                elif action == "decrypt":
                    result = decrypt_rsa(message, PRIVATE_KEY)
                else:
                    result = "Invalid action."

        except Exception as e:
            result = f"An error occurred: {e}"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
