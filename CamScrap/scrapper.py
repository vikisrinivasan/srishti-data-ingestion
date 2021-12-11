from bs4 import  BeautifulSoup
import requests
import csv
from csv import DictWriter

brand = 'canon'
prodlisturl = 'https://www.dpreview.com/products/{brand}/cameras?subcategoryId=cameras&view=List&page={pageno}'


prods = []
def prodList(url,brand,iterations):
    for i in range(1,iterations):  # from page 1 to 7
        print('Page : {page}'.format(page = i))
        r = requests.get(url.format(brand = brand, pageno = i))
        page = BeautifulSoup(r.text, 'html.parser')
        divs = page.find_all(["div"], class_='name')
        for div in divs:
            try:
                prodname = div.a.text
                produrl = div.a['href']+'/specifications'
                export(prodname,produrl)
            except:
                pass



def export(prodname,produrl):
    r = requests.get(produrl)
    page = BeautifulSoup(r.text, 'html.parser')
    trs = page.find_all(["tr"])

    new_row = {'CameraName' : prodname , 'CameraSpecsUrl' : produrl  }
    fieldnames = ['CameraName','CameraSpecsUrl']
    for tr in trs:
        try:
            key = tr.th.string.strip()
            value = tr.td.text.strip()
            new_row[key] = value
            fieldnames.append(key)
            # print(tr.th.string.strip()+':'+ tr.td.text.strip())
        except:
            pass

    with open('cameras.csv', 'a', newline='',encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(new_row)

    new_row = {}
    fieldnames = []


prodList(prodlisturl,brand,8)