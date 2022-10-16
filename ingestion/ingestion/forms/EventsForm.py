import django_tables2 as tables
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from ..models.utils.MasterData import City,Country
from django import forms
# Create the form class.
from ..models.Events import Events

class EventForm(forms.ModelForm):
    YES_NO = ((True, 'Yes'), (False, 'No'))
    Date=forms.DateField(widget=forms.DateInput(attrs={'class':'input-control','placeholder':"Date"}))
    EventKey=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Event Name"}))
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Event Attender Name"}))
    Type=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Event Type"}))
    Mode=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Event Mode (Virtual or Physical"}))
    Venue=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Venue Address"}))
    StartDate=forms.DateField(widget=forms.DateInput(attrs={'class':'input-control','placeholder':"Date"}))
    EndDate=forms.DateField(widget=forms.DateInput(attrs={'class':'input-control','placeholder':"Date"}))
    Partner=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Comma Seperated list of partners"}))
    AffliateBrand=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Affliate Brand"}))
    AffliateBrand1=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Affliate Brand1"}))
    AffliateBrand2=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Affliate Brand2"}))



    City = forms.ChoiceField(
        choices=City.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"City"})
    )
    Country = forms.ChoiceField(
        choices=Country.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"Country"})
    )
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('Date', css_class='input-xlarge'),
        Field('EventKey', css_class='input-xlarge'),

        Field('Name', css_class='input-xlarge'),
        Field('Type', css_class='input-xlarge'),
        Field('Mode', css_class='input-xlarge'),
        Field('Venue', css_class='input-xlarge'),
        Field('StartDate', css_class='input-xlarge'),
        Field('EndDate',css_class='input-xlarge'),
        Field('Partner', css_class='input-xlarge'),
        Field('AffliateBrand', css_class='input-xlarge'),
        Field('AffliateBrand1', css_class='input-xlarge'),
        Field('AffliateBrand2', css_class='input-xlarge'),
        Field('City', css_class='input-xlarge'),
        Field('Country', css_class='input-xlarge'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        ))
    helper.form_method = 'POST'

    class Meta:
        model = Events
        exclude = ("Id", )

