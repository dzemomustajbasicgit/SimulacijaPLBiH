from klub import Klub
from tabulate import tabulate
from utakmica import Utakmica
import time

class Liga():

    klubovi = []
    ukupan_broj_kola = 22

    def DodajKlub(self, klub : Klub):
        self.klubovi.append(klub)

    def NapraviRaspored(self):
        raspored = {}
        kopija = []
        for klub in self.klubovi:
            kopija.append(klub.ime)
        for i in range(len(kopija) - 1):
            mecevi_u_kolu = []
            for j in range(0, len(kopija) // 2):
                mec = (kopija[j], kopija[-(j + 1)])
                mecevi_u_kolu.append(mec)    
            raspored[i + 1] = mecevi_u_kolu
            kopija = [kopija[0]] + [kopija[-1]] + kopija[1:-1]  
        return raspored     
    
    def SimulirajSezonu(self):
        print("DOBRODOŠLI NA SIMULACIJU PREMIJER LIGE BOSNE I HERCEGOVINE!")
        time.sleep(2)
        klubovi = {}
        for klub in self.klubovi:
            klubovi[klub.ime] = klub
        for i in range(self.ukupan_broj_kola):
            izvjestaj = []
            trenutno_kolo = self.IgrajSljedeceKolo(i + 1, self.NapraviRaspored())
            for utakmica in trenutno_kolo:
                for tim in utakmica:
                    if i < 11:
                        mec = Utakmica(klubovi[utakmica[0]], klubovi[utakmica[1]])
                    else:
                        mec = Utakmica(klubovi[utakmica[1]], klubovi[utakmica[0]])
                    mec.StartUtakmice()
                    mec.IzvjestajSaUtakmice()
                    izvjestaj.append(mec)
                    break
            self.IzvjestajPoslijeOdigranogKola(izvjestaj, i + 1)    
            self.IspisiTabelu()
            self.DajListuStrijelaca()

    def IgrajSljedeceKolo(self, broj_kola, raspored):
        kopija = broj_kola
        for kolo, parovi in raspored.items():
            if broj_kola > 11:
                broj_kola -= 11
            if kolo == broj_kola:
                trenutno_kolo = parovi
        print(f"\nU {kopija}. kolu Premijer Lige Bosne i Hercegovine se sastaju: \n")
        for i in range(6):
            time.sleep(1)
            if kopija <= 11:
                print(f"{trenutno_kolo[i][0]} vs {trenutno_kolo[i][1]}")
            else:
                print(f"{trenutno_kolo[i][1]} vs {trenutno_kolo[i][0]}")    
        return trenutno_kolo        

    def IspisiTabelu(self):
        time.sleep(2)
        print(f"\nPoredak Premijer Lige BiH nakon {self.klubovi[0].broj_odigranih_utakmica}. kola:\n")
        time.sleep(2)
        tabela = []
        i = 1
        for klub in self.klubovi:
            tabela_klub = [klub.ime, klub.broj_odigranih_utakmica, klub.bodovi, klub.broj_pobjeda, klub.broj_nerijesenih, klub.broj_poraza, klub.broj_datih_golova, klub.broj_primljenih_golova, klub.broj_datih_golova - klub.broj_primljenih_golova]
            tabela.append(tabela_klub)
            i += 1

        sortirana_tabela = sorted(tabela, key=lambda bodovi : bodovi[2], reverse=True)
        #Dodajemo kolonu pozicije 1-12 nakon sortiranja
        i = 1
        for list in sortirana_tabela:
            list.insert(0, i)
            i += 1     

        kolone = ["Pos", "Ime kluba", "OS", "Bodovi", "W", "D", "L", "GD", "GP", "GD"]
        #Pravimo tabelu koja je sortirana po koloni 'Bodovi'    
        tabulate_tabela = tabulate(sortirana_tabela, headers=kolone, tablefmt="fancy_grid")

        print(tabulate_tabela)

    def IzvjestajPoslijeOdigranogKola(self, izvjestaj, broj_kola):
        time.sleep(2)
        print(f"\nZavršeno je {broj_kola}. kolo Premijer Lige BiH, a ovo su rezultati:\n")
        time.sleep(1)
        for utakmica in izvjestaj:
            time.sleep(1)
            print(f"{utakmica.domacin.ime} : {utakmica.gost.ime} {utakmica.domacin_golovi} : {utakmica.gost_golovi}")

    def DajListuStrijelaca(self):
        tabela = []
        time.sleep(2)
        print(f"\nLista najboljih strijelaca poslije {self.klubovi[0].broj_odigranih_utakmica}. kola: \n")
        time.sleep(2)
        for klub in self.klubovi:
            for igrac in klub.tim:
                if igrac.golovi > 0:
                    lista_strijelaca = [igrac.ime, igrac.pozicija, igrac.klub, igrac.golovi]
                    tabela.append(lista_strijelaca)   

        kolone = ["Ime", "Pozicija", "Klub", "Broj golova"]
        sortirana_tabela = sorted(tabela, key=lambda golovi : golovi[3], reverse=True)                  
        print(tabulate(sortirana_tabela, headers=kolone))

    def DajListuAsistenata(self):
        tabela = []
        print(f"\nLista najboljih asistenata poslije {self.klubovi[0].broj_odigranih_utakmica}. kola: \n")
        for klub in self.klubovi:
            for igrac in klub.tim:
                    if igrac.asistencije > 0:
                        lista_asistenata = [igrac.ime, igrac.pozicija, igrac.klub, igrac.asistencije]
                        tabela.append(lista_asistenata)   

        kolone = ["Ime", "Pozicija", "Klub", "Broj asistencija"]
        sortirana_tabela = sorted(tabela, key=lambda asistencije : asistencije[3], reverse=True)                  
        print(tabulate(sortirana_tabela, headers=kolone))

    def DajListuZutihKartona(self):
        pass

    def DajListuCrvenihKartona(self):
        pass

    def DajLideraPrvenstva(self):
        lista_bodova = []
        for klub in self.klubovi:
            tupless = (klub.ime, klub.bodovi)
            lista_bodova.append(tupless)    
        sortirana = sorted(lista_bodova, key=lambda bodovi: bodovi[1], reverse=True)
        print(f"\nLider prvenstva je {sortirana[0][0]} a imaju {sortirana[0][1]} bodova!")
    
    def DajNajboljegGolmana(self):
        lista_golmana = []
        for klub in self.klubovi:
            for igrac in klub.tim:
                if igrac.pozicija == 'GK':
                    tupless = (igrac.broj_primljenih_golova, igrac.ime)
                    lista_golmana.append(tupless)    
        sortirana = sorted(lista_golmana, key=lambda bodovi: bodovi[0])
        print(f"\nNajbolji golman prvenstva je {sortirana[0][1]} a primio je samo {sortirana[0][0]} golova!")



