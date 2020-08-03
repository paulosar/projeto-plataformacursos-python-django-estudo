from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse as rv

class HomeViewTest(TestCase):

    def test_home(self):
        client = Client()
        rp = client.get(rv('core:home'))
        return self.assertEqual(rp.status_code, 200)

    def test_home_template(self):
        client = Client()
        rp = client.get(rv('core:home'))
        return self.assertTemplateUsed(rp, 'home.html')