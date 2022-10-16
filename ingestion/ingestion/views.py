import json
from pathlib import Path

from django.core.files.storage import FileSystemStorage
from django.db import Error
from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponsePermanentRedirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import pandas as pd
import django.apps


from formtools.wizard.views import SessionWizardView

from .filters.EventFilter import EventFilter
from .filters.EventRegistrationFilter import EventRegistrationFilter
from .filters.InfluencerFilter import InfluencerFilter
from .filters.InstitutionalClientsFilter import InstitutionalClientsFilter
from .filters.PhotographerLeadsFilter import PhotographerLeadsFilter
from .filters.ServiceRequestFilter import ServiceRequestFilter
from .filters.SocialMediaEnquiriesFilter import SocialMediaEnquiriesFilter
from .forms.EventsForm import EventForm
from .forms.EventsRegistrationForm import EventRegistrationForm
from .forms.InfluencerForm import InfluencerForm
from .forms.InstitutionalClientsForm import InstitutionalClientsForm
from .forms.PhotographerLeadsForm import PhotographerLeadsForm
from .forms.ServiceRequestForm import ServiceRequestForm
from .forms.SocialMediaEnquiriesForm import SocialMediaEnquiriesForm
from .tables.EventTables import EventTable
from .tables.EventsRegistration import EventRegistrationTable

from .models.EventRegistration import EventRegistration
from .models.Events import Events
from .models.Influencers import Influencers
from .models.InstitutionalClients import InstitutionalClients
from .models.PhotographerLeads import PhotographerLeads
from django.template import loader, Context, RequestContext
import os

from .models.ServiceRequest import ServiceRequests
from .models.SocialMediaEnquiries import SocialMediaEnquiries
from .tables.InfluencerTable import InfluencerTable
from .tables.InstitutionalClientTable import InstitutionalClientsTable
from .tables.PhotographerLeadsTable import PhotographerLeadsTable
from .tables.ServiceRequestTable import ServiceRequestTable
from .tables.SocialMediaEnquiriesTable import SocialMediaEnquiriesTable
from .utils import clear_dir,save_json,read_json,get_field_type
global file_storage

def generate_my_model_class(model_name):
    if model_name=='EventRegistration':
        return EventRegistration()
    elif model_name=='Events':
        return Events()
    elif model_name=='Influencers':
        return Influencers()
    elif model_name=='InstitutionalClients':
        return InstitutionalClients()
    elif model_name=='PhotographerLeads':
        return PhotographerLeads()
    elif model_name=='ServiceRequests':
        return ServiceRequests()
    else:
        return SocialMediaEnquiries()

def create_model(model_name,df,mapping_body):
    import django.apps
    models=django.apps.apps.get_models(include_auto_created=False, include_swapped=True)

    models=[model for model in models if model.__name__ not in ('LogEntry','Permission',
                                                                'Group','User',
                                                               'ContentType','Session')]
    df=df.loc[:,~df.columns.duplicated()]
    for model in models:
        if model.__name__==model_name:
            save_model(model,df,mapping_body)

def save_model(model,df,mapping_dict):
    try:
        for index,row in df.iterrows():
            model_class=generate_my_model_class(model.__name__)
            for original_col, map_col in mapping_dict.items():
                if map_col not in ['Auto Generate','Unknown']:
                    setattr(model_class, original_col, row[map_col])
            model_class.save()
        return True
    except Exception as e:
        raise Error("Please check the mapping of fields")

def get_mapping_model_attr():
    import django.apps
    models=django.apps.apps.get_models(include_auto_created=False, include_swapped=True)

    models=[model.__name__  for model in models if model.__name__ not in ('LogEntry','Permission',
                                                                          'Group','User',
                                                                          'ContentType','Session')]
    return models

