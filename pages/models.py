from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# 1. La page de votre salon sur Wagtail
class PrestationsPage(Page):
    introduction = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
    ]

# 2. Le modèle pour enregistrer chaque réservation
class Reservation(models.Model):
    utilisateur = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    date_heure = models.DateTimeField()
    service = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} - {self.service}"

    content_panels = Page.content_panels + [
        FieldPanel("utilisateur"),
        FieldPanel("email"),
        FieldPanel("date_heure"),
        FieldPanel("service")
    ]

 
class EquipePage(Page):
    pass


class ContactPage(Page):
    pass
