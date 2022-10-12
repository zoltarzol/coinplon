from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
import lorem

# Create your models here.
class FlexPage(Page): 
    template = 'flex/flex_page.html'

    lorem = models.TextField(
            blank=True,
            max_length=500,
            default=lorem.paragraph()
        )

    content_panels = Page.content_panels + [
        FieldPanel("lorem")
        ]

    class Meta:                               #  code pour
        verbose_name="Flex Page"              #  renommer
        verbose_name_plural="Flex Pages"      #  les champs (Admin UI)
