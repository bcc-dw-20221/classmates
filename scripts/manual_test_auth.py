import json
from faker import Faker
from faker.providers import date_time, person, internet, misc

import requests as r

Faker.seed(0)
fake = Faker("pt-BR")
fake.add_provider(date_time)
fake.add_provider(person)
fake.add_provider(internet)
fake.add_provider(misc)


BASE_URL = "http://localhost:8000"

# Vamos solicitar nosso par de tokens
resp = r.post(
    f"{BASE_URL}/api/token/", {"username": "felipe", "password": "1234"}
)

print(resp.content.decode("utf-8"))

# extraindo as tokens para uso nos próximos exemplos

tokens = json.loads(resp.content)

# Vamos verificar nossa token de acesso
resp = r.post(
    f"{BASE_URL}/api/token/verify/",
    {"token": f"{tokens['access']}"},
)

print(f"A verificação da token retornou: {resp}")

# Vamos acessar um dos endpoints
resp = r.get(f"{BASE_URL}/boteco/api/perfis/")

print(resp.content.decode("utf-8"))

# Vamos inserir um novo item no endpoint
# Atenção: nas libs do JS e TS a gente usa o formato JSON normal.
#          Aqui no requests, precisei adaptar pro padrão user.atributo.
with open("chifre.jpg", "rb") as profile_pic:
    files = {
        "foto_perfil": profile_pic,
    }
    senha = fake.password()
    print(f"A senha é: {senha}")
    novo_corno = {
        "user.username": fake.user_name(),
        "user.password": senha,
        "user.email": fake.ascii_email(),
        "user.first_name": fake.first_name(),
        "user.last_name": fake.last_name(),
        "foto_perfil": "chifre.jpg",
        "qtd_chifres": 0,
        "ultimo_chifre": fake.date_time(),
        "procurando_mais": fake.boolean(),
    }

    resp = r.post(
        f"{BASE_URL}/boteco/api/perfis/",
        data=novo_corno,
        files=files,
        headers={
            "Authorization": f"Bearer {tokens['access']}",
        },
    )

    print(resp.content.decode("utf-8"))
