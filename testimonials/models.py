from django.db import models

# Create your models here.
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
        return "test" #self.name
    
    class Meta:                                     #  code pour
            verbose_name="Testimonial"              #  renommer
            verbose_name_plural="Testimonials"      #  les champs (Admin UI)