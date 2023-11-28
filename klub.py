class Klub():

    def __init__(self, ime, stadion):
        self.ime = ime
        self.stadion = stadion
        self.tim = []
        self.broj_odigranih_utakmica = 0
        self.bodovi = 0
        self.broj_pobjeda = 0
        self.broj_poraza = 0
        self.broj_nerijesenih = 0
        self.broj_datih_golova = 0
        self.broj_primljenih_golova = 0  

    def DodajNovogIgraca(self, igrac):
        igrac.klub = self.ime
        self.tim.append(igrac)

    def DodajPobjedu(self, dati, primljeni):
        self.broj_odigranih_utakmica += 1
        self.broj_pobjeda += 1
        self.bodovi += 3
        self.broj_datih_golova += dati
        self.broj_primljenih_golova += primljeni

    def DodajNerijeseno(self, dati, primljeni):
        self.broj_odigranih_utakmica += 1
        self.broj_nerijesenih += 1
        self.bodovi += 1
        self.broj_datih_golova += dati
        self.broj_primljenih_golova += primljeni
        
    def DodajPoraz(self, dati, primljeni):
        self.broj_odigranih_utakmica += 1
        self.broj_poraza += 1
        self.broj_datih_golova += dati
        self.broj_primljenih_golova += primljeni

    def DajGolmana(self):
        return self.tim[0]

    def DajListuIgraca(self):
        return self.tim
    
    def DajImeStadiona(self):
        return self.stadion
    
                   

    
   