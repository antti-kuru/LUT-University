######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Antti Kuru    
# Opiskelijanumero: 614321
# Päivämäärä: 20.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPeruskirjasto.py
# eof
import sys # Lisätään sys kirjasto poikkeustenkäsittelyä varten.
import datetime # Lisätään datetime kirjasto päivämäärien käsittelyä varten.

EROTIN = ";"

class TIEDOT: # Luodaan luokka luettavia tietoja varten. Tiedostossa on päivämääriä ja eri kellonaikoja vastaavia hintoja. Tallennetaan siis hinta ja sitä vastaava aikaleima tähän oliona tämän luokan perusteella.
    aikaleima = None
    hinta = None

class VIIKONPVTULOKSET: # Luodaan luokka valinnan 4 viikonpäiväanalyysiä varten. Tämä helpottaa yhdistämään viikonpäivän, ja apulistoista sitä vastaavan summan ja alkoiden lukumäärän. Tämän avulla saadaan tehtyä lopullinen tulosteet lista kätevästi.
    paiva = None
    summa = None    
    lkm = None
    
class TULOKSET: # Luodaan luokka tilastotietoanalyysiä varten. Luokkaan tallennetaan kaikki analysoitavat tiedot oliona, jotta niiden käsittely on jatkossa helpompaa.
    lkm = None
    pienin = None
    suurin = None
    keskiarvo = None
    aikaleimapienin = None
    aikaleimasuurin = None

def TiedostoNimet(kehote): # Kysytään tällä aliohjelmalla sekä luettavan että kirjoitettavan tiedoston nimet.
    nimi = input("Anna " + kehote + " tiedoston nimi: ")
    return nimi # Palautetaan käyttäjän antama nimi pääohjelmaan

