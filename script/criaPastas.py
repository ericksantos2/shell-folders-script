import os
import re
from pathList import (pathsPadrao, listaPaths)


def app(nomeInicial):
    nome = nomeInicial
    if verificaDir(nome) is False:
        os.mkdir(nome)
    os.chdir(nome)
    criaPastas()
    os.chdir('..')


def criaPastas():
    listaPathsTexto = []
    for item in listaPaths:
        texto = arrumaNomePath(item[1])
        if texto not in listaPathsTexto:
            listaPathsTexto.append(texto)
    for pasta in listaPathsTexto:
        if pasta == arrumaNomePath(pathsPadrao.cameraRoll) or pasta == arrumaNomePath(pathsPadrao.savedPictures):
            nome = pathsPadrao.pictures
            if verificaDir(nome) is False:
                os.mkdir(nome)
            os.chdir(nome)
            if verificaDir(pasta) is False:
                os.mkdir(pasta)
            os.chdir('..')
        else:
            if verificaDir(pasta) is False:
                os.mkdir(pasta)


def arrumaNomePath(string):
    if '\\' in string:
        regex = '\\\([\\w\\s]*)'
        return (re.findall(regex, string))[0]
    else:
        return string


def verificaDir(nome):
    listaDir = os.listdir()
    if nome in listaDir:
        return True
    else:
        return False
