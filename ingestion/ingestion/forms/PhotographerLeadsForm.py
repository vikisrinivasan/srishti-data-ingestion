import django_tables2 as tables
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from ..models.utils.MasterData import City,Country,InstitutionType
from django import forms
# Create the form class.
from ..models.PhotographerLeads import PhotographerLeads

class PhotographerLeadsForm(forms.ModelForm):
    YES_NO = ((True, 'Yes'), (False, 'No'))
    lead_created_date=forms.DateField(widget=forms.DateInput(attrs={'class':'input-control','placeholder':"Date"}))
    Pro=forms.BooleanField(widget=forms.RadioSelect(attrs={'class':'input-control','placeholder':"Pro Level"},choices=YES_NO))
    Youtube=forms.URLField(widget=forms.URLInput(attrs={'class':'input-control','placeholder':"Youtube Link"}))
    Instagram=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Instagram Link"}))
    Snapchat=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Snapchat Link"}))
    Facebook=forms.URLField(widget=forms.URLInput(attrs={'class':'input-control','placeholder':"Facebook Link"}))
    Twitter=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Twitter Link"}))
    LinkedIn=forms.URLField(widget=forms.URLInput(attrs={'class':'input-control','placeholder':"Linkedin Link"}))
    Website=forms.URLField(widget=forms.URLInput(attrs={'class':'input-control','placeholder':"Website Link"}))
    SalesPerson=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"salesperson"}))
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"name"}))
    Phone=forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Home Phone Number"}))
    Phone1=forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Office Phone Number"}))
    Phone2=forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Mobile Number"}))
    Email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-control','placeholder':"Primary Email ID"}))
    Email1=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-control','placeholder':"Secondary Email ID"}))
    Email2=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-control','placeholder':"Email ID 3"}))
    ProductOwned=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Product Owned"}))
    City = forms.ChoiceField(
        choices=City.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"City"})
    )
    Country = forms.ChoiceField(
        choices=Country.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"Country"})
    )
    GenreTags=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Genre"}))
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('lead_created_date', css_class='input-xlarge'),

        Field('Pro', css_class='input-xlarge'),
        Field('Youtube', css_class='input-xlarge'),
        Field('Instagram', css_class='input-xlarge'),
        Field('Snapchat', css_class='input-xlarge'),
        Field('Facebook',css_class='input-xlarge'),
        Field('Twitter', css_class='input-xlarge'),
        Field('LinkedIn', css_class='input-xlarge'),
        Field('Website', css_class='input-xlarge'),

        Field('SalesPerson', css_class='input-xlarge'),
        Field('Name', css_class='input-xlarge'),
        Field('Phone', css_class='input-xlarge'),
        Field('Phone1', css_class='input-xlarge'),
        Field('Phone2', css_class='input-xlarge'),
        Field('Email', css_class='input-xlarge'),
        Field('Email1', css_class='input-xlarge'),
        Field('Email2', css_class='input-xlarge'),
        Field('ProductOwned', css_class='input-xlarge'),
        Field('City', css_class='input-xlarge'),
        Field('Country', css_class='input-xlarge'),
        Field('GenreTags', css_class='input-xlarge'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        ))
    helper.form_method = 'POST'

    class Meta:
        model = PhotographerLeads
        exclude = ("Id", )

