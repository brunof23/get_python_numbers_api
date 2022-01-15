import requests
import json



def get_numbers(page):

    r = requests.get(f'http://challenge.dienekes.com.br/api/numbers?page={page}')
            
    if r.status_code != 200:
         return False

    x = r.json()

    has_next = x['numbers']

    lista = has_next
            
    return lista
   




   
