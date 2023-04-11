# shell-folders-script
Um script para mudar o local das pastas como downloads para outro lugar, util para quem tem windows em um disco e arquivos em outro.

Como usar: Coloque os arquivos no "Diretório Pai" de onde ficará a pasta do seu usuário, exemplo: Minha pasta ficará em D:\Erick, então tenho que colocar os arquivos em D:\
Ao terminar, é recomendado salvar a pasta backup e o resto dos arquivos podem ser excluidos normalmente.

* Para usar é necessário o python 3.

* Aviso: Se houver acento em alguma pasta, por exemplo a Área de Trabalho, é necessário que os acentos sejam trocados manualmente, para isso, abra o regedit, vá até ```Computador\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders``` e troque os acentos que devem estar incorretos.
