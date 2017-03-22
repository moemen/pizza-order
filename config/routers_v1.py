from django.conf.urls import include, url

urlpatterns = [
    url('^', include('pizza.orders.urls')),
    url('^', include('pizza.pizza.urls')),
]
