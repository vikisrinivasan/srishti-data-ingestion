import django_tables2 as tables
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from ..models.utils.MasterData import City,Country,InstitutionType
from django import forms
# Create the form class.
from ..models.InstitutionalClients import InstitutionalClients

class InstitutionalClientsForm(forms.ModelForm):
    Date=forms.DateField(widget=forms.DateInput(attrs={'class':'input-control','placeholder':"Date"}))
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Event Attender Name"}))
    Contact=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Instagram Link"}))
    Contact1=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Snapchat Link"}))
    Contact2=forms.URLField(widget=forms.URLInput(attrs={'class':'input-control','placeholder':"Facebook Link"}))
    InstitutionType= forms.ChoiceField(
        choices=InstitutionType.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"Institution Type"})
    )
    Phone=forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Home Phone Number"}))
    Phone1=forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Office Phone Number"}))
    Phone2=forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Mobile Number"}))
    Email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-control','placeholder':"Primary Email ID"}))
    Email1=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-control','placeholder':"Secondary Email ID"}))
    Email2=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-control','placeholder':"Email ID 3"}))
    Website=forms.URLField(widget=forms.URLInput(attrs={'class':'input-control','placeholder':"Website Link"}))
    Address=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Address"}))


    City = forms.ChoiceField(
        choices=City.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"City"})
    )
    Country = forms.ChoiceField(
        choices=Country.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"Country"})
    )
    Products=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Products"}))
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('Date', css_class='input-xlarge'),

        Field('Name', css_class='input-xlarge'),
        Field('Contact', style="background: #FAFAFA; padding: 10px;"),
        Field('Contact1', css_class='input-xlarge'),
        Field('Contact2', css_class='input-xlarge'),
        Field('InstitutionType', css_class='input-xlarge'),
        Field('Phone', css_class='input-xlarge'),
        Field('Phone1', css_class='input-xlarge'),
        Field('Phone2', css_class='input-xlarge'),
        Field('Email', css_class='input-xlarge'),
        Field('Email1', css_class='input-xlarge'),
        Field('Email2', css_class='input-xlarge'),
        Field('Website', css_class='input-xlarge'),
        Field('Address', css_class='input-xlarge'),
        Field('City', css_class='input-xlarge'),
        Field('Country', css_class='input-xlarge'),
        Field('Products', css_class='input-xlarge'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        ))
    helper.form_method = 'POST'

    class Meta:
        model = InstitutionalClients
        exclude = ("Id", )

