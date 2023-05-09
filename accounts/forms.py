from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs = {
        'placeholder':'Mot de passe',
        'class':'form-control'
    }))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs = {
        'placeholder':'confirmer mot de passe',
        'class':'form-control'
    }))
    class Meta:
        
        model = Account
        fields = ['first_name', 'last_name','email','phone_number'] 
    
    def __init__(self,*args,**kwargs):
        
        
        super(RegistrationForm,self).__init__(*args,**kwargs)
        print(self.fields)
        self.fields['first_name'].widget.attrs['placeholder'] = 'votre nom'
        self.fields['last_name'].widget.attrs['placeholder'] = 'votre prenom'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'numero de telephone'
        self.fields['email'].widget.attrs['placeholder'] = 'votre email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'  
    
    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('repeat_password')
        
        if password!=confirm_password:
            raise forms.ValidationError('les mots de passes ne correspondent pas !')
        