def get_mapping_cols(files):
    mapping_columns=[]
    data_path=os.path.join(Path(__file__).resolve().parent, 'data')
    is_dir_cleared=clear_dir(data_path)
    if is_dir_cleared:
        for file_name,file in files.items():
            xls = pd.ExcelFile(file)
            sheets=list(xls.sheet_names)

            for sheet_name in sheets:
                df=pd.read_excel(file,sheet_name=sheet_name)

                if df.shape[0]>0:
                    df.columns=df.columns.str.lower()
                    df=df.loc[:,~df.columns.str.match("unnamed")]
                    if len(list(df.columns))>0:
                        raw_filename="leads_%s"%(file_name.replace(".xlsx","").replace(" ","_"))
                        saved_filename="%s_%s.csv"%(raw_filename,sheet_name)
                        df.to_csv("%s/%s"%(data_path,saved_filename))
                        mapping_columns.append({'filename':raw_filename,'sheetname':sheet_name,'columns':list(df.columns)})
    save_json(mapping_columns,"%s/%s"%(data_path,'mapping_cols'))
    return mapping_columns

@ensure_csrf_cookie
def get_sheet_model_selection(request):
    files=request.FILES
    mapping_cols=get_mapping_cols(files)
    original_cols=get_mapping_model_attr()
    html = render_to_string('data_mapping_selection.html', {'original_cols':original_cols,'mapping_columns': mapping_cols})
    return HttpResponse(html)

@ensure_csrf_cookie
def upload_files(request):
    if request.method == 'POST':
        return  get_sheet_model_selection(request)

@ensure_csrf_cookie
def render_mapping(request):

    if request.method == 'POST':
        mapping_request = request.body.decode('utf-8')
        mapping_body = json.loads(mapping_request)
        data_path=os.path.join(Path(__file__).resolve().parent, 'data')
        sheetname=mapping_body['sheetname']
        modeltype=mapping_body['modeltype']
        mapping_cols=read_json(f"{data_path}/mapping_cols.json")
        selected_mapping_cols=[]
        for mapping  in mapping_cols:
            if sheetname==mapping['sheetname']:
               selected_mapping_cols=[mapping]

        original_cols=[]

        models=django.apps.apps.get_models(include_auto_created=False, include_swapped=True)

        models=[model for model in models if model.__name__ not in ('LogEntry','Permission',
                                                                              'Group','User',
                                                                              'ContentType','Session')]
        for model in models:
            if model.__name__==modeltype:
                original_cols=[(f.attname,f.help_text) for f in model._meta.concrete_fields if "_id" not in f.attname]

        data_mapping_html = render_to_string('data_mapping.html', {'model_type':modeltype,'original_cols':original_cols,'mapping_columns': selected_mapping_cols})
        return HttpResponse(data_mapping_html)

@ensure_csrf_cookie
def save_mapping(request):
    if request.method == 'POST':
        mapping_request = request.body.decode('utf-8')
        mapping_body = json.loads(mapping_request)
        data_path=os.path.join(Path(__file__).resolve().parent, 'data')
        sheetname=mapping_body['sheetname']
        filename=mapping_body['filename']
        model_name=mapping_body['modeltype']
        df=pd.read_csv(f"{data_path}/{filename}_{sheetname}.csv")

        original_cols=[col.strip().split("Description")[0].strip() for col in mapping_body['original_cols'] if col]
        mapping_cols=[col.strip() for col in mapping_body['mapped_cols'] if col]

        mapping_dict = dict(zip(original_cols,mapping_cols))
        df.columns=df.columns.str.strip()
        # filtered_df=df[[col for col in  mapping_cols if col not in ["Auto Generate","Unknown"]]]


        errors=[]
        model=[model for model in django.apps.apps.get_models(include_auto_created=False, include_swapped=True) if model.__name__ == model_name]

        for org_col,map_col in mapping_dict.items():

            if org_col=='Id' and map_col!='Auto Generate':
                errors.append("Id Column Should be mapped to Auto Generate !!")
            if 'date' in org_col.lower() and map_col=='Unknown':
                errors.append(f"{org_col} column Should be mapped or assigned to Auto Generate !!")
            if map_col not in ['Auto Generate','Unknown']:
                field_type=get_field_type(df,map_col)
                if org_col!='Id' and model[0]._meta.get_field(org_col).__class__!=field_type:
                    errors.append(f"Please check the mapping column types for {org_col}!!")
        combined_errors=",".join(errors)
        if len(errors)<=0:
            filtered_df=df[[col for col in  mapping_cols if col not in ["Auto Generate","Unknown"]]]
            try:
                create_model(model_name,filtered_df,mapping_dict)
            except Exception as e:
                return HttpResponse("Error: Please check the field Mappings before saving")
            return HttpResponse("Success: Mapping is saved successfully")
        else:
            return HttpResponse(f"Errors: {combined_errors}")


