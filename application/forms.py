from django import forms
from django.forms import ModelForm
from .models import Stock, Product


class StockCreateForm(ModelForm):
    def __init__(self, *args, category=None, **kwargs):
        super().__init__(*args, **kwargs)
        if category:
            self.fields['product'].queryset = Product.objects.filter(category__name=category)

    class Meta:
        model = Stock
        fields = '__all__'
