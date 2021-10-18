"""GlatexManagementSoftware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path("",views.Index, name="homeindex"),
    path("shop",views.Shop, name="shop"),
    path("cart",views.Cart, name="cart"),
    path("add_cart/<int:product_id>/",views.add_cart, name="add_cart"),
    path("shop/<slug:category_slug>/",views.Shop, name="product_by_category"),
    path("shop/<slug:category_slug>/<slug:product_slug>",views.ProductDetail, name="product_detail"),
    path("about",views.AboutUs, name="aboutus"),
    path("checkout",views.Checkout, name="checkout"),
    path("contacts",views.ContactUs, name="contactus"),
]
