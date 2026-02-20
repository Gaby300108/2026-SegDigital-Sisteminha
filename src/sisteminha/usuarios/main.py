from ..senhas import PasswordService
from werkzeug.security import generate_password_hash

class UsuarioService:
    @staticmethod
    def criar_usuario():
        email = input("Digite o email para login:")
        senha = PasswordService.gerar_senha(tamanho = 5,
                                            simbolos=False)
        # Semana que vem, guarda no banco
        print(senha)
        senha_pro_banco = generate_password_hash(senha)
        print(senha_pro_banco)
