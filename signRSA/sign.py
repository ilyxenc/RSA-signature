from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import os

# подпись файла или сообщения с помощью ЭЦП
def sign(fileName, signPairPath = "./files/pair/", keyPath = "./files/keys/", file = True, message = ""):
    # считывание файла или сообщения
    if file == True:
        with open(fileName, mode='rb') as file: # b is important -> binary
            content = file.read()
    else:
        content = message

    key = RSA.import_key(open(keyPath + "private.key").read()) # импорт личного ключа
    h = SHA256.new(content) # создание хэша на основе предоставленного файла или сообщения

    # создание подписи на основе алгоритма RSA
    signer = pkcs1_15.new(key) 
    signature = signer.sign(h)

    # создание папки для выходного файла, если та отсутствует
    os.makedirs(os.path.dirname(signPairPath), exist_ok=True)

    fileOut = open(signPairPath + "signature.pem", "wb")
    fileOut.write(signature)
    fileOut.close()

    fileOut = open(signPairPath + fileName, "wb")
    fileOut.write(content)
    fileOut.close()