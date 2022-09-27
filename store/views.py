from django.shortcuts import render
from .models import Store
import requests
from bs4 import BeautifulSoup as bs
import plotly.express as px
import pandas as pd
import json
# Create your views here.
def home(request):

    all_grants= Store.objects.all()

    return render(request, 'home.html',{'product':all_grants})

def home_view(request):

    url='http://127.0.0.1:8000'

    page=requests.get(url).text

    soup = bs(page,'html.parser')

    grants=soup.find_all('div',class_='card')

    store_list=[]

    for i in range(len(grants)):
            product=grants[i-1].h5.text
            price=grants[i-1].div.find_all('ul')[0].text.split(':')[-1]
            quantity=grants[i-1].div.find_all('ul')[1].text.split(':')[-1]
        
            
            store_list.append([product,price,quantity])

    df=pd.DataFrame(store_list,columns=['Product','Price','Quantity'])
    df['Total'] = df['Price'].astype(int)*df['Quantity'].astype(int)
    df.loc[(df.index[-1] +1)] = ['Kenploy Mop Bucket', 460,1,
                                            460]
    df_july=df.iloc[1:47]
    df_june=df.iloc[47:df.index[-1]+1]
    df_june.loc[(df_june.index[-1] +1)] = ['', '','',
                                            df_june['Total'].sum()]
    df_july.loc[(df_july.index[-1] +1)] = ['', '','',
                                            df_july['Total'].sum()]
    json_thematic=df_june.reset_index().to_json(orient='records')
    data_thematic=[]
    data_thematic=json.loads(json_thematic)

    json_thematics=df_july.reset_index().to_json(orient='records')
    data_thematics=[]
    data_thematics=json.loads(json_thematics)



    return render(request, 'home_view.html',{'table':data_thematic,'july':data_thematics})


def dorcas(request):
    return render(request,'dorcas.html', {})