from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import pandas as pd

@ensure_csrf_cookie
def upload_files(request):
    if request.method == 'POST':
        files=request.FILES['file']
        df=pd.read_excel(files, index_col=0)
        print(df.head(10))

        return JsonResponse({'msg':'<span style="color: green;">File successfully uploaded</span>'})
    else:
        return render(request, 'files_upload.html', )