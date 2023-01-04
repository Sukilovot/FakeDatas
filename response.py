import PySimpleGUI as sg

def response(json):
    layout = [
        [sg.Text("Fake Datas")],
        [sg.Text(f"===INFORMAÇÕES BÁSICAS")],
        [sg.Text(f"Nome: {json['name']}")],
        [sg.Text(f"CPF ou SSN: {json['ssn']}")],
        [sg.Text(f"Número de telefone: {json['phone_number']}")],
        [sg.Text(f"Endereço: {json['address']}")],
        [sg.Text(f"Email: {json['email']}")],
        [sg.Text(f"Nascimento: {json['birthday_date']}")],
        [sg.Text(f"IP: {json['ip']}")],
        [sg.Text(f"===VEICULO")],
        [sg.Text(f"Nome: {json['car_info']['vehicle']}")],
        [sg.Text(f"Placa: {json['car_info']['license_plate']}")],
        [sg.Text(f"===EMPRESA")],
        [sg.Text(f"Nome: {json['company']['name']}")],
        [sg.Text(f"Função: {json['company']['job']}")],
        [sg.Text(f"Lema: {json['company']['catch_phrase']}")],
        [sg.Text(f"===CARTÃO DE CRÉTIDO")],
        [sg.Text(f"Provedora: {json['cc']['provider']}")],
        [sg.Text(f"Número: {json['cc']['num']}")],
        [sg.Text(f"Código de segurança: {json['cc']['security_code']}")],
        [sg.Text(f"Expira em: {json['cc']['expiration_date']}")],
        [sg.Text("===CONTAS BANCARIAS")],
        [sg.Text(f"Número da conta do banco: {json['bank_acc_num']['basic_bank_acc_num']}")],
        [sg.Text(f"Número da conta internacional do banco: {json['bank_acc_num']['internacional_bank_acc_num']}")],
        [sg.Button("Sair")]
    ]

    win = sg.Window("Fake Datas", layout, icon="favicon.ico")

    while True:
        event, values = win.read()

        if event == "Sair":
            break

    win.close()