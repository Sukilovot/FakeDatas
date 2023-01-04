import PySimpleGUI as sg
from error import error
from response import response
from class_json import data_json
from txt_created import response_txt_created

def main():
    layout = [
        [sg.Text("Fake Datas")],
        [sg.Text("Digite a lingua e sigla o país (pt-BR): "), sg.InputText()],
        [sg.Button("Gerar"), sg.Button("Gerar em .txt", key="txt"), sg.Button("Sair")]
    ]

    win = sg.Window("Fake Datas", layout, icon="favicon.ico")

    while True:
        event, values = win.read()

        if event == "Gerar":
            country = str(values[0]).strip()
            country.replace("_", "-")

            try:
                faker_data = data_json(country).return_json()

                response(faker_data)
            except:
                error("País não encontrado ou arquivo 'response.py' foi excluido", 1)
                continue

        if event == "txt":
            try:
                country = str(values[0]).strip()
                country.replace("_", "-")
                faker_data = data_json(country).return_json()
                name_archive = f"{faker_data['name']}.txt"
                open(f"datas/{name_archive}", "w").write(f"Fake Datas by Sukilovot\n"
                                                             f"ORG.SURU\n\n"
                                                             f"===Informações basicas===\n"
                                                             f"Nome: {faker_data['name']}\n"
                                                             f"CPF ou SSN: {faker_data['ssn']}\n"
                                                             f"Endereço: {faker_data['address']}\n"
                                                             f"Email: {faker_data['email']}\n"
                                                             f"Nascimento: {faker_data['birthday_date']}\n"
                                                             f"IP: {faker_data['ip']}\n"
                                                             f"===VEICULO===\n"
                                                             f"Nome: {faker_data['car_info']['vehicle']}\n"
                                                             f"Placa: {faker_data['car_info']['license_plate']}\n"
                                                             f"===EMPRESA===\n"
                                                             f"Nome: {faker_data['company']['name']}\n"
                                                            f"Lema: {faker_data['company']['catch_phrase']}\n"
                                                            f"Cargo: {faker_data['company']['job']}\n"
                                                            f"===CARTÃO DE CRÉDITO===\n"
                                                            f"Provedora: {faker_data['cc']['provider']}\n"
                                                            f"Número: {faker_data['cc']['num']}\n"
                                                            f"Código de segurança: {faker_data['cc']['security_code']}\n"
                                                            f"Data de expiração: {faker_data['cc']['expiration_date']}")

                response_txt_created(name_archive)
            except:
                error("País não encontrado ou pasta 'datas' foi deletada", 2)
                continue

        if event == "Sair":
            break

    win.close()