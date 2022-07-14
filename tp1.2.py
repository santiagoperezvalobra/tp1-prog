import string
import sys

def palabras_equivocadas(lista_palabras_equivocadas):
    contador = []
    with open("spanish.lst", "r+", encoding='utf-8') as diccionario:
        x=diccionario.read().split()
        for p in lista_palabras_equivocadas:
            if p not in x:
                contador.append(p)
    print(f"El texto contiene {len(contador)} {'palabra' if len(contador)==1 else 'palabras'} que no {'esta' if len(contador)==1 else 'estan'} en el diccionario.")
    return contador

def nuevas_palbras(contador):
    if len(contador)>0:
        for palabra in contador:
            eleccion=str(input(f"La palabra {palabra} no se encuentra en el diccionario.\n¿Qué desea hacer?\n 1. Agregarla al diccionario\n 2. Corregir palabra\n 3. Ignorar y seguir.\n"))
            while eleccion!="1"and eleccion!="2" and eleccion!="3":
                print("Comando invalido, trate otra vez.")
                eleccion=str(input(f"La palabra {palabra} no se encuentra en el diccionario.\n¿Qué desea hacer?\n 1. Agregarla al diccionario\n 2. Corregir palabra\n 3. Ignorar y seguir.\n"))
            if eleccion=="1":
                with open("spanish.lst", "a", encoding='utf-8') as diccionario:
                    diccionario.write(palabra)
            if eleccion=="2":
                nueva_plabra=input(f"Ingrese palabra para reemplazar {palabra}\n")
                with open("spanish.lst", "r+", encoding='utf-8') as diccionario:
                    x=diccionario.read().split()
                    if nueva_plabra not in x:
                        contador.append(nueva_plabra)
            if eleccion=="3":
                contador.remove(palabra)

def normalize(text_to_correct):
    replacements = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"))
    for a, b in replacements:
        text_to_correct = text_to_correct.replace(a, b)
    for x in list(string.punctuation):
        text_to_correct = text_to_correct.replace(x, " ")
    return text_to_correct

def modo_interactivo(Escribir):
    with open("newtext.txt", "w+", encoding='utf-8') as newtext:
        while Escribir != "@fin":  
            newtext.write(normalize(Escribir))
            newtext.write("\n")
            Escribir=input("Ingrese el texto hasta que llegue una línea con '@fin': ")
        if Escribir=="@fin":
            newtext.seek(0)
            print(f"Ha finalizado el ingreso de texto.")
            lista_a_normalize=newtext.read()
            text_to_correct=normalize(lista_a_normalize)
            newtext.seek(0)
            newtext.write(text_to_correct)
            newtext.seek(0)
            lista_palabras_equivocadas = newtext.read().split()
            contador= palabras_equivocadas(lista_palabras_equivocadas)
            nuevas_palbras(contador)
    return newtext, text_to_correct

def modo_archivo(eleccion):
    try:
        with open(f"{eleccion}", "r+", encoding='utf-8') as archivo:
            archivo=archivo.read().lower()
            text_to_normalize=normalize(archivo)
            lista_palabras_equivocadas=palabras_equivocadas(text_to_normalize)
            #print(lista_palabras_equivocadas)
            contador=nuevas_palbras(lista_palabras_equivocadas)
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")

print("¡Bienvenidx al TP1 del curso de programación!")

if len(sys.argv)>1:
    import sys
    eleccion=sys.argv[1]
    modo_archivo(eleccion)
if len(sys.argv)==1:
    print("Usted ha ingresado al modo interactivo.")
    Escribir=str(input("Ingrese su texto de pureba (escriba @fin para terminar): ").lower())
    modo_interactivo(Escribir)