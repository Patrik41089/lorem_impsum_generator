GENERÁTOR ANGLICKÝCH SLOV

1) První si musíte soubor stáhnout nebo naklonovat repozitář do visual studia
2) Pro generaci náhodného textu si potřebujete nejprve spustit terminál
3) Pomocí funkce RUN PYTHON FILE, která je vpravo nahoře spustíte program
4) Program Vám vypsal náhodný text, který se podobá angličtině, jak je zmíněno v nadpisu
5) Pokud chcete generovat znovu musíte opakovat spouštění funkce RUN PYTHON FILE, nebo-li zopakovat krok 3)
 
MŮJ POSTUP ŘEŠENÍ
  
1) Jako první jsem si importoval random, protože hodlám pracovat s nějakou náhodou pro generování slov
2) První jsem se rozhodl jaký jazyk chci napodopit a vybral jsem si angličtinu.
3) Poté jsem se rozhodl udělat nějaký list s abecedou , kde jsou všechna písmena pro angličtinu.
4) Následně jsem udělal další dva seznamy pro samohlásky a souhlásky, protože nechci aby slovo bylo složeno jen ze 5) souhlásek nebo samohlásek.
6) Seznamy pro koncová slova a předložky jsem použil proto, aby se to nejvíce podobalo angličtině. Vybral jsem pár o kterých si myslím že jsou nejpoužívanější a proto abych lépe poznal jak často se budou opakovat.
7) Dále jsem si zavedl funkce pro vytváření náhodných souhlásek, samohlásek, koncovek a předložek. Ze souhlásek a samohlásek složitější funkci, díky které se spojí souhlásky a samohlásky a vznikne slovo.
8) Protože poprvé jsem to zkoušel bez nějaké operace, která by omezila právě například 3 stejné samohlásky zasebou, jsem zvolil jednoduchý postup, který mě napadl. Po každé se vybere nějaké písmeno z abecedy a následně každý sudý výběr zvolí samohlásku a každý lichý výběr zvolí souhlásku.
9) Poslední funkcí kterou jsem potřeboval bylo, abych mohl zobrazit spoustu těhle generovaných slov.
10) Tam jsem potřeboval použít vše co jsem si zatím vytvořil. Udělal jsem si novou proměnnou prázdného seznamu, kam budu chtít vkládat to, co chci zobrazit. Použil jsem porměnnou ve funkci generování textu pro ulehčení, tak jako jsem to udělal u slova. Parametr délky slov jsem určil na 2-10 protože slova nebyla dost dlouhá ani krátká.
11) Nějakou pravděpodobnost na vložení anglické koncovky ke slovu, protože bych nechtěl aby byli u všech slov. Podobným způsobem jsem zpracoval vkládání předložek, ale tady jsem to udělal složitější, aby se nestávalo že budou párkrát zasebou ale co nejméně.
12) Po zhotovení cyklů jsem výsledné proměnné a funkce vložil do prázdného seznamu. Určil délku textu na náhodu od 20 až do 150 slov, aby jich nebylo málo a zároveň aby se vešel na obrazovku a zobrazil jsem proměnnou text.
