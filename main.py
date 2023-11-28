from igrac import Igrac, Golman
from klub import Klub
from liga import Liga
from data import lista_klubova, dict_igraci, lista_stadiona

klubovi = {}
i = 0

for klub in lista_klubova: #Kreiramo dictionary ime kluba : objekat Klub
    klubovi[klub] = Klub(klub, lista_stadiona[i])
    i += 1
    
igraci = {}

for igrac, info in dict_igraci.items(): #Kreiramo dictionary ime igraca : objekat Igrac
    if info[1] != "GK":
        igraci[igrac] = Igrac(igrac, info[0], info[1], info[2])
    else:
        igraci[igrac] = Golman(igrac, info[0], info[1], info[2])
        
for igrac, objekat_igrac in igraci.items(): #Ubacujemo svakog igrača u klub za koji nastupa
    for klub, objekat_klub in klubovi.items():
        if objekat_igrac.klub == objekat_klub.ime:
            objekat_klub.DodajNovogIgraca(objekat_igrac)
            
bhliga = Liga()#Kreiramo BH Premijer Ligu

for ime, klub in klubovi.items():#Ubacujemo klubove u ligu
    bhliga.DodajKlub(klub)

#Simulacija sezone
bhliga.SimulirajSezonu()



    

                                        







