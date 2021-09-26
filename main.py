from signRSA import create as cr
from signRSA import sign as sg
from signRSA import verify as vf

cr.createKeys() # создание ключей

sg.sign(fileName = "test.docx") # подпись документа

print(vf.verify(fileName = "test.docx")) # проверка подписи