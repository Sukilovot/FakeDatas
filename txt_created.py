import PySimpleGUI as sg

def response_txt_created(name_archive):
    layout = [
        [sg.Text("IP Search")],
        [sg.Text(f"Arquivo {name_archive} foi criado com sucesso")],
        [sg.Button("Sair")]
    ]

    win = sg.Window("IP Serach", layout, icon="favicon.ico")

    while True:
        event, values = win.read()

        if event == "Sair":
            break

    win.close()