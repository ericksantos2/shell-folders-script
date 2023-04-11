class PathsPadrao:
    def __init__(self):
        # Change the folders name here
        self.pictures = 'Pictures'
        self.documents = 'Documentos'
        self.videos = 'Videos'
        self.downloads = 'Downloads'
        self.savedGames = 'Jogos Salvos'
        self.contacts = 'Contatos'
        self.cameraRoll = f'{self.pictures}\\Camera Roll'
        self.savedPictures = f'{self.pictures}\\Saved Pictures'
        self.links = 'Links'
        self.desktop = 'Área de Trabalho'
        self.favorites = 'Favoritos'
        self.music = 'Music'
        self.searches = 'Pesquisas'
        
# DONT CHANGE NOTHING BELOW

pathsPadrao = PathsPadrao();

listaPaths = [
    ['{0DDD015D-B06C-45D5-8C4C-F59713854639}', pathsPadrao.pictures],
    ['{24D89E24-2F19-4534-9DDE-6A6671FBB8FE}', pathsPadrao.documents],
    ['{339719B5-8C47-4894-94C2-D8F77ADD44A6}', pathsPadrao.pictures],
    ['{35286A68-3C57-41A1-BBB1-0EAE73D76C95}', pathsPadrao.videos],
    ['{374DE290-123F-4565-9164-39C4925E467B}', pathsPadrao.downloads],
    ['{4C5C32FF-BB9D-43B0-B5B4-2D72E54EAAA4}', pathsPadrao.savedGames],
    ['{56784854-C6CB-462B-8169-88E350ACB882}', pathsPadrao.contacts],
    ['{767E6811-49CB-4273-87C2-20F355E1085B}', pathsPadrao.cameraRoll],
    ['{7D1D3A04-DEBB-4115-95CF-2F29DA2920DA}', pathsPadrao.searches],
    ['{7D83EE9B-2244-4E70-B1F5-5393042AF1E4}', pathsPadrao.downloads],
    ['{A0C69A99-21C8-4671-8703-7934162FCF1D}', pathsPadrao.music],
    ['{AB5FB87B-7CE2-4F83-915D-550846C9537B}', pathsPadrao.cameraRoll],
    ['{B7BEDE81-DF94-4682-A7D8-57A52620B86F}', pathsPadrao.savedPictures],
    ['{BFB9D5E0-C6A9-404C-B2B2-AE6DB6AF4968}', pathsPadrao.links],
    ['{F42EE2D3-909F-4907-8871-4C22FC0BF756}', pathsPadrao.documents],
    ['Desktop', pathsPadrao.desktop],
    ['Favorites', pathsPadrao.favorites],
    ['My Music', pathsPadrao.music],
    ['My Pictures', pathsPadrao.pictures],
    ['My Video', pathsPadrao.videos],
    ['Personal', pathsPadrao.documents]
]

listaPathsShell = [
    ['{374DE290-123F-4565-9164-39C4925E467B}', pathsPadrao.downloads],
    ['{4C5C32FF-BB9D-43B0-B5B4-2D72E54EAAA4}', pathsPadrao.savedGames],
    ['{56784854-C6CB-462B-8169-88E350ACB882}', pathsPadrao.contacts],
    ['{7D1D3A04-DEBB-4115-95CF-2F29DA2920DA}', pathsPadrao.searches],
    ['{BFB9D5E0-C6A9-404C-B2B2-AE6DB6AF4968}', pathsPadrao.links],
    ['Desktop', pathsPadrao.desktop],
    ['Favorites', pathsPadrao.favorites],
    ['My Music', pathsPadrao.music],
    ['My Pictures', pathsPadrao.pictures],
    ['My Video', pathsPadrao.videos],
    ['Personal', pathsPadrao.documents],
]