def render_home(request):
    if request.user.is_authenticated:
        return  render(request, "home.html")
    else:
        return  HttpResponsePermanentRedirect("/accounts/")




@csrf_exempt
def render_models_table(request,model_name):

    models=django.apps.apps.get_models(include_auto_created=False, include_swapped=True)

    models=[model.__name__ for model in models if model.__name__ not in ('LogEntry','Permission',
                                                                         'Group','User',
                                                                         'ContentType','Session')]

    if model_name=='EventRegistration':
        filter = EventRegistrationFilter(request.GET, queryset=EventRegistration.objects.all())
        table = EventRegistrationTable(data=filter.qs)
    elif model_name=='Events':
        filter=EventFilter(request.GET,queryset=Events.objects.all())
        table=EventTable(data=filter.qs)
    elif model_name=='Influencers':
        filter=InfluencerFilter(request.GET,queryset=Influencers.objects.all())
        table=InfluencerTable(data=filter.qs)
    elif model_name=='InstitutionalClients':
        filter=InstitutionalClientsFilter(request.GET,queryset=InstitutionalClients.objects.all())
        table=InstitutionalClientsTable(data=filter.qs)
    elif model_name=='PhotographerLeads':
        filter=PhotographerLeadsFilter(request.GET,queryset=PhotographerLeads.objects.all())
        table=PhotographerLeadsTable(data=filter.qs)
    elif model_name=='ServiceRequests':
        filter=ServiceRequestFilter(request.GET,queryset=ServiceRequests.objects.all())
        table=ServiceRequestTable(data=filter.qs)
    elif model_name=='SocialMediaEnquiries':
        filter=SocialMediaEnquiriesFilter(request.GET,queryset=SocialMediaEnquiries.objects.all())
        table=SocialMediaEnquiriesTable(data=filter.qs)

    table.paginate(page=request.GET.get("page", 1), per_page=10)
    return render(request, "edit_menu.html", {
            "table": table,
            "filter":filter,
            "model_name":model_name,
            "models":models
        })

def delete_item(request,pk,model_name):
    print(model_name)
    if model_name=='EventRegistration':
        EventRegistration.objects.filter(Id=pk).delete()
        filter = EventRegistrationFilter(request.GET, queryset=EventRegistration.objects.all())
        table = EventRegistrationTable(data=filter.qs)
    elif model_name=='Events':
        Events.objects.filter(Id=pk).delete()
        filter=EventFilter(request.GET,queryset=Events.objects.all())
        table=EventTable(data=filter.qs)
    elif model_name=='Influencers':
        Influencers.objects.filter(Id=pk).delete()
        filter=InfluencerFilter(request.GET,queryset=Influencers.objects.all())
        table=InfluencerTable(data=filter.qs)
    elif model_name=='InstitutionalClients':
        InstitutionalClients.objects.filter(Id=pk).delete()
        filter=InstitutionalClientsFilter(request.GET,queryset=InstitutionalClients.objects.all())
        table=InstitutionalClientsTable(data=filter.qs)
    elif model_name=='PhotographerLeads':
        PhotographerLeads.objects.filter(lead_id=pk).delete()
        filter=PhotographerLeadsFilter(request.GET,queryset=PhotographerLeads.objects.all())
        table=PhotographerLeadsTable(data=filter.qs)
    elif model_name=='ServiceRequests':
        ServiceRequests.objects.filter(RequestID=pk).delete()
        filter=ServiceRequestFilter(request.GET,queryset=ServiceRequests.objects.all())
        table=ServiceRequestTable(data=filter.qs)
    elif model_name=='SocialMediaEnquiries':
        SocialMediaEnquiries.objects.filter(EnquiryID=pk).delete()
        filter=SocialMediaEnquiriesFilter(request.GET,queryset=SocialMediaEnquiries.objects.all())
        table=SocialMediaEnquiriesTable(data=filter.qs)

    models=django.apps.apps.get_models(include_auto_created=False, include_swapped=True)
    models=[model.__name__ for model in models if model.__name__ not in ('LogEntry','Permission',
                                                                         'Group','User',
                                                                         'ContentType','Session')]
    table.paginate(page=request.GET.get("page", 1), per_page=10)
    return render(request, "edit_menu.html", {
        "table": table,
        "filter":filter,
        "model_name":model_name,
        "models":models
    })
