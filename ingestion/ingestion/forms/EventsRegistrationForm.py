import django_tables2 as tables
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from ..models.utils.MasterData import City,Country
# Create the form class.
from ..models.EventRegistration import EventRegistration

class EventRegistrationForm(forms.ModelForm):
    YES_NO = ((True, 'Yes'), (False, 'No'))
    Date=forms.DateField(widget=forms.DateInput(attrs={'class':'input-control','placeholder':"Date"}))
    EventName=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Event Name"}))
    EventDate=forms.DateField( widget=forms.DateInput(attrs={'class':'input-control','placeholder':"Event Date"}))
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Event Attender Name"}))
    Pro=forms.BooleanField(widget=forms.RadioSelect(attrs={'class':'input-control','placeholder':"Event Attender Name"},choices=YES_NO))
    Youtube=forms.URLField(widget=forms.URLInput(attrs={'class':'input-control','placeholder':"Youtube Link"}))
    Instagram=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Instagram Link"}))
    Snapchat=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Snapchat Link"}))
    Facebook=forms.URLField(widget=forms.URLInput(attrs={'class':'input-control','placeholder':"Facebook Link"}))
    Twitter=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Twitter Link"}))
    LinkedIn=forms.URLField(widget=forms.URLInput(attrs={'class':'input-control','placeholder':"Linkedin Link"}))
    Phone=forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Home Phone Number"}))
    Phone1=forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Office Phone Number"}))
    Phone2=forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Mobile Number"}))
    Email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-control','placeholder':"Primary Email ID"}))
    Email1=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-control','placeholder':"Secondary Email ID"}))
    Email2=forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-control','placeholder':"Email ID 3"}))
    City = forms.ChoiceField(
        choices=City.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"City"})
    )
    Country = forms.ChoiceField(
        choices=Country.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"Country"})
    )
    PermissionToShareData=forms.BooleanField( widget=forms.RadioSelect(attrs={'class':'input-control','placeholder':"Permission To Give Data"},choices=YES_NO))
    Photographer=forms.BooleanField(widget=forms.RadioSelect(attrs={'class':'input-control','placeholder':"Profession Protographer or Not"},choices=YES_NO))
    GenreTags=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Genre"}))
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('Date', css_class='input-xlarge'),
        Field('EventName', css_class='input-xlarge'),
        Field('EventDate', css_class='input-xlarge'),
        Field('Name', css_class='input-xlarge'),
        Field('Pro', style="background: #FAFAFA; padding: 10px;"),
        Field('Youtube', css_class='input-xlarge'),
        Field('Instagram', css_class='input-xlarge'),
        Field('Snapchat', css_class='input-xlarge'),
        Field('Facebook',css_class='input-xlarge'),
        Field('Twitter', css_class='input-xlarge'),
        Field('LinkedIn', css_class='input-xlarge'),
        Field('Phone', css_class='input-xlarge'),
        Field('Phone1', css_class='input-xlarge'),
        Field('Phone2', css_class='input-xlarge'),
        Field('Email', css_class='input-xlarge'),
        Field('Email1', css_class='input-xlarge'),
        Field('Email2'),
        Field('City', css_class='col-md-6'),
        Field('Country', css_class='col-md-6'),
        Field('PermissionToShareData', css_class='input-xlarge'),
        Field('Photographer', css_class='input-xlarge'),
        Field('GenreTags', css_class='input-xlarge'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        ))
    helper.form_method = 'POST'

    class Meta:
        model = EventRegistration
        exclude = ("Id", )

