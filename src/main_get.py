from src.get_numbers import get_numbers as get
import src.recupera_pages as recupera_pages
import src.ordenando as ordenando

def getFullNumbers():

    pages = recupera_pages.get_pages()

    juntas = [] 

    lista_index = list(range(1,pages))

    for page in lista_index:

        todos = get(page)

        juntas.append(todos)
    
    lista_final = []

    for i in juntas:
        lista_final.extend(i)


    lista_ordenada = ordenando.getOrdem(lista_final)

    return  lista_ordenada
