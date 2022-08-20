from django.test import TestCase

from boteco.models import Postagem

# Create your tests here.
class PostagensTestCase(TestCase):
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

        self.assertGreaterEqual(len(existe), 1)
        self.assertEqual(response.status_code, 200)
