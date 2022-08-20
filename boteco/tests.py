import json

from django.test import TestCase

from boteco.models import Postagem


# Create your tests here.
class PostagensTestCase(TestCase):
    def setUp(self):
        Postagem.objects.create(texto="Hoje é o dia do corno, foi bom te encontrar.")
        Postagem.objects.create(
            texto="Manda esse homem embora, mete o pé na bunda dele."
        )

    def tests_postagem_retorna_405_para_http_nao_post(self):
        response = self.client.get("/boteco/add/")

        self.assertEqual(response.status_code, 405)

    def tests_postagem_retorna_200_para_post(self):
        response = self.client.post(
            "/boteco/add/",
            data={
                "texto": "O homem sem chifre é um animal indefeso.",
            },
        )
        existe = Postagem.objects.filter(
            texto="O homem sem chifre é um animal indefeso."
        )

        self.assertEqual(len(existe), 1)
        self.assertEqual(response.status_code, 200)

    def tests_endpoint_todas_as_postagens(self):
        response = self.client.get("/boteco/")

        resp_dict = json.loads(response.content)

        self.assertGreaterEqual(len(resp_dict), 1)

    def tests_get_postagem_especifica(self):
        response = self.client.get("/boteco/get/1/")

        resp_dict = json.loads(response.content)

        self.assertTrue(
            resp_dict[0]["fields"]["texto"]
            == "Hoje é o dia do corno, foi bom te encontrar."
        )

    def tests_delete_item(self):
        response_delete = self.client.delete("/boteco/remove/1/")

        self.assertEqual(response_delete.status_code, 200)
