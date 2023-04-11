from fn import (criaLista, criaArquivo)
from pathList import listaPathsShell
from file import File

file = File('Shell Folders.reg')


def shellFoldersApp(path):
    lista = criaLista(path, listaPathsShell, 'normal')
    criaArquivo(lista, file, 'semHex2',
                '[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders]')
