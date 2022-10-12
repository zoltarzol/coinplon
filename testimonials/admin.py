from unittest import TestSuite
from django.contrib import admin
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Testimonials

class TestimonialsAdmin(ModelAdmin):
    model = Testimonials
    menu_label = "Testimonials"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

modeladmin_register(TestimonialsAdmin)