@csrf_exempt
def add_item(request,model_name):
     if request.method == 'POST':
            post_data =request.POST.dict()
            del post_data['csrfmiddlewaretoken']
            request.POST._mutable = True
            models=django.apps.apps.get_models(include_auto_created=False, include_swapped=True)
            models=[model.__name__ for model in models if model.__name__ not in ('LogEntry','Permission',
                                                                         'Group','User',
                                                                         'ContentType','Session')]
            if model_name=='EventRegistration':
                # print(request.POST)
                event=EventRegistration(**post_data)
                event.save()
                filter = EventRegistrationFilter(request.GET, queryset=EventRegistration.objects.all())
                table = EventRegistrationTable(data=filter.qs)
            elif model_name=='Events':
                event=Events(**post_data)
                event.save()
                filter=EventFilter(request.GET,queryset=Events.objects.all())
                table=EventTable(data=filter.qs)
            elif model_name=='Influencers':
                event=Influencers(**post_data)
                event.save()
                filter=InfluencerFilter(request.GET,queryset=Influencers.objects.all())
                table=InfluencerTable(data=filter.qs)
            elif model_name=='InstitutionalClients':
                event=InstitutionalClients(**post_data)
                event.save()
                filter=InstitutionalClientsFilter(request.GET,queryset=InstitutionalClients.objects.all())
                table=InstitutionalClientsTable(data=filter.qs)
            elif model_name=='PhotographerLeads':
                event=PhotographerLeads(**post_data)
                event.save()
                filter=PhotographerLeadsFilter(request.GET,queryset=PhotographerLeads.objects.all())
                table=PhotographerLeadsTable(data=filter.qs)
            elif model_name=='ServiceRequests':
                event=ServiceRequests(**post_data)
                event.save()
                filter=ServiceRequestFilter(request.GET,queryset=ServiceRequests.objects.all())
                table=ServiceRequestTable(data=filter.qs)
            elif model_name=='SocialMediaEnquiries':
                event=SocialMediaEnquiries(**post_data)
                event.save()
                filter=SocialMediaEnquiriesFilter(request.GET,queryset=SocialMediaEnquiries.objects.all())
                table=SocialMediaEnquiriesTable(data=filter.qs)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            return render(request, "edit_menu.html", {
                "table": table,
                "filter":filter,
                "model_name":model_name,
                "models":models
            })
     if model_name=='EventRegistration':
         form=EventRegistrationForm()
         return render(request, "edit_template.html", {"form": form})
     elif model_name=='Events':
         form=EventForm()
         return render(request, "edit_template.html", {"form": form})
     elif model_name=='Influencers':
         form=InfluencerForm()
         return render(request, "edit_template.html", {"form": form})
     elif model_name=='InstitutionalClients':
         form=InstitutionalClientsForm()
         return render(request, "edit_template.html", {"form": form})
     elif model_name=='PhotographerLeads':
         form=PhotographerLeadsForm()
         return render(request, "edit_template.html", {"form": form})
     elif model_name=='ServiceRequests':
         form=ServiceRequestForm()
         return render(request, "edit_template.html", {"form": form})
     elif model_name=='SocialMediaEnquiries':
         form=SocialMediaEnquiriesForm()
         return render(request, "edit_template.html", {"form": form})




