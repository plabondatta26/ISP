from django.contrib import admin
from django.urls import path
from .views import HomeView, PackagesView, BillingView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('packages/', PackagesView.as_view(), name="packages"),
    path('biliings/', BillingView.as_view(), name="billings"),
]
