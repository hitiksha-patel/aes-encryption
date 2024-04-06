
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from rest_framework.renderers import BaseRenderer
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Read the secret key and IV from environment variables
AES_SECRET_KEY = os.getenv('AES_SECRET_KEY').encode('utf-8')
AES_IV = os.getenv('AES_IV').encode('utf-8')

# Ensure the IV length is exactly 16 bytes
AES_IV = AES_IV[:16]

class CustomRenderer(BaseRenderer):
    media_type = 'application/octet-stream'
    format = 'aes'

    def render(self, data, media_type=None, renderer_context=None):
        plaintext = json.dumps(data)
        padded_plaintext = pad(plaintext.encode(), 16)
        cipher = AES.new(AES_SECRET_KEY, AES.MODE_CBC, AES_IV)
        ciphertext = cipher.encrypt(padded_plaintext)
        ciphertext_b64 = base64.b64encode(ciphertext).decode()
        response = {'ciphertext': ciphertext_b64}
        return json.dumps(response)
