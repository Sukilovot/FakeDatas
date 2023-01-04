import PySimpleGUI as sg
import webbrowser

def error(error_text, code):
    layout = [
        [sg.Text("IP Search")],
        [sg.Text(f"Erro {code}: {error_text}")],
        [sg.Button("Obter suporte (via Discord)", key="get_support_discord"), sg.Button("Sair")]
    ]

    win = sg.Window("Fake Datas", layout, icon="favicon.ico")

    while True:
        event, values = win.read()

        if event == "get_support_discord":
            webbrowser.open("https://discord.gg/7tnFYtfj")

        if event == "Sair":
            break

    win.close()