import argparse
from importlib.metadata import version

from sisteminha.usuarios import UsuarioService


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="sisteminha",
        description="SedDigital Sisteminha CLI",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {version('sisteminha')}",
    )
    parser.parse_args()

    print("Bem vindo!")
    print("="*60)

    while True:
        print()
        print("Escolha uma opção")
        print("[1] Criar uma conta")
        print("[0] Sair")
        try:
            opcao = int(input())
        except ValueError:
            print("Apenas numeros")
            continue
        match opcao:
            case 1:
                UsuarioService.criar_usuario()
            case 0:
                break
            case _:
                print("Opção inválida!")


if __name__ == "__main__":
    main()
