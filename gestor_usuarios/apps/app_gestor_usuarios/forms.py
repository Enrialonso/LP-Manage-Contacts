from django import forms

from apps.app_gestor_usuarios.models import db_usuarios, db_manage_contacts

class signupForm(forms.ModelForm):


    class Meta:
        model = db_usuarios

        fields = [
            'name',
            'last',
            'email',
            'password',
        ]
        labels = {
            'name':'Name',
            'last':'Last',
            'email':'Email',
            'password':'Password',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'last': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }

class loginForm(forms.ModelForm):


    class Meta:
        model = db_usuarios

        fields = [
            'email',
            'password',
        ]
        labels = {
            'email':'Email',
            'password':'Password',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }

class addForm(forms.ModelForm):

    class Meta:
        model = db_manage_contacts

        fields = [
            'id',
            'associated_user',
            'name',
            'last',
            'email',
            'phone_local',
            'phone_mov',
            'street',
            'street_number',
            'population',
            'state',
            'postalcode',
            'country',
            'url_web',
        ]
        labels = {
            'id':'id',
            'associated_user':'Associated User',
            'name':'Name',
            'last':'Last',
            'email':'Email',
            'phone_local':'Local Phone',
            'phone_mov':'Cel. Phone',
            'street':'Street',
            'street_number':'Street Number',
            'population':'Population',
            'state':'Comunity',
            'postalcode':'Postal code',
            'country':'Country',
            'url_web':'Web or Blog',
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'associated_user':forms.EmailInput(attrs={'class':'form-control','readonly':'True'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'last': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone_local': forms.TextInput(attrs={'class':'form-control'}),
            'phone_mov': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'id':'route'}),
            'street_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'street_number'}),
            'population': forms.TextInput(attrs={'class': 'form-control', 'id':'locality'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'id': 'administrative_area_level_1'}),
            'postalcode': forms.TextInput(attrs={'class': 'form-control', 'id':'postal_code'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'id':'country'}),
            'url_web': forms.URLInput(attrs={'class': 'form-control'}),

        }