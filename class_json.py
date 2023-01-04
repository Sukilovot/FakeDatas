from faker import Faker
from random import choice, randint
from faker_vehicle import VehicleProvider
import datetime
from faker.providers import internet

class data_json:
    def __init__(self, country):
        country = country.strip()
        data = Faker(country)
        data.add_provider(VehicleProvider)
        data.add_provider(internet)

        self.faker_data = {
            "name": data.name(),
            "ssn": data.ssn(),
            "ip": data.ipv4(),
            "address": str(data.address()).replace(" / ", "-"),
            "email": str(data.email()).replace("example.org" or "example.net" or "example.com", str(choice(
                ["gmail.com", "hotmail.com", "outlook.com", "green.info", "howard-snow.com", "lloyd.org",
                 "rivera.com", "green.com", "yahoo.com", "archer-patel.org", "castro-gomez.com",
                 "brown-sellers.com"]))),
            "car_info": {
                "license_plate": data.license_plate(),
                "vehicle": data.vehicle_year_make_model_cat()
            },
            "birthday_date": data.date_of_birth(),
            "phone_number": data.phone_number(),
            "bank_acc_num": {
                "basic_bank_acc_num": data.bban(),
                "internacional_bank_acc_num": data.iban()
            },
            "company": {
                "name": data.company(),
                "catch_phrase": data.catch_phrase(),
                "job": data.job()
            },
            "cc": {
                "provider": data.credit_card_provider(),
                "num": data.credit_card_number(),
                "security_code": data.credit_card_security_code(),
                "expiration_date": data.credit_card_expire()
            }
        }

    def return_json(self):
        return self.faker_data