from django.db import models
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):
    customer_name = models.CharField(_('Customer Name'), max_length=150)
    customer_address = models.TextField(_('Customer Address'))
    size = models.CharField(_('Pizza Size'), max_length=50)
    pizza = models.ForeignKey('pizza.pizza')

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return "Order {pizza} to {customer}".format(pizza=self.pizza,
                                                    customer=self.customer_name)
