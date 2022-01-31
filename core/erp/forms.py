from django.forms import *
from core.erp.models import Category


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder':'Introduzca el nombre'
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Introduzca la descripción'
                }
            )
        }
