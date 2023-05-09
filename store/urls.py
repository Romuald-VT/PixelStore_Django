from django.urls import path
from .views import store_page,product_detail,search

urlpatterns = [
    path('',store_page, name='store_page'),
    path("category/<slug:cat_slug>/",store_page,name='product_by_category'),
    path("category/<slug:cat_slug>/<slug:prod_slug>/",product_detail,name='product_detail'),
    path('search/',search,name='search')
    
]
