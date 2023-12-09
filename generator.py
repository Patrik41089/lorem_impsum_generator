import random
seznam = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
samohlasky = ["a","e","i","y","o","u"]
anglictina_predlozky = ["an","the", "in", "on", "at", "up"]
anglictina_konce = ["ing","tion"]

def nahodne_slovo(delka):
    slovo = ''.join(random.choice(seznam) for i in range(delka))
    return slovo

vygenerovana_slova = ' '.join(nahodne_slovo(random.randint(2, 10)) for i in range(random.randint(10,20)))



print(vygenerovana_slova)