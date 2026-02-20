# 2026-SegDigital-Sisteminha

SegDigital Sisteminha — aplicação de linha de comando (CLI) em Python para gerenciamento de usuários com persistência em SQLite.

## Pré-requisitos

- [uv](https://docs.astral.sh/uv/) para gerenciamento de ambiente e dependências

## Instalação

```bash
uv sync
```

## Uso

```bash
uv run sisteminha
```

Por padrão, o banco de dados é criado no arquivo `sisteminha.db` no diretório atual. Para usar um arquivo diferente:

```bash
uv run sisteminha --db /caminho/para/banco.db
```

### Menu principal

Ao iniciar, a aplicação exibe um menu interativo com as seguintes opções:

| Opção | Ação |
|-------|------|
| `1` | Criar usuário |
| `2` | Listar usuários |
| `3` | Alterar nome de usuário |
| `4` | Mudar senha |
| `5` | Remover usuário |
| `0` | Sair |

## Funcionalidades

### Gerenciamento de usuários

- **Criar usuário** — cadastra um novo usuário informando nome, e-mail e senha. A senha é armazenada como hash (werkzeug).
- **Listar usuários** — exibe todos os usuários cadastrados.
- **Alterar nome** — exibe o nome atual do usuário e permite alterá-lo.
- **Mudar senha** — valida a senha atual antes de aceitar a nova.
- **Remover usuário** — remove o usuário pelo e-mail.

### Banco de dados

- Persistência em SQLite com criação automática do banco e das tabelas na primeira execução.
- Campos `created_at` e `updated_at` preenchidos com timestamps UTC (via `arrow`) em todas as operações de escrita.
- Caminho do arquivo de banco configurável via argumento `--db`.

### Segurança

- Senhas nunca são armazenadas em texto puro — geração e verificação de hash via `werkzeug.security`.
- Alteração de senha exige confirmação da senha atual.

## Arquitetura

```
src/sisteminha/
├── cli.py              # Ponto de entrada e menu interativo
├── models.py           # Modelo de domínio (Usuario)
├── database/
│   └── main.py         # DatabaseService — conexão e inicialização do SQLite
└── usuarios/
    └── main.py         # UsuarioDAO (acesso a dados) e UsuarioService (fluxos interativos)
```

## Desenvolvimento

```bash
# Instalar dependências
uv sync

# Executar a aplicação
uv run sisteminha

# Adicionar uma dependência
uv add <pacote>

# Adicionar uma dependência de desenvolvimento
uv add --dev <pacote>
```

## Dependências

| Pacote | Uso |
|--------|-----|
| `werkzeug` | Hash e verificação de senhas |
| `arrow` | Timestamps UTC para `created_at` / `updated_at` |
