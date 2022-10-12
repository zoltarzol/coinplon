from django.db import models
from django.forms import ValidationError
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel

class ServicesListingPage(Page):
    template = 'services/services_listing_page.html'
    subtitle = models.TextField(
        blank=True,
        max_length=500
    )
    content_panels = Page.content_panels + [
        FieldPanel("subtitle")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['services'] = ServicePage.objects.live().public()
        import pudb; # pu.db()
        return context


class ServicePage(Page):
    description = models.TextField(
        blank=True,
        max_length=500
    )

    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name="+",
        help_text="Sélectionner une page interne",
        on_delete=models.SET_NULL
    )

    external_page = models.URLField(blank=True)

    button_text = models.CharField(blank=True, max_length=50)

    service_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text="Choisir une image pour ce service",
        related_name="+"

    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel('internal_page'),
        FieldPanel('external_page'),
        FieldPanel('button_text'),
        FieldPanel('service_image'), 
    ]

    def clean(self):
        super().clean()

        if self.internal_page and self.external_page:
            raise ValidationError({
                'internal_page' : ValidationError('Sélectionnez un lien interne OU un lien externe'),
                'external_page' : ValidationError('Sélectionnez un lien interne OU un lien externe')
            })
        if not self.internal_page and not self.external_page:
            raise ValidationError({
                'internal_page' : ValidationError('Vous dever sélectionnez un lien interne OU un lien externe'),
                'external_page' : ValidationError('Vous dever sélectionnez un lien interne OU un lien externe')
            })