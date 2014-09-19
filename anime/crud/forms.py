from django import forms
from crud.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
