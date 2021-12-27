import json
from pathlib import Path

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie
import pandas as pd
from .models.leads import Leads
from .models.contacts import Contacts
from django.template import loader, Context
import os
from .utils import clear_dir
# def create_contact(df,mapping_body):
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
        raise "Please check the fields"
    return False

def create_contact(df,mapping_dict):
    try:
        for index,row in df.iterrows():
            contact=Contacts()
            for original_col, map_col in mapping_dict.items():
                if map_col not in ['Auto Generate','Unknown']:
                    setattr(contact, original_col, row[map_col])
                elif 'date' not in original_col and map_col=='Auto Generate':
                    raise "ONLY DATE FIELD CAN BE AUTO GENERATED , PLEASE CHANGE THE FIELD NAME"
            contact.save()
        return True
    except Exception as e:
        raise "Please check the fields"
    return False

@ensure_csrf_cookie
def upload_files(request):
    if request.method == 'POST':
        files=request.FILES
        type=request.POST['type']
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
                            saved_filename="leads_%s_%s.csv"%(file_name.replace(".xlsx","").replace(" ","_"),sheet_name)
                            df.to_csv("%s/%s"%(data_path,saved_filename))

                            mapping_columns.append({'filename':saved_filename,'sheetname':sheet_name,'columns':list(df.columns)})
        original_cols=[]
        if type in ['Leads-ID','Leads-RD']:
            original_cols={'leads':[(f.attname,f.help_text) for f in Leads._meta.concrete_fields if "_id" not in f.attname],
                            'contacts':[(f.attname,f.help_text) for f in Contacts._meta.concrete_fields if "_id" not in f.attname]}

        html = render_to_string('data_mapping.html', {'active':'leads','type':type,'original_cols':original_cols,'mapping_columns': mapping_columns})
        return HttpResponse(html)
    else:
        return render(request, 'files_upload.html')

@ensure_csrf_cookie
def save_files(request):
    if request.method == 'POST':
        mapping_request = request.body.decode('utf-8')
        mapping_body = json.loads(mapping_request)

        data_path=os.path.join(Path(__file__).resolve().parent, 'data')
        sheetname=mapping_body['sheetname']
        filename=mapping_body['filename']
        modeltype=mapping_body['modeltype']
        original_cols=[col.strip().split("Description")[0].strip() for col in mapping_body['original_cols'] if col]
        mapping_cols=[col.strip() for col in mapping_body['mapped_cols'] if col]
        mapping_dict = dict(zip(original_cols,mapping_cols))
        df=pd.read_csv(f"{data_path}/{filename}")
        if mapping_body['type']=='Leads-ID':
            if modeltype=='leads':

                print(original_cols)
                filtered_df=df[[col for col in  mapping_cols if col not in ["Auto Generate","Unknown"]]]
                create_leads(filtered_df,mapping_dict)
            elif modeltype=='contacts':
                filtered_df=df[[col for col in  mapping_cols if col not in ["Auto Generate","Unknown"]]]
                create_contacts(filtered_df,mapping_dict)






           #leads_loaded=pd.read_csv('%s/leads.csv'%(data_path))
           #create_leads(leads_loaded,mapping_body)
           # print(leads_loaded.head(10))
