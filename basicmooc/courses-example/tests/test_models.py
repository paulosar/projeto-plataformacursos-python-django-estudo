from django.test import TestCase
from django.test.client import Client
from model_mommy import mommy

from simplemooc.courses.models import Course


class CourseManagerTestCase(TestCase):

    def setUp(self):
        self.courses_python = mommy.make('courses.Course', name='python', _quantity=5)
        self.courses_django = mommy.make('courses.Course', name='django', _quantity=10)
        self.client = Client

    def tearDown(self):
        Course.objects.all().delete()

    def testSearch(self):
        s1 = Course.objects.search('django')
        s2 = Course.objects.search('python')
        self.assertEquals(len(s1), 5)
        self.assertEquals(len(s2), 10)