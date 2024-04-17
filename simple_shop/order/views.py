from django.shortcuts import render
from django.views.generic import FormView
from .forms import OrderForm

# Create your views here.
class OrderCreate(FormView):
    form_class=OrderForm
    success_url='/product/'

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw