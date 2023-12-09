import random
seznam = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]

samohlasky = ["a","e","i","y","o","u"]

anglictina_predlozky = ["an","the", "in", "on", "at", "up"]

anglictina_konce = ["ing","tion","ed","s"]

#generace písmena s délkou k pouziti na slozeni slova z pismen
def nahodne_slovo(delka):               
    slovo = ''.join(random.choice(seznam) for i in range(delka))
    return slovo    #vraceni hodnoty z funkce abych ji mohl pouzit

#generace koncovky
def nahodna_koncovka():
    koncovka = random.choice(anglictina_konce)
    return koncovka

#generace predlozky
def nahodna_predlozka():
    predlozka = random.choice(anglictina_predlozky)
    return predlozka

#generace textu, z písmena slovo s koncovkou
def generovani_text(pocet_slov): #pocet slov k pouziti ke generovani nahodneho mnozstvi textu pozdeji
    vygenerovana_slova = [] #prazdny seznam kam se mi budou vypisovat generovana slova s koncovkou
    predlozka = False #nastaveni predlozky na false
    for i in range(pocet_slov): #pro zadany pocet slov dela pro kazde slovo tento cyklus
        slovo = nahodne_slovo(random.randint(2, 10))
        if random.randint(0,1) < 0.5:  #0.5 je polovina rozsahu generace nahodneho cisla od 0 do 1 takze je to 50% sance na pridani koncovky ke kazdemu generovanemu slovu
            slovo += nahodna_koncovka() #slouceni slova a koncovky
            
        if not predlozka and random.randint(0,1) < 0.8: #kdyz predlozka false a zaroven je cislo mensi nez 0.8 => 80% sance 
            vygenerovana_slova.append(nahodna_predlozka()) #prida predlozku do seznamu 
            predlozka = True    #nasteveni predlozky na true aby cyklus pokracoval do else
        else:
            predlozka = False   #nastaveni predlozky na false aby se cyklus opakoval
        
        vygenerovana_slova.append(slovo) #vlozeni hotoveho slova s koncovku do seznamu ktery s vypise pouzdeji

    text = ' '.join(vygenerovana_slova) #slouceni pomoci join aby se to nevypisovalo v seznamu
    return text

text = generovani_text(random.randint(20, 150))
print(text)
