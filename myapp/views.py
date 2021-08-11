from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic.base import ContextMixin
from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView
from .models import Product, Item
from .forms import ProductForm, ItemForm
from django.utils.translation import gettext as _
import urllib

# Create your views here.
def index(request):
    default_language = {
        'tk':'/tk/home/',
        'en':'/en/home/',
    }
    return redirect('{}'.format(default_language[settings.LANGUAGE_CODE]))

class MyContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['hello'] = _('Hello world !')
        return context


class HomeIndexView(CreateView, MyContextMixin):
    template_name = 'myapp/index.html'
    form_class = ProductForm
    success_url = '/'

class AboutView(TemplateView, MyContextMixin):
    template_name = 'myapp/about.html'

class AnotherView(CreateView, ListView, MyContextMixin):
    queryset = Item.objects.order_by('-id')
    paginate_by = 10
    template_name = 'myapp/another.html'
    form_class = ItemForm
    success_url = '/another/'
