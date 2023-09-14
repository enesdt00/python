def minFunksjon():
   for x in range(2):
       c = 2
       print(c)
       c += 1
       b = 10
       b += a
       print(b)
   return(b)
def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)
hovedprogram()
"""Først defineres funksjonen minFunksjon, som ikke skal ta imot noen 
parametere.e. Deretter defineresprosedyren hovedprogram, som heller ikke tar noen parametre.
Deretter kalles hovedprogram.Inne i hovedprogram opprettes en variabel a med verdi 42.
Deretter oppretter vi en variabel b med verdien 0. Så vises b verdien med print. 
Deretter er b lik med a.Så kaller vi minFunksjon.i funksjonen er det en for-løkken som kjøres
3 ganger.På grunn av at Rangen var 2. Så opprettes en variabel c med verdi 2. Så vises c verdien
med print. Deretter øker verdien av c bare med 1 tall. Så opprettes en variabel b med verdi 10.
Deretter blir b lik med b pluss a, men a er ikke opprettes i den funksjonen, derfor fikk vi feil
melding(Name Eror). Hvis a hadde ha blitt definert inn i lokalen, fikk vi ikke den feil meldingen.
"""
