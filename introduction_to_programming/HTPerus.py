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
# Tehtävä HTPerus.py
# eof
import HTPerusKirjasto # Lisätään itsetehty kirjasto tehtävään

def valikko(): # Luodaan valikko ohjelma, josta käyttäjä valitsee haluamansa toiminnon.
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi viikonpäivittäiset keskiarvot")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta # Palautetaan käyttäjän valinta kokonaislukuna.

def paaohjelma():
    valinta = 1 # Alustetan valinta 1:sellä, jotta pästään While looppiin
    LukuLista = [] # Luodaan luettavia tietoja varten LukuLista.
    AnalyysiLista = [] # Luodaan tilastotietoanalyysiä varten AnalyysiLista.
    PaivaLista = [] # Luodaan päiväanalyysiä varten PaivaLista.
    TulosteetLista = [] # Luodaan viikonpäivä analyysiä varten TulosteetLista.
    while valinta != 0: # Koska valinta on alustettu 1, pysytään loopissa niin kauan ennen kuin käyttäjä valitsee numeron, jonka toimintoon kuuluu break.
        valinta = valikko() # Tällä tavalla saadaan valikko tulostettua aina yhden toiminnon jälkeen uudestaan.

        if valinta == 1:
            LukuLista.clear() # Tyhjennetään luettuja tietoja sisältävä lista aina ennen, kun luetaan uutta tiedostoa. Näin ollen listassa on aina ainoastaan sen kerran tiedot, mitä seuraavassa kohdassa kysytään.
            luettava = HTPerusKirjasto.TiedostoNimet("luettavan") # Käydään kirjaston TiedostoNimet aliohjelmassa, josta palautuu luettavan tiedoston nimi.
            LukuLista = HTPerusKirjasto.TiedostoLue(luettava, LukuLista) # Käydään kirjaston TiedostoLue aliohjelmassa, johon lähetetään luettavan tiedoston nimi
            # ja tyhjäksi alustettu LukuLista, johon luetut tiedot tallennetaan.
            
        elif valinta == 2:
            # Tyhjennetään molemmat analyysien tuloslistat aina, kun aletaan tekemään analyysejä. Tällä varmistetaan, ettei listoissa ole moninkertaisesti arvoja.
            AnalyysiLista.clear()
            PaivaLista.clear()
            # Tarkistetaan ensin, onko analysoitavassa listassa mitään arvoja, joita voi analysoida. Jos ei ole, tulostaa ohjelma käyttäjälle tiedon, ettei ollut analysoitavaa.
            if len(LukuLista) > 0: # Kun analysoitavaa on, tehdään analyysit.
                AnalyysiLista = HTPerusKirjasto.tilastotietoAnalyysi(LukuLista, AnalyysiLista) # Käydään kirjaston tilastotietoAnalyysi aliohjelmassa, johon
                # lähetetään luettava lista ja tyhjäksi alustettu AnalyysiLista, johon tilastotietoanalyysin tulokset tallennetaan.
                PaivaLista = HTPerusKirjasto.PaivaAnalyysi(LukuLista,PaivaLista) # Käydään kirjaston PaivaAnalyysi aliohjelmassa, johon
                # lähetetään luettava lista ja tyhjäksi alustettu PaivaLista, johon päiväanalyysin tulokset tallennetaan.
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
                
        elif valinta == 3:
            if len(AnalyysiLista) > 0 and len(PaivaLista) > 0: # Aluksi tarkastetaan, onko listoilla mitään kirjoitettavaa. Jos ei ole, niin ei kysytä kirjoitettavan tiedoston nimeä.
                kirjoitettava = HTPerusKirjasto.TiedostoNimet("kirjoitettavan") # Kysytään käyttäjältä kirjoitettavan tiedoston nimi.
                kerta = 1 # Tämä alustus tarkoittaa ensimmäistä kirjoituskertaa eli kun kirjoitetaan tiedostoon tilastotietoanalyysin tulokset.
                HTPerusKirjasto.TiedostoKirjoita(kerta, kirjoitettava, AnalyysiLista) # TiedostoKirjoita ohjelman saamat parametrit (kirjoituskerta, tiedoston nimi, lista)    
                kerta = 2 # Tämä alustus tarkoittaa toista kirjoituskertaa eli kun kirjoitetaan päiväanalyysin tulokset.
                HTPerusKirjasto.TiedostoKirjoita(kerta, kirjoitettava, PaivaLista) # TiedostoKirjoita ohjelman saamat parametrit (kirjoituskerta, tiedoston nimi, lista)
            else:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")


        elif valinta == 4:
            TulosteetLista.clear() # Tyhjennetään tulosteet lista aina ennen kun tehdään analyysi, jotta varmistetaan, ettei listalla ole moninkertaisesti arvoja.
            kerta = 3 # Tämä alustus tarkoittaa kolmatta kirjoituskertaa eli kun kirjoitetaan tiedostoon viikonpäivä analyysin tulokset.
            if len(LukuLista) > 0: # Tarkistetaan taas, että luettavassa listassa on tietoja ennen analyysiä.
                TulosteetLista = HTPerusKirjasto.ViikonpvAnalyysi(LukuLista, TulosteetLista) # Käydään kirjaston VookonpvAnalyysi aliohjelmassa, johon
                # lähetetään luettava lista ja tyhjäksi alustettu TulosteetLista, johon ViikonpvAnalyysin tulokset tallennetaan
                
            if len(TulosteetLista) > 0: # Tarkastetaan vielä, että kirjoitettavassa listassa on jotain kirjoitettavaa.
                kirjoitettava = HTPerusKirjasto.TiedostoNimet("kirjoitettavan") # Kysytään kirjoitettavan tiedoston nimeä.
                HTPerusKirjasto.TiedostoKirjoita(kerta, kirjoitettava, TulosteetLista) #TiedostoKirjoita ohjelman saamat parametrit (kirjoituskerta, tiedoston nimi, lista)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
                
        elif valinta == 0:
            print("Lopetetaan.")
            # Tyhjennetään kaikki listat
            LukuLista.clear()
            AnalyysiLista.clear()
            PaivaLista.clear()
            TulosteetLista.clear()
            break # Poistutaan While loopista
            
        else:
            print("Tuntematon valinta, yritä uudestaan.") # Jos käyttäjä syöttää jotakin muuta kuin 0-4, pyydetään syöttämään uusi valinta
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()   # Kutsutaan pääohjelmaa
