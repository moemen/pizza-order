from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('customer_name', 'customer_address', 'size', 'pizza',)

    def validate(self, data):
        # To handle cases creation, update and partial update
        pizza = data.get('pizza', getattr(self.instance, 'pizza', None))
        size = data.get('size', getattr(self.instance, 'size', None))
        if size not in pizza.sizes:
            raise serializers.ValidationError(_('You should provide valid size for your pizza'))
        return data
