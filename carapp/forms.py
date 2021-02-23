from django import forms
from django.forms import ModelForm
from .models import Car

class CarCreateForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        mileage = cleaned_data.get('mileage')
        price = cleaned_data.get('price')
        if mileage<0:
            msg = 'Invalid entry'
            self.add_error('mileage',msg)
        if price<1:
            msg = 'Invalid entry'
            self.add_error('price',msg)