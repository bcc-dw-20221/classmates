from django.test import TestCase

from bar.models import Postagem

import json

# Create your tests here.
class PostagensTestCase(TestCase):
    def setUp(self):
        Postagem.objects.create(texto="Hoje é o dia do corno, foi bom te encontrar.")
        Postagem.objects.create(
            texto="Manda esse homem embora, mete o pé na bunda dele."
        )

    def tests_postagem_retorna_403_para_http_nao_post(self):
        response = self.client.get("/bar/add/")

        self.assertEqual(response.status_code, 403)

    def tests_postagem_retorna_200_para_post(self):
        response = self.client.post(
            "/bar/add/",
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
        response = self.client.get("/bar/")

        resp_dict = json.loads(response.content)

        self.assertTrue("postagens" in resp_dict)
        self.assertGreaterEqual(len(resp_dict["postagens"]), 1)

    def tests_get_postagem_especifica(self):
        response = self.client.get("/bar/get/1/")

        resp_dict = json.loads(response.content)

        self.assertTrue("postagem" in resp_dict)

    def tests_delete_item(self):
        response_delete = self.client.get("/bar/remove/1/")

        self.assertEqual(response_delete.status_code, 200)
