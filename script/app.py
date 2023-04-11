import os
import criaPastas
import criaRegUserShell
from fn import limpaTerminal
import criaBackup


def app():
    criaBackup.app()
    limpaTerminal()
    print('! - Os backups foram salvos na pasta backup')
    print('! - Para mudar o nome das pastas use um editor de texto e, dentro da pasta script, modifique o arquivo pathList.py\n')
    nome = input('Qual o nome da pasta do seu usuário?\n')
    limpaTerminal()
    path = input('Como ficará a pasta como destino? Ex.: D:\\Erick\n')
    limpaTerminal()
    criaPastas.app(nome)
    os.chdir('script')
    criaRegUserShell.app(path)
    limpaTerminal()
    input('O arquivo regedit foi gerado na pasta script.\nPressione enter para terminar.')
    limpaTerminal()


app()
