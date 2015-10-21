from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

class SmokeTest(StaticLiveServerTestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_connect_to_home_page(self):
        pass
