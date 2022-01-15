import requests
import json

def get_pages():
    page = 1
    while True:
        print ('página',page)
        r = requests.get(f'http://challenge.dienekes.com.br/api/numbers?page={page}')

        
        if r.status_code != 200:
            break

        x = r.json()

        has_next = x['numbers']


        qtd = has_next

        if page == 25 or not has_next:
            break        
        page = page + 1 
       

    return page
