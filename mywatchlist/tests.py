from multiprocessing.connection import Client
from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class ApplicationTest(TestCase):
    def test_html_existance(self):
        response = Client().get('http://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

class ApplicationTest(TestCase):
    def test_xml_existance(self):
        response = Client().get('http://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

class ApplicationTest(TestCase):
    def test_json_existance(self):
        response = Client().get('http://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code,200)