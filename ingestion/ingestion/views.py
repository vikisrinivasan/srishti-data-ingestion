import json
from pathlib import Path

from django.core.files.storage import FileSystemStorage
from django.db import Error
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie
import pandas as pd
from formtools.wizard.views import SessionWizardView
import django_tables2 as tables
from .models.leads import Leads
from .models.contacts import Contacts
from django.template import loader, Context
import os
from .utils import clear_dir,save_json,read_json
global file_storage
def create_model(model_type,df,mapping_body):
    if model_type=='leads':
        create_leads(df,mapping_body)
    elif model_type=='contacts':

        create_contact(df,mapping_body)



def create_leads(df,mapping_dict):
    try:
        for index,row in df.iterrows():
            leads=Leads()
            for original_col, map_col in mapping_dict.items():
                if map_col not in ['Auto Generate','Unknown']:
                    setattr(leads, original_col, row[map_col])
                elif 'date' not in original_col and map_col=='Auto Generate':
                    raise "ONLY DATE FIELD CAN BE AUTO GENERATED , PLEASE CHANGE THE FIELD NAME"
            leads.save()
        return True
    except Exception as e:
        raise Error("Please check the mapping of fields")
    return False

def create_contact(df,mapping_dict):
    try:
        for index,row in df.iterrows():
            contact=Contacts()
            for original_col, map_col in mapping_dict.items():
                if map_col not in ['Auto Generate','Unknown']:
                    print(original_col,map_col)
                    setattr(contact, original_col, row[map_col])
                elif 'date' not in original_col and map_col=='Auto Generate':
                    raise "ONLY DATE FIELD CAN BE AUTO GENERATED , PLEASE CHANGE THE FIELD NAME"
            contact.save()
        return True
    except Exception as e:
        raise Error("Please check the mapping of fields")
    return False

def get_mapping_model_attr():
    models=['leads','contacts']
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
    print("done")
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
        if modeltype=='leads':
            original_cols=[(f.attname,f.help_text) for f in Leads._meta.concrete_fields if "_id" not in f.attname]
        elif modeltype=='contacts':
            original_cols=[(f.attname,f.help_text) for f in Contacts._meta.concrete_fields if "_id" not in f.attname]
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
        modeltype=mapping_body['modeltype']
        df=pd.read_csv(f"{data_path}/{filename}_{sheetname}.csv")

        original_cols=[col.strip().split("Description")[0].strip() for col in mapping_body['original_cols'] if col]
        mapping_cols=[col.strip() for col in mapping_body['mapped_cols'] if col]


        mapping_dict = dict(zip(original_cols,mapping_cols))
        filtered_df=df[[col for col in  mapping_cols if col not in ["Auto Generate","Unknown"]]]
        try:
            create_model(modeltype,filtered_df,mapping_dict)
        except Exception as e:
            return HttpResponse("Error: Please check the field Mappings before saving")
        return HttpResponse("Success: Mapping is saved successfully")


def edit_model_view(request):
    print("Hi")

class LeadsTableView(tables.SingleTableView):
    from .models.leads import Leads
    from .tables import LeadsTable
    import django
    print(django.apps.apps.get_models())
    model = Leads
    table_class = LeadsTable
    queryset = Leads.objects.all()
    template_name = "edit_menu.html"



