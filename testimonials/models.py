from django.db import models
from wagtail.snippets.models import register_snippet

@register_snippet
class Testimonials(models.Model):
    quote = models.TextField(
        max_length = 500,
        blank = False,
        null = False
    )

    author = models.CharField(
        max_length = 50,
        blank = False,
        null = False
    )

    def __str__(self):
        return f"{self.quote} par {self.author}"
    
    class Meta:                                     #  code pour
        verbose_name="Testimonial"              #  renommer
        verbose_name_plural="Testimonials"      #  les champs (Admin UI)