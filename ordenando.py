
def getOrdem(lista):
       

        j = len(lista)

        xordem = True
        while xordem:
                xordem = False
                i = 0
                j -= 1
                while i < j:
                        if lista[i] > lista[i + 1]:
                                lista[i], lista[i + 1] = \
        				lista[i + 1], lista[i]
                                xordem = True
                        i += 1
        return lista



     

              
