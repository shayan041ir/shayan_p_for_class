from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField()
    price = forms.IntegerField()