def TiedostoLue(nimi, lista): # Luetaan tiedosto tässä aliohjelmassa. Mikäli tiedostoa ei pystytä lukemaan, ilmoittaa aliohjelma käyttäjälle, että tiedoston käsittelyssä virhe ja ohjelma lopetetaan hallitusti.
    try:
        tiedosto = open(nimi, "r", encoding="utf-8")
        rivi = tiedosto.readline()
        while len(rivi) > 0:
            rivi = rivi[:-1] # Rivin viimeinen merkki on '\n' eli rivin vaihtomerkki, karsitaan se pois.
            if "DateTime" not in rivi: # Tällä komennolla saadaan tiedoston haluttu analysointi aloitettua toiselta riviltä, sillä ensimmäinen rivi on otsikkorivi ja sen tietoja ei haluta
                tietoalkio = rivi.split(';') # Tällä komennolla saadaan eroteltua luettu data eri sarakkeisiin eli aikaleimoihin ja hintoihin.
                Olio = TIEDOT()
                Olio.aikaleima = datetime.datetime.strptime((tietoalkio[0])[1:20], "%Y-%m-%d %H:%M:%S") # Muokataan olion aikaleimasta datetime-olio
                Olio.hinta = tietoalkio[1]
                lista.append(Olio) # Lisätään luetut rivit olioina listaan.
            rivi = tiedosto.readline() # Jatketaan rivien lukemista ja palataan loopin alkuun.
        tiedosto.close() # Suljetaan tiedosto.
        print("Tiedosto", "'" + nimi + "'", "luettu.")
    except Exception:
        print("Tiedoston", "'" + nimi + "'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return lista # Palautetaan luetusta tiedostosta tehty oliolista pääohjelmaan.

def tilastotietoAnalyysi(oliolista, AnalyysiLista):
    tulos = TULOKSET()
    summa = 0
    tulos.lkm = len(oliolista)
    for alkio in oliolista:
        summa = summa + float(alkio.hinta)
        if tulos.pienin == None or float(tulos.pienin) > float(alkio.hinta): # Tällä komennolla vertaillaan aina kahta peräkkäistä listan arvoa ja mikäli seuraava alkio on pienempi kuin edellinen, vaihtuu olion "pienin" alkio kyseiseksi ja looppi jatkuu. Lopulta saadaan listan pienin alkio ja sitä vastaava aikaleima.
            tulos.pienin = float(alkio.hinta)
            tulos.aikaleimapienin = alkio.aikaleima
            
        elif tulos.suurin == None or float(tulos.suurin) < float(alkio.hinta): # Tässä sama homma kuin ylempänä, mutta toiseen suuntaan eli saadaan suurin alkio ja sitä vastaava aikaleima tietoon.
            tulos.suurin = float(alkio.hinta)
            tulos.aikaleimasuurin = alkio.aikaleima
    tulos.keskiarvo = summa / tulos.lkm
    AnalyysiLista.append(tulos) # Lisätään olio listaan.
    print("Tilastotietojen analyysi suoritettu", tulos.lkm, "alkiolle.")      
    return AnalyysiLista # Palautetaan tilastotietoanalyysin tuloslista pääohjelmaan, listassa on yksi olio.

def PaivaAnalyysi(oliolista, PaivaLista):
    summa = 0
    lkm = 0
    vertailtavapv = oliolista[0]
    vertailtava = vertailtavapv.aikaleima.date()# Valitaan vertailtavaksi oliolistan ensimmäisen olion päivä.
    for alkio in oliolista:
        if vertailtava == alkio.aikaleima.date(): # Jos kaksi peräkkäin vertailtavaa datetime-olion päivämäärää on samat (HUOM. kellonaikaa ei oteta huomioon, joten datetime-oliosta saadaan pelkkä päivämäärä datetime.date() komennolla), lasketaan päivien summa yhteen ja alkioiden lkm.
            summa = summa + float(alkio.hinta)
            lkm = lkm + 1
        elif vertailtava != alkio.aikaleima.date(): # Jos vertailtavat päivät ovat eri, tallennetaan uuteen paivatulos-olioon oliolistan edellisen kohdan päivä ja päivän keskiarvo eli hinta (saadaan jakamalla summa alkioiden lukumäärällä).
            paivatulos = TIEDOT()
            paivatulos.aikaleima = vertailtava
            paivatulos.hinta = summa / lkm
            PaivaLista.append(paivatulos) # Lisätään yhden päivän tulokset uuteen listaan.
            vertailtava = alkio.aikaleima.date() # Vaihdetaan vertailtava päivä nyt oliolistan ensimmäiseen uuden päivän alkioon.
            summa = 0
            summa = summa + float(alkio.hinta) # Nollataan summa ja lisätään siihen oliolistan uuden päivän ensimmäisen alkion hinta. 
            lkm = 1 # Alustetaan alkioiden lukumäärä 1, koska pitää laskea uuden päivän ensimmäinen alkio. 
            
    #For -loopin viimeisessä kohdassa alkiot loppuvat listasta eli loopin ulkopuolelle palautuu viimeinen päivämäärä ja sen hinta-alkioiden summa. Loopissa siis ei mennä enää elif kohtaan vaan loop päättyy if kohtaan.
    #Lisätään tämä viimeinen olio käsin listaan. 
    paivatulos = TIEDOT()
    paivatulos.aikaleima = alkio.aikaleima.date()
    paivatulos.hinta = summa / lkm
    PaivaLista.append(paivatulos)
    print("Päivittäiset keskiarvot laskettu", len(PaivaLista), "päivälle.")
    return PaivaLista # Palautetaan päiväanalyysin tuloslista pääohjelmaan

def ViikonpvAnalyysi(oliolista, TulosteetLista):
    viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"] # Luodaan viikonpäiväanalyysiä varten lista, johon alustetaan jokainen päivä omalle alkioille. Tämä helpottaa oliolistan teossa myöhemmin.
    summalista = [0, 0, 0, 0, 0, 0, 0] # Alustetaan viikonpäivien alkioiden summat listaan, ensimmäinen on maanantain, toinen tiistain jne.
    lkmlista = [0, 0, 0, 0, 0, 0, 0] # Sama kuin ylempänä, mutta vain alkioiden lukumäärälle.
    ApuLista =[] # Tätä hyödynnetään tehtäessä lopullista tulosteet -listaa.
    for alkio in oliolista:
        if alkio.aikaleima.weekday() == 0: # Tällä komennolla käydään oliolistan aikaleima alkioita läpi, ja jos aikaleima on maanantai, lisätään listan maanantain alkion kohdalle summa ja lkm listoihin aikaleimaa vastaava tieto.
            summalista[0] = summalista[0] + float(alkio.hinta)
            lkmlista[0] = lkmlista[0] + 1
            
        elif alkio.aikaleima.weekday() == 1: # Sama kuin edellä, mutta tiistaille.
            summalista[1] = summalista[1] + float(alkio.hinta)
            lkmlista[1] = lkmlista[1] + 1
            
        elif alkio.aikaleima.weekday() == 2: # Keskiviikolle
            summalista[2] = summalista[2] + float(alkio.hinta)
            lkmlista[2] = lkmlista[2] + 1
            
        elif alkio.aikaleima.weekday() == 3: # Torstaille
            summalista[3] = summalista[3] + float(alkio.hinta)
            lkmlista[3] = lkmlista[3] + 1
            
        elif alkio.aikaleima.weekday() == 4: # Perjantaille
            summalista[4] = summalista[4] + float(alkio.hinta)
            lkmlista[4] = lkmlista[4] + 1
            
        elif alkio.aikaleima.weekday() == 5: # Lauantaille
            summalista[5] = summalista[5] + float(alkio.hinta)
            lkmlista[5] = lkmlista[5] + 1
            
        elif alkio.aikaleima.weekday() == 6: # Sunnuntaille
            summalista[6] = summalista[6] + float(alkio.hinta)
            lkmlista[6] = lkmlista[6] + 1

    for alkio in range (0,7): # Alkio käy läpi arvot 0-6 eli seitsemän yhteensä.
        tulos = VIIKONPVTULOKSET() # Luodaan jokaista viikonpäivää vastaava olio, jossa on päivän nimi, summa ja lkm
        tulos.paiva = viikonpaivat[alkio]
        tulos.summa = summalista[alkio]
        tulos.lkm = lkmlista[alkio]
        ApuLista.append(tulos) # Lisätään jokainen olio apulistaan.

    for alkio in ApuLista: # Apulistan pohjalta saadaan tehtyä tulosteet lista.
        if alkio.summa == 0: # Jos kyseisellä päivän alkioiden laskettu summa on 0, on keskiarvon oltava myös 0, koska jos laskee 0 / X, on tulos aina 0.
           analyysi = TIEDOT() # Luodaan olio, jossa on aikaleima eli tässä tapauksessa päivän nimi ja sitä vastaava hinta eli keskiarvo.
           analyysi.aikaleima = alkio.paiva
           analyysi.hinta = alkio.summa
           TulosteetLista.append(analyysi) # Lisätään olio tulosteet listaan.
        else: # Jos päivän yhteenlaskettu summa on != 0, keskiarvo saadaan jakamalla summa alkioiden lukumäärällä.
            analyysi = TIEDOT()
            analyysi.aikaleima = alkio.paiva
            analyysi.hinta = alkio.summa / alkio.lkm
            TulosteetLista.append(analyysi) # Lisätään olio tulosteet listaan.
    # Tyhjennetään kaikki apulistat.        
    summalista.clear() 
    lkmlista.clear()
    ApuLista.clear()
    viikonpaivat.clear()
    return TulosteetLista # Aliohjelma palauttaa tulosteet listan, jossa on jokaista viikonpäivää (maanantai, tiistai, ...) vastaava päivän keskiarvo.

def TiedostoKirjoita(kerta, nimi, lista): # kirjoitetaan tiedosto tässä aliohjelmassa. Mikäli tiedostoa ei pystytä lukemaan, ilmoittaa aliohjelma käyttäjälle, että tiedoston käsittelyssä virhe ja ohjelma lopetetaan hallitusti.
    # Aliohjelman parametri "kerta" tarkoittaa kirjoituskertaa. Koska minulla on tässä ohjelmassa kolme eri listaa jokaisesta analyysistä, tulen käymään samassa kirjoitusaliohjelmassa kolme kertaa, ja joka kerralla kirjoitan eri jutun, joten aliohjelman
    # jako kolmeen eri toimintoon on kätevää.
    try:
        if kerta == 1: # Pääohjelmassa on alustettu, että kerta = 1 tarkoittaa tilastotietoanalyysin listan kirjoittamista.
            tiedosto = open(nimi, "w", encoding="utf-8") # Avataan käyttäjältä kysytty tiedosto ja käytetään "w" komentoa, koska kaikki edellinen tieto halutaan tyhjentää ennen kirjoitusta.
            for alkio in lista: # Käydään oliolista läpi ja kirjoitetaan tiedot halutussa muodossa
                tiedosto.write("Analyysin tulokset " + str(alkio.lkm) + " tunnilta ovat seuraavat:" + '\n') # Lisätään aina rivinvaihtomerkki loppuun, jotta tiedot tulevat eri riveille.
                tiedosto.write("Sähkön keskihinta oli " + str(round(alkio.keskiarvo, 1)) + " snt/kWh." + '\n')
                tiedosto.write("Halvimmillaan sähkö oli " + str(round(alkio.pienin, 2))  + " snt/kWh, " + alkio.aikaleimapienin.strftime("%d.%m.%Y %H:%M") + "." + '\n')
                tiedosto.write("Kalleimmillaan sähkö oli " + str(round(alkio.suurin, 2)) + " snt/kWh, " + alkio.aikaleimasuurin.strftime("%d.%m.%Y %H:%M") + "." + '\n')
                tiedosto.write("\n") # Tilastotietoanalyysin ja päiväanalyysin tietojen kirjoittamisen väliin haluttiin tyhjä rivi, joten kirjoitetaan lopuksi tyhjä rivi.
            tiedosto.close() # Suljetaan tiedosto.
        elif kerta == 2: # Tämä vastaa päiväanalyysin listan kirjoittamista.
            tiedosto = open(nimi, "a", encoding="utf-8") # Avataan tiedosto nyt "a" (append) muodossa, jotta aiemmin kirjoitetut tiedot ei häviä vaan lisätään samaan tiedostoon lisää tekstiä.
            tiedosto.write("Päivittäiset keskiarvot (Pvm;snt/kWh):" + '\n') 
            for alkio in lista: # Käydään päiväanalyysi oliolista läpi
                tiedosto.write(alkio.aikaleima.strftime("%d.%m.%Y") + EROTIN + str(round(alkio.hinta, 1)) + '\n') # Muokataan ja kirjoitetaan päivämäärä halutussa muodossa (pv.kk.vvvv), lisätään tietojen välille EROTIN ja kirjoitetaan päivän keskiarvo yhden desimaalin tarkkuudella.
            print("Tiedosto", "'" + nimi + "'", "kirjoitettu.")
            tiedosto.close() # Suljetaan tiedosto.
    except Exception:
        print("Tiedoston", "'" + nimi + "'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    try:
        if kerta == 3: # Tämä vastaa viikonpäiväanalyysin listan kirjoittamista.
            tiedosto = open(nimi, "w", encoding="utf-8") # Avataan tiedosto taas "w" muodossa.
            tiedosto.write("Viikonpäivä" + EROTIN + "Keskimääräinen hinta snt/kWh" + '\n') # Kirjoitetaan otsikko rivi halutussa muodossa.
            for alkio in lista: # Käydään oliolista läpi ja kirjoitetan tiedot halutussa muodossa
                tiedosto.write(alkio.aikaleima + EROTIN + "{0:.1f}".format(alkio.hinta) + '\n') # Käytetään formattia, koska jos päivän keskiarvo oli 0, halutaan se ilmaista yhden desimaalin tarkkuudella 0,0.
            tiedosto.close() # Suljetaan tiedosto
            print("Tiedosto", "'" + nimi + "'", "kirjoitettu.")
    except Exception:
        print("Tiedoston", "'" + nimi + "'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None # Kirjoitus aliohjelma ei palauta mitään





    
