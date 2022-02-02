
from django.contrib import admin
from django.urls import path

from pocetna.views import home_view, contact, about_view
from proizvodi.views import product_detail_view, product_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact),
    path('about/', about_view),
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('admin/', admin.site.urls),

]
