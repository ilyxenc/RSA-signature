from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# проверка файла и подписи
def verify(fileName, signName = "signature.pem", signPairPath = "./files/pair/", 
    keyPath = "./files/keys/", keyName = "public.key", file = True, message = ""):
    # считывание файла или сообщения
    if file == True:
        with open(signPairPath + fileName, mode='rb') as file: # b is important -> binary
            content = file.read()
    else:
        content = message

    key = RSA.import_key(open(keyPath + keyName).read()) # считывание открытого ключа


    # считывание ЭЦП в качестве бинарного файла
    with open(signPairPath + signName, mode='rb') as file:
            signature = file.read()

    h = SHA256.new(content) # создание хэша на основе предоставленного файла или сообщения

    # проверка подписи, созданной на базе алгоритма RSA
    try:
        pkcs1_15.new(key).verify(h, signature)
        return(True)
    except (ValueError, TypeError):
        return(False)