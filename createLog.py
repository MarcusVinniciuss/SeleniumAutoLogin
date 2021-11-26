from automa import *
import os.path
import shutil
from datetime import date, datetime

agora = datetime.now()

url = getUrl

print(url)



if url == 'http://127.0.0.1:5500/logado.html':
    msg_sucesso= 'Robô logou no sistema!' 
    print('Sucesso')
    file_name = 'log.txt'
    arquivo = open(file_name, 'r+')
    arquivo = open(file_name, 'w+')
    arquivo.writelines(u'{}'.format('{}. ({})').format(msg_sucesso, agora))
    arquivo.close()

else:
    msg_erro= 'Robô não conseguiu logar sistemam, favor verificar novamente!' 
    print('Erro')
    file_name = 'log.txt'
    arquivo = open(file_name, 'r+')
    arquivo = open(file_name, 'w+')
    arquivo.writelines(u'{}'.format('{}. ({})').format(msg_erro, agora))
    arquivo.close()
