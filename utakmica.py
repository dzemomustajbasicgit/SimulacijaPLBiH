import random
import time
from igrac import Golman

def IndexIgracaGol():
    broj = random.randint(1, 100)
    if broj == 1:
        return 0 #Vracamo index golmana
    elif broj > 1 and broj < 16:
        defanzivac = random.randint(1, 4)
        return defanzivac
    elif broj >= 16 and broj < 45:
        veznjak = random.randint(5, 7)
        return veznjak
    else:
        napadac = random.randint(8, 10)
        return napadac
    
def IndexIgracaAsistencija():
    broj = random.randint(1, 100)
    if broj == 1:
        return 0
    elif broj > 1 and broj <= 20:
        defanzivac = random.randint(1, 4)
        return defanzivac
    elif broj > 20 and broj <= 55:
        veznjak = random.randint(5, 7)
        return veznjak
    else:
        napadac = random.randint(8, 10)
        return napadac
    
class Utakmica():

    def __init__(self, domacin, gost):

        self.domacin = domacin
        self.gost = gost
        self.domacin_golovi = 0
        self.gost_golovi = 0
        self.zuti_kartoni = []
        self.strijelci = []

    def Gol(self, minuta):

        gol = random.randint(1,180)

        if gol == 50 or gol == 100 or gol == 125:
            index_gol = IndexIgracaGol()
            index_asistencija = IndexIgracaAsistencija()
            while index_gol == index_asistencija:
                index_asistencija = IndexIgracaAsistencija()
            igrac_koji_je_zabio = self.domacin.tim[index_gol]
            igrac_koji_je_zabio.golovi += 1
            self.domacin.tim[index_asistencija].asistencije += 1
            self.domacin_golovi += 1
            self.gost.tim[0].broj_primljenih_golova += 1
            self.strijelci.append(igrac_koji_je_zabio)
            print(f"\n{minuta}' - GOOOOOOOOOOOL! {self.domacin.ime} : {self.gost.ime} {self.domacin_golovi} : {self.gost_golovi}\nGol je postigao {igrac_koji_je_zabio.ime} a asistenciju je upisao {self.domacin.tim[index_asistencija].ime}!!")
            return True
        elif gol == 60 or gol == 130:
            index_gol = IndexIgracaGol()
            index_asistencija = IndexIgracaAsistencija()
            while index_gol == index_asistencija:
                index_asistencija = IndexIgracaAsistencija()
            igrac_koji_je_zabio = self.gost.tim[index_gol]
            igrac_koji_je_zabio.golovi += 1
            self.gost.tim[index_asistencija].asistencije += 1
            self.gost_golovi += 1
            self.domacin.tim[0].broj_primljenih_golova += 1
            self.strijelci.append(igrac_koji_je_zabio)
            print(f"\n{minuta}' - GOOOOOOOOOOOL! {self.domacin.ime} : {self.gost.ime} {self.domacin_golovi} : {self.gost_golovi}\nGol je postigao {igrac_koji_je_zabio.ime} a asistenciju je upisao {self.gost.tim[index_asistencija].ime}!!")
            return True
        else:
            return False
            
        
    def ZutiKarton(self, minuta):

        zuti_karton = random.randint(1,75)
        
        if zuti_karton == 50:
            zuti = random.choice([self.domacin, self.gost])
            igrac_koji_je_dobio_zuti = random.choice(zuti.tim)
            igrac_koji_je_dobio_zuti.zuti_kartoni += 1
            self.zuti_kartoni.append(igrac_koji_je_dobio_zuti)
            print(f"\n{minuta}' - {igrac_koji_je_dobio_zuti.ime}[{zuti.ime}] je dobio žuti karton!")
            return True
        else:
            return False
        
    def CrveniKarton(self):
        pass 
        
    def StartUtakmice(self):
        time.sleep(2)
        print(f"\nUskoro počinje meč {self.domacin.ime} - {self.gost.ime} na stadionu {self.domacin.stadion}!")
        time.sleep(2)
        print(f"\nDomaća momčad izlazi u sastavu:\n")
        time.sleep(2)
        for igrac in self.domacin.tim:
            print(igrac.ime)
            time.sleep(1)
        time.sleep(2)
        print(f"\nGostujuća momčad izlazi u sastavu:\n")
        time.sleep(2)
        for igrac in self.gost.tim:
            print(igrac.ime)
            time.sleep(1)
        time.sleep(2)
        print("\nMeč je počeo!")        
        for minuta in range(1, 91):
            time.sleep(1)
            self.Gol(minuta)
            self.ZutiKarton(minuta)
            if minuta == 45:
                print(f"\nPrvo poluvrijeme je završeno rezultatom: {self.domacin.ime} : {self.gost.ime} {self.domacin_golovi} : {self.gost_golovi}")
                time.sleep(1)
                print("\nPauza od 15 min je u toku!")
                time.sleep(5)
                print("\nPočelo je drugo poluvrijeme!")

    def IzvjestajSaUtakmice(self):
        time.sleep(2)
        print(f"\nUtakmica je završila. {self.domacin.ime} : {self.gost.ime} {self.domacin_golovi} : {self.gost_golovi}")
        time.sleep(2)
        if self.domacin_golovi > self.gost_golovi:
            if self.gost_golovi == 0:
                self.domacin.tim[0].cleansheets += 1
            self.domacin.DodajPobjedu(self.domacin_golovi, self.gost_golovi)
            self.gost.DodajPoraz(self.gost_golovi, self.domacin_golovi)
        elif self.domacin_golovi < self.gost_golovi:
            if self.domacin_golovi == 0:
                self.gost.tim[0].cleansheets += 1
            self.domacin.DodajPoraz(self.domacin_golovi, self.gost_golovi)
            self.gost.DodajPobjedu(self.gost_golovi, self.domacin_golovi)
        else:
            if self.domacin_golovi == 0:
                self.domacin.tim[0].cleansheets += 1
                self.gost.tim[0].cleansheets += 1
            self.domacin.DodajNerijeseno(self.domacin_golovi, self.gost_golovi)
            self.gost.DodajNerijeseno(self.gost_golovi, self.domacin_golovi)
        if len(self.strijelci) > 0:
            print(f"\nGolove su postigli: \n")
            for igrac in self.strijelci:
                time.sleep(1)
                print(f"{igrac.ime}")
        if len(self.zuti_kartoni) > 0:
            print(f"\nŽute kartone su dobili:\n")
            for igrac in self.zuti_kartoni:
                time.sleep(1)
                print(f"{igrac.ime}")
                
           
