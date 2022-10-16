import os
import glob
import shutil

from django.db.models.fields import CharField, IntegerField,DateField
from pandas.core.dtypes.common import is_string_dtype, is_numeric_dtype, is_datetime64_any_dtype


def get_field_type(df,col):
   if  is_string_dtype(df[col]):
       return CharField
   elif is_numeric_dtype(df[col]):
       return IntegerField
   elif is_datetime64_any_dtype(df[col]):
       return DateField


def clear_dir(dir_path):
    try:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
        os.makedirs(dir_path)
        return True
    except Exception as e:
        raise "Please Check the Directory"

def save_json(json_obj,filename):
    import json
    out_file = open("%s.json"%filename, "w")
    json.dump(json_obj, out_file)
    out_file.close()


def read_json(path):
    import json
    out_file = open(path)
    data = json.load(out_file)
    out_file.close()
    return data