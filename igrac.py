class Igrac():

    def __init__(self, ime, broj_godina, pozicija, klub):
        self.ime = ime
        self.broj_godina = broj_godina
        self.pozicija = pozicija
        self.klub = klub 
        self.golovi = 0
        self.asistencije = 0
        self.zuti_kartoni = 0
        self.crveni_kartoni = 0
    
class Golman(Igrac):

    def __init__(self, ime, broj_godina, pozicija, klub):
        super().__init__(ime, broj_godina, pozicija, klub)
        self.broj_primljenih_golova = 0
        self.cleansheets = 0
        self.odbranjeni_penali = 0