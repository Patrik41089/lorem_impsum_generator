import random
seznam = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
samohlasky = ["a","e","i","y","o","u"]
anglictina_predlozky = ["an","the", "in", "on", "at", "up"]
anglictina_konce = ["ing","tion"]

def nahodne_slovo(delka):
    slovo = ''.join(random.choice(seznam) for i in range(delka))
    return slovo

def nahodna_koncovka():
    koncovka =  ''.join(random.choice(anglictina_konce))
    return koncovka

vygenerovana_slova = ' '.join(nahodne_slovo(random.randint(2, 10)) for i in range(random.randint(2,10)))

text = ''.join(vygenerovana_slova + random.choice(anglictina_konce))

print(text)