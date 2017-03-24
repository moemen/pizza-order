from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField


class Pizza(models.Model):
    SIZE_CHOICES = (
        ('30cm', _('30 CM')),
        ('40cm', _('40 CM')),
        ('50cm', _('50 CM')),
        ('55cm', _('55 CM')),
    )
    name = models.CharField(_('Pizza Name'), max_length=250)
    sizes = ArrayField(models.CharField(max_length=50, choices=SIZE_CHOICES))

    class Meta:
        verbose_name = _("Pizza")
        verbose_name_plural = _("Pizzas")

    def __str__(self):
        return self.name
