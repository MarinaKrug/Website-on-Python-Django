from django.urls import path

from locks.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', index, name='index'),
    path('sale/', Sale.as_view(), name='show_sale'),
    path('contacts/', contacts, name='show_contacts'),
    path('services/', Services.as_view(), name='show_services'),
    path('gallery/', Galleries.as_view(), name='show_gallery'),
    path('category/<slug:cat_slug>/', Categories.as_view(), name='show_category')
]