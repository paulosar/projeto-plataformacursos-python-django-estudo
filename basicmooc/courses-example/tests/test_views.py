from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse as rv
from django.core import mail
from django.conf import settings

from simplemooc.courses.models import Course

class ContactCouseTestCase(TestCase):

    def setUp(self):
        self.course = Course.objects.create(name='Django', slug='django')

    def test_contact_from_error(self):
        data = {'name': 'Fulano', 'email':'', 'message':''}
        client = Client()
        path = rv('courses:details', args=[self.course.slug])
        rp = client.post(path, data)
        self.assertFormError(rp, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(rp, 'form', 'message', 'Este campo é obrigatório.')

    def test_contact_form_success(self):
        data = {'name': 'Fulano', 'email': 'fulano@teste.com', 'message': 'teste mensagem'}
        client = Client()
        path = rv('courses:details', args=[self.course.slug])
        client.post(path, data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])