from django.test import TestCase

# Create your tests here.
class Exemplo01TestCase(TestCase):
    """Testa a view exemplo1."""

    def tests_exemplo01_returns_status_200(self):
        """Testa o status de retorno."""
        client = self.client
        response = client.get("/1908/exemplo1/")

        self.assertEqual(response.status_code, 200)

    def tests_exemplo01_returns_string_planned(self):
        """Testa a mensagem retornada."""
        client = self.client
        response = client.get("/1908/exemplo1/")

        self.assertEqual(response.content, b"Uma mensagem foi retornada")


class Exemplo02TestCase(TestCase):
    """Testa a view exemplo2."""

    def tests_exemplo02_returns_status_404(self):
        """Testa o status retornado."""
        id_exemplo = 20

        client = self.client
        response = client.get(f"/1908/exemplo2/{id_exemplo}/")

        self.assertEqual(response.status_code, 404)

    def tests_exemplo02_returns_string_planned(self):
        """Testa a mensagem retornada."""
        id_exemplo = 20

        client = self.client
        response = client.get(f"/1908/exemplo2/{id_exemplo}/")

        self.assertEqual(response.content, b"Usuario de ID: 20 nao existe.")
