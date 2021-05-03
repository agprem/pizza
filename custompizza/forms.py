from django.forms import ModelForm
from django import forms
from custompizza.models import Pizza
from django.core.exceptions import ValidationError
#from formValidationApp.models import *

class createpizza(ModelForm):
    class Meta:
        model=Pizza
        fields=["types","size","toppings"]

    def clean(self):
        size=self.cleaned_data['size']
        print("Hello",size)
        if (size !="big" and size != "medium" and size !="small"):
            print("inside val",size)
            raise forms.ValidationError("Only Small ,Medium and Big shape are available")
