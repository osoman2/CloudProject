from urllib import response
import string
import secrets
import requests
import os

class Security:
    @staticmethod
    def generate_pin():
        LEN = 6
        alphabet = string.digits

        while True:
            password = ''.join(secrets.choice(alphabet)
                               for i in range(LEN))
            if any(c.isdigit() for c in password):
                break

        return password

    @staticmethod
    def generate_pin_remote():
        domain_port = os.environ.get('OPENFAAS_HOST')
        #domain_port = "http://127.0.0.1:8080" #8080 inside docker, 8010 local      
        pin = ""
        rc = 0
        #Calling serverless function in OpenFaaS
        try:
            res = requests.get(domain_port+"/function/generate-pinv2")
            if res.status_code == 200:
                pin = res.text
                print(pin)
            else:
                rc = 1
                print("Error!")
        except BaseException as err:
            rc = 2
            print(f"Unexpected {err=}, {type(err)=}")

        return (pin, rc)          