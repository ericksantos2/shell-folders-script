from criaPastas import verificaDir
import os


def app():
    if verificaDir('backups') is False:
      os.mkdir('backups')
    os.chdir('backups')
    os.system('reg export \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders\" ShellFolderBak.reg')
    os.system('reg export \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders\" UserShellFolderBak.reg')
    os.chdir('..')