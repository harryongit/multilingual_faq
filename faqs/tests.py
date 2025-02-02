from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        FAQ.objects.create(question="Test Question", answer="Test Answer")

    def test_faq_creation(self):
        faq = FAQ.objects.first()
        self.assertEqual(faq.question, "Test Question")
