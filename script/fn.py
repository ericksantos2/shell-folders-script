import re
import os
from pathList import listaPaths


class Item:
    def __init__(self, nome, lugar):
        self.nome = nome
        self.lugar = lugar


def criaLista(path, lista=listaPaths, type='hex'):
    listaClassePaths = []
    if type == 'hex':
        for item in lista:
            itemComClasse = Item(item[0], pathToHex(f'{path}{item[1]}'))
            listaClassePaths.append(itemComClasse)
    elif type == 'normal':
        for item in lista:
            novoLugar = f'{path}{item[1]}'.replace('\\', '\\\\')
            itemComClasse = Item(item[0], novoLugar)
            listaClassePaths.append(itemComClasse)
    return listaClassePaths


def pathToHex(str):
    strEncoded = transformaString(str)
    strHex = strEncoded.hex()
    regex = '([\w]{2})'
    match = re.findall(regex, strHex)
    returnString = (',00,'.join(match)) + ',00'
    return returnString


def transformaString(str):
    strB = str.encode('raw_unicode_escape')
    return strB


def criaArquivo(lista, arquivo, type='normal', path='[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders]'):
    messageA = 'Windows Registry Editor Version 5.00'
    messageB = path
    arquivo.clear()
    arquivo.write(f'{messageA}\n')
    arquivo.write(f'\n{messageB}\n')
    if type == 'normal':
        for item in lista:
            arquivo.write(f'"{item.nome}"=hex(2):{item.lugar}\n')
    elif type == 'semHex2':
        for item in lista:
            arquivo.write(f'"{item.nome}"="{item.lugar}"\n')


def limpaTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[0;37;41mEsse script deve ser executado no \'Diretório Pai\' da sua pasta de usuário.\n\033[0m')
