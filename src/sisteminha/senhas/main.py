import secrets
import string
from random import shuffle


class PasswordService:

    @staticmethod
    def gerar_senha(tamanho: int=10,
                    maiusculas: bool=True,
                    minusculas: bool=True,
                    digitos: bool=True,
                    simbolos: bool=True,
                    remover_confusos: bool=True) -> str:
        espaco = ""
        senha = []
        if maiusculas:
            valores = string.ascii_uppercase if not remover_confusos\
                                            else "ABCDEFGHJKLMNPRSTUVWXYZ"
            espaco += valores
            senha.append(secrets.choice(valores))
            tamanho -= 1
        if minusculas:
            valores = string.ascii_lowercase if not remover_confusos\
                                             else "abcdefghjkmnpqrstuvwxyz"
            espaco += valores
            senha.append(secrets.choice(valores))
            tamanho -= 1
        if digitos:
            valores = "0123456789" if not remover_confusos\
                                   else "23456789"
            espaco += valores
            senha.append(secrets.choice(valores))
            tamanho -= 1
        if simbolos:
            valores = string.punctuation if not remover_confusos \
                                         else "@#$%&*-+=[]^:?/"
            espaco += valores
            senha.append(secrets.choice(valores))
            tamanho -= 1
        for _ in range(tamanho):
            senha.append(secrets.choice(espaco))
        shuffle(senha)
        return "".join(senha)

    @staticmethod
    def validar_complexidade():
        pass