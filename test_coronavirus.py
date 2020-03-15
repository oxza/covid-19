import os, time, msvcrt

coronavirus = 0
gripe = 0
resfriado = 0

os.system("cls")
print("Te formularé varias preguntas. Debes responderlas con total sinceridad.")
time.sleep(3)
print("\nSi la respuesta es positiva, escribe SOLO una 'Y'.")
time.sleep(2)
print("Si la respuesta es negativa, entonces escribe una 'N'.")
time.sleep(5)
os.system("cls")
print("Si desconoces la respuesta, simplemente presiona la tecla 'enter'.")
time.sleep(4)
os.system("cls")
print("¿Listo?")
time.sleep(2)
print("Presiona cualquier tecla para comenzar el test!")
msvcrt.getch()
os.system("cls")

print("¿Tienes fiebre?")
fiebre = input("Introduce tu respuesta: ")
if fiebre == "Y":
    coronavirus = 3
    gripe = 2
    resfriado = -2
elif fiebre == "N":
    gripe = -1
    resfriado = 1
else:
    pass
os.system("cls")

print("¿Tienes tos?")
tos = input("Introduce tu respuesta: ")
if tos == "Y":
    coronavirus = coronavirus + 2
    gripe = gripe + 2
    resfriado = resfriado + 3
elif tos == "N":
    coronavirus = coronavirus - 1
    gripe = gripe - 1
    resfriado = resfriado - 2
else:
    pass
os.system("cls")

print("¿Tienes mocos?")
mocos = input("Introduce tu respuesta: ")
if mocos == "Y":
    coronavirus = coronavirus - 3
    gripe = gripe + 2
    resfriado = resfriado - 1
elif mocos == "N":
    coronavirus = coronavirus + 1
    gripe = gripe - 1
    resfriado = resfriado + 1
else:
    pass
os.system("cls")

print("¿Tienes congestión nasal?")
c_nasal = input("Introduce tu respuesta: ")
if c_nasal == "Y":
    coronavirus = coronavirus - 1
    gripe = gripe - 1
    resfriado = resfriado + 1
elif c_nasal == "N":
    coronavirus = coronavirus + 1
    gripe = gripe + 1
    resfriado = resfriado - 1
else:
    pass
os.system("cls")

print("¿Sueles estornudar?")
est = input("Introduce tu respuesta: ")
if est == "Y":
    coronavirus = coronavirus - 3
    gripe = gripe + 2
    resfriado = resfriado + 2
elif est == "N":
    gripe = gripe - 1
    resfriado = resfriado - 1
else:
    pass
os.system("cls")

print("¿Te duele o sientes un malestar en la garganta?")
grg = input("Introduce tu respuesta: ")
if grg == "Y":
    resfriado = resfriado + 1
else:
    pass
os.system("cls")

print("¿Tienes dificultad al respirar?")
no_respirar = input("Introduce tu respuesta: ")
if no_respirar == "Y":
    coronavirus = coronavirus + 3
    gripe = gripe + 1
    resfriado = resfriado - 1
elif no_respirar == "N":
    coronavirus = coronavirus - 1
else:
    pass
os.system("cls")

print("¿Tienes flema?")
flema = input("Introduce tu respuesta: ")
if flema == "Y":
    coronavirus = coronavirus + 1
    gripe = gripe + 1
    resfriado = resfriado + 1
    os.system("cls")
    print("¿La flema es de color amarillo o verde? Y/N")
    color_flema = input("Introduce tu respuesta: ")
    if color_flema == "Y":
        coronavirus = coronavirus + 2
        gripe = gripe + 1
        resfriado = resfriado + 1
    elif color_flema == "N":
        coronavirus = coronavirus - 2
        gripe = gripe + 1
        resfriado = resfriado + 1
    else:
        pass
# creado por Omar
else:
    pass
os.system("cls")

print("¿Has vomitado o sentido ganas de vomitar?")
vm = input("Introduce tu respuesta: ")
if vm == "Y":
    coronavirus = coronavirus - 2
    gripe = gripe + 2
    resfriado = resfriado - 3
