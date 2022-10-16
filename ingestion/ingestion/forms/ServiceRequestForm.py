import django_tables2 as tables
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from ..models.utils.MasterData import City,Country
# Create the form class.
from ..models.ServiceRequest import ServiceRequests

class ServiceRequestForm(forms.ModelForm):
    YES_NO = ((True, 'Yes'), (False, 'No'))
    RequestDate=forms.DateField(widget=forms.DateInput(attrs={'class':'input-control','placeholder':"Request Date"}))
    Brand=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Brand"}))
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Name"}))
    RequestText=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Request Text"}))
    Phone=forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Home Phone Number"}))
    Email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-control','placeholder':"Primary Email ID"}))
    City = forms.ChoiceField(
        choices=City.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"City"})
    )
    Country = forms.ChoiceField(
        choices=Country.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"Country"})
    )
    ClosedDate=forms.DateField(widget=forms.DateInput(attrs={'class':'input-control','placeholder':"Request Date"}))
    Resolution=forms.BooleanField( widget=forms.RadioSelect(attrs={'class':'input-control','placeholder':"Permission To Give Data"},choices=YES_NO))
    ProductsEnquired=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Products Enquired"}))
    ResolvedBy=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Resolved By"}))
    ServiceCenter=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Service Center"}))

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('RequestDate', css_class='input-xlarge'),
        Field('Brand', css_class='input-xlarge'),
        Field('Name', css_class='input-xlarge'),
        Field('Phone', css_class='input-xlarge'),
        Field('Email', css_class='input-xlarge'),
        Field('City', css_class='col-md-6'),
        Field('Country', css_class='col-md-6'),
        Field('ClosedDate', css_class='input-xlarge'),
        Field('Resolution', css_class='input-xlarge'),
        Field('ProductsEnquired', css_class='input-xlarge'),
        Field('ResolvedBy', css_class='input-xlarge'),
        Field('ServiceCenter', css_class='input-xlarge'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        ))
    helper.form_method = 'POST'

    class Meta:
        model = ServiceRequests
        exclude = ("Id", )

