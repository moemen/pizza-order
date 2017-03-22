from django.db import models
from django.utils.translation import ugettext_lazy as _


class Pizza(models.Model):
    name = models.CharField(_('Pizza Name'), max_length=250)

    class Meta:
        verbose_name = _("Pizza")
        verbose_name_plural = _("Pizzas")

    def __str__(self):
        return self.name
