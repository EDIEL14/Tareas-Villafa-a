def comparar(a, b):
    if a > b:
        return "mayor"
    elif a < b:
        return "menor"
    else:
        return "igual"
    
    def pedir_mano():
        a = input("¿Quieres casarte conmigo?")
        if(a == 'si'):
            return 'yeah'
        else:
            return 'triste'