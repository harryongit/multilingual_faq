from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from googletrans import Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))
    question_hi = models.TextField(_("Hindi Question"), blank=True, null=True)
    answer_hi = RichTextField(_("Hindi Answer"), blank=True, null=True)
    question_bn = models.TextField(_("Bengali Question"), blank=True, null=True)
    answer_bn = RichTextField(_("Bengali Answer"), blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()

        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text

        super().save(*args, **kwargs)

    def get_translation(self, lang='en'):
        """ Fetch translated FAQ dynamically from cache or DB """
        cache_key = f"faq_{self.pk}_{lang}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data
        
        if lang == 'hi':
            data = {"question": self.question_hi, "answer": self.answer_hi}
        elif lang == 'bn':
            data = {"question": self.question_bn, "answer": self.answer_bn}
        else:
            data = {"question": self.question, "answer": self.answer}
        
        cache.set(cache_key, data, timeout=86400)  # Cache for 1 day
        return data

    def __str__(self):
        return self.question
