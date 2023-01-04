import PySimpleGUI as sg
from main import main
from error import error

login = {
    "login": ["sukilovot", "org.suru", "org.suru.users"],
    "password": ["sukilovot7777!", "org.suru.sukilovot", "org.suru.wbeatw", "org.suru.px",
                 "org.suru.another", "org.suru.dstdi", "org.suru.next", "org.suru.dunk"]
}

sg.change_look_and_feel("Black")

layout = [
    [sg.Text("Fake Datas")],
    [sg.Text("Login")],
    [sg.InputText("{}".format(str(open("saved_login.fkd", "r").read())))],
    [sg.Text("Senha")],
    [sg.InputText(password_char="*")],
    [sg.Text("")], # /n in other words
    [sg.Check("Salvar login?")],
    [sg.Button("Logar"), sg.Button("Sair")]
]

win = sg.Window("FakeDatas", layout, icon="favicon.ico")

while True:
    event, values = win.read()

    if event == "Logar":
        if str(values[0]) in login["login"] and str(values[1]) in login["password"]:
            main()
        else:
            error("Login ou senha não são validas", 0)

    if values[2] == True:
        open("saved_login.fkd", "w").write(str(values[0]))
    elif values[2] == False:
        open("saved_login.fkd", "w").write("")

    if event == "Sair":
        break

win.close()