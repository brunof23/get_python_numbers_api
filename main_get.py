import get_numbers
import recupera_pages
import ordenando

def getFullNumbers():

    pages = recupera_pages.get_pages()

    juntas = [] 

    lista_index = list(range(1,pages))

    for page in lista_index:

        todos = get_numbers.get_numbers(page)

        juntas.append(todos)
    
    lista_final = []

    for i in juntas:
        lista_final.extend(i)


    lista_ordenada = ordenando.getOrdem(lista_final)

    return  lista_ordenada