elif vm == "N":
    gripe = gripe - 2
else:
    pass
os.system("cls")

print("¿Tienes diarrea?")
drr = input("Introduce tu respuesta: ")
if drr == "Y":
    coronavirus = coronavirus - 1
    gripe = gripe + 2
    resfriado = resfriado - 3
elif drr == "N":
    gripe = gripe - 2
else:
    pass
os.system("cls")

print("¿Te sientes mental o físicamente más cansado de lo habitual?")
cn = input("Introduce tu respuesta: ")
if cn == "Y":
    coronavirus = coronavirus + 2
    gripe = gripe + 1
    resfriado = float(resfriado) + 0.5
elif cn == "N":
    coronavirus = coronavirus - 1
    resfriado = float(resfriado) - 0.5
else:
    pass

coronavirus = float(coronavirus)
gripe = float(gripe)
resfriado = float(resfriado)

os.system("cls")
print("Cargando los resultados (\)")
time.sleep(1)
os.system("cls")
print("Cargando los resultados (|)")
time.sleep(1)
os.system("cls")
print("Cargando los resultados (/)")
time.sleep(1)
os.system("cls")
print("Cargando los resultados (\)")
time.sleep(1)
os.system("cls")
print("Cargando los resultados (|)")
time.sleep(1)
os.system("cls")
print("Cargando los resultados (/)")
time.sleep(2)
os.system("cls")

print("Atención: el diagnóstico puede no ser fiable. El mejor diagnóstico siempre es el de un profesional.")
time.sleep(4)
print("\nSi tienes una tos constante y/o dificultad para respirar QUÉDATE EN CASA. No es peligroso para gente joven,\npero puedes salvar muchas vidas de gente anciana o con problemas de salud, solo por precaución.")
time.sleep(7)
os.system("cls")
print("Presiona cualquier tecla para ver los resultados.")
msvcrt.getch()
os.system("cls")
time.sleep(1)

if coronavirus > gripe and coronavirus > resfriado:
    print("Los síntomas indican que lo más probable es que tengas el COVID-19.")
    print("Quédate en casa. No salgas bajo ninguna excepción.")
    time.sleep(2)
elif coronavirus < resfriado and coronavirus > gripe:
    print("Todo parece indicar que tienes un simple resfriado. De todos modos, por precaución,\nquédate en casa a menos que tengas una urgencia o tengas que ir a comprar.")
elif coronavirus == resfriado and gripe < resfriado:
        print("Hay exactamente las mismas probabilidades de que tengas tanto el coronavirus como un resfriado.")
elif gripe > coronavirus and gripe > resfriado:
    print("Todo parece indicar que tienes la gripe. De todos modos, por precaución,\nquédate en casa a menos que tengas una urgencia o tengas que ir a comprar.")
elif gripe > coronavirus and gripe < resfriado:
    print("Todo parece indicar que tienes un simple resfriado. De todos modos, por precaución,\nquédate en casa a menos que tengas una urgencia o tengas que ir a comprar.")
elif resfriado == gripe and coronavirus < resfriado:
     print("Hay exactamente las mismas probabilidades de que tengas tanto un resfriado como la gripe, es poco probable que tengas el COVID-19.")
elif resfriado > gripe and resfriado > coronavirus:
    print("Todo parece indicar que tienes un simple resfriado. De todos modos, por precaución,\nquédate en casa a menos que tengas una urgencia o tengas que ir a comprar.")
elif resfriado > gripe and resfriado < coronavirus:
    print("Los síntomas indican que lo más probable es que tengas el COVID-19.")
    print("Quédate en casa. No salgas bajo ninguna excepción.")
else:
    print("No se ha podido determinar la enfermedad más probable en base a la información dada.")
time.sleep(2)
print("\nSi crees que tus síntomas son graves o corres peligro, llama de inmediato al 112.")
time.sleep(3)
print("\nPuedes encontrar más información acerca del nuevo coronavirus en https://www.who.int/es/emergencies/diseases/novel-coronavirus-2019.\n\n\n\n\n")
time.sleep(8)