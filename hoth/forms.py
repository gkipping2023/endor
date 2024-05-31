from django.forms import ModelForm
from .models import Logbook, User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from datetime import date

class new_entry_form(ModelForm):
    date = forms.DateField(label='Fecha',initial=date.today(),widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    equip = forms.CharField(max_length=250,label='C172',empty_value=None,widget=forms.TextInput(attrs={'class':'form-control'}))
    registration = forms.CharField(max_length=50,initial='HP1234',empty_value=None,widget=forms.TextInput(attrs={'class':'form-control','id':'block1','oninput':'myFunction()'}))
    origin = forms.CharField(max_length=80, label='Origen',empty_value=None,widget=forms.TextInput(attrs={'class':'form-control','list':'airports'})) #Dropdown de Airports
    destination = forms.CharField(max_length=80, label= 'Destination',empty_value=None,widget=forms.TextInput(attrs={'class':'form-control','list':'airports'})) #Dropdown de Airports
    airplane_sel = forms.DecimalField(max_digits=15,decimal_places=2,required=False,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    airplane_mel = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    airplane_cfi = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    x_country = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    night = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    act_ifr = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    sim_ifr = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    gnd_trainer = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    pic = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    sic = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    dual = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    totalt = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    remarks = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    synth_trainer = forms.DecimalField(max_digits=15,decimal_places=2,initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Logbook
        fields = [
        'date',
        'equip',
        'registration',
        'origin',
        'destination',
        'airplane_sel',
        'airplane_mel',
        'x_country',
        'night',
        'act_ifr',
        'sim_ifr',
        'gnd_trainer',
        'pic',
        'sic',
        'dual',
        'totalt',
        'remarks',
        'synth_trainer'

        ]