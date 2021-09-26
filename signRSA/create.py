from Crypto.PublicKey import RSA
import os

# создание ключей с заданием их дальнейшего расположения
def createKeys(path = "./files/keys/"):    
    # создание папки для ключей, если та отсутствует
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # генерирование и сохранение ключей шифрования с длиной 2048 бит (рекомендуемо)
    key = RSA.generate(2048)
    private_key = key.export_key() # экспорт личного ключа
    file_out = open(path + "private.key", "wb") 
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key() # экспорт открытого ключа
    file_out = open(path + "public.key", "wb")
    file_out.write(public_key)
    file_out.close()