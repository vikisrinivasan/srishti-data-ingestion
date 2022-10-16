import django_tables2 as tables
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from ..models.utils.MasterData import City,Country,Platforms
# Create the form class.
from ..models.SocialMediaEnquiries import SocialMediaEnquiries

class SocialMediaEnquiriesForm(forms.ModelForm):
    YES_NO = ((True, 'Yes'), (False, 'No'))
    ReceivedDate=forms.DateField(widget=forms.DateInput(attrs={'class':'input-control','placeholder':"Request Date"}))
    Platform = forms.ChoiceField(
        choices=Platforms.choices,
        widget=forms.Select(attrs={'class':'input-control','placeholder':"Platform"})
    )
    ProfileURL=forms.URLField(widget=forms.URLInput(attrs={'class':'input-control','placeholder':"Profile URL Link"}))
    SocialProfile=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Social Profile"}))
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Name"}))
    EnquiryText=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Enquiry Text"}))
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
    ResponseDate=forms.DateField(widget=forms.DateInput(attrs={'class':'input-control','placeholder':"Response Date"}))
    Resolution=forms.BooleanField( widget=forms.RadioSelect(attrs={'class':'input-control','placeholder':"Have a Resolution or not"},choices=YES_NO))
    ResolvedFlag=forms.BooleanField( widget=forms.RadioSelect(attrs={'class':'input-control','placeholder':"Resolved or not"},choices=YES_NO))
    ProductsEnquired=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Products Enquired"}))
    ProductsSuggested=forms.CharField(widget=forms.TextInput(attrs={'class':'input-control','placeholder':"Products Suggested"}))

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('ReceivedDate', css_class='input-xlarge'),
        Field('Platform', css_class='input-xlarge'),
        Field('ProfileURL', css_class='input-xlarge'),
        Field('SocialProfile', css_class='input-xlarge'),
        Field('Name', css_class='input-xlarge'),
        Field('EnquiryText', css_class='col-md-6'),
        Field('Phone', css_class='col-md-6'),
        Field('Email', css_class='input-xlarge'),
        Field('City', css_class='input-xlarge'),
        Field('Country', css_class='input-xlarge'),
        Field('ResponseDate', css_class='input-xlarge'),
        Field('Resolution', css_class='input-xlarge'),
        Field('ResolvedFlag', css_class='input-xlarge'),
        Field('ProductsEnquired', css_class='input-xlarge'),
        Field('ProductsSuggested', css_class='input-xlarge'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        ))
    helper.form_method = 'POST'

    class Meta:
        model = SocialMediaEnquiries
        exclude = ("Id", )

