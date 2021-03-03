from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from data_logger.models import Node, Data
# Create your tests here.


class ApiTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("timo", "timo@testaaja.fi", "salasana", is_superuser=True)
        self.client = APIClient()
        token = Token.objects.get(user_id=self.user.id)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token.key)

    def test_add_data(self):
        node = Node.objects.create(name="testikone", type=1, address="32:32:32:32:32")
        data = {
            "type": "temperature",
            "value": "4",
            "node": node.address
        }
        response = self.client.post('/api/data-logger/data/', type='json', data=data)
        self.assertTrue(200 <= response.status_code <= 204,
                        msg="{}: {}".format(response.status_code, response.data)
                        )





