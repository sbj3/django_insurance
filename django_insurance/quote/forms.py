from django import forms 
from .import models 

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['first_name', 'last_name', 'address','telephone', 'email_address',
                  'date_of_birth', 'home_ownership_options', 'home_ownership']
    
    
