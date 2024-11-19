
#ESERCIZIO 2B

m=int(input("Inserire (1), se si vuole fare la media in centesimi, inserire (2) se si vuole calcolare la media in decimi"))
v1=int(input("Inserire il primo voto: "))
v2=int(input("Inserire il secondo voto: "))
v3=int(input("Inserire il terzo voto: "))
if(m==1):
    m=v1+v2+v3*100/30
    print("La media in centesimi sarà di: ",m)
else:
    m=v1+v2+v3/3
    print("La media in decimi sarà di: ",m)




#ESERCIZIO 3B

l1=float(input("Inserisci la distanza del primo lancio: "))
l2=float(input("Inserisci la distanza del secondo lancio: "))
l3=float(input("Inserisci la distanza del terzo lancio: "))
l4=float(input("Inserisci la distanza del quarto lancio: "))
l5=float(input("Inserisci la distanza del quinto lancio: "))
i=5
if(l1==0 and l2==0 and l3==0 and l4==0 and l5==0):
    print("Tutti i lanci sono nulli")
if(l1==0):
    i=i-1
if(l2==0):
    i=i-1
if(l3==0):
    i=i-1
if(l4==0):
    i=i-1
if(l5==0):
    i=i-1
    m=l1+l2+l3+l4+l5/i



