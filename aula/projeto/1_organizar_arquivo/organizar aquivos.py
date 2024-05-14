import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title = 'Selecione a pasta')

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", "jpg"],
    "planilhas": ["xlsx"],
    "csv": [".csv"],
    "paython": [".py"],
    "pdf": [".pdf"],
    "xml": [".xml"]
}
for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais[pasta:]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho/{pasta}}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')


import os
from PyQt5.QtWidgets import QApplication, QFileDialog

def askdirectory(title='Selecione a pasta'):
    app = QApplication([])
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.Directory)
    dialog.setOption(QFileDialog.ShowDirsOnly, True)
    dialog.setWindowTitle(title)
    if dialog.exec_() == QFileDialog.Accepted:
        directory = dialog.selectedFiles()[0]
        return directory
    return None

caminho = askdirectory()

if caminho:
    lista_arquivos = os.listdir(caminho)

    locais = {
        "imagens": [".png", ".jpg"],
        "planilhas": [".xlsx"],
        "csv": [".csv"],
        "python": [".py"],
        "pdf": [".pdf"],
        "xml": [".xml"]
    }

    for arquivo in lista_arquivos:
        nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
        for pasta in locais:
            if extensao in locais[pasta]:
                pasta_caminho = os.path.join(caminho, pasta)
                if not os.path.exists(pasta_caminho):
                    os.mkdir(pasta_caminho)
                os.rename(os.path.join(caminho, arquivo), os.path.join(pasta_caminho, arquivo))
else:
    print("Nenhuma pasta selecionada.")
