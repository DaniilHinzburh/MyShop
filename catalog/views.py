from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Buyer, Operator, Manufacturer, Category, Subcategory, Product, Order, Check


class IndexView(TemplateView):
    template_name = "catalog/index.html"
