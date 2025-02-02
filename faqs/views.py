from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()
        data = [faq.get_translation(lang) for faq in faqs]
        return Response(data)
