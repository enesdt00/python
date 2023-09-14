# det oppretter jeg en funksjon som tar 2 variabel og samler dem
def add_funksjon(tall1,tall2):
    sum=tall1 + tall2
    return sum
print(add_funksjon(100,200))
#  det definert jeg en funksjon som tar 2 variabler og vurderer i 3 betinget. Hvis alle bettingelsene er oppfylt, trekkes andre tallen fra første tallen.
def sub_funksjon(tall1,tall2):
    sum=tall1-tall2
    assert tall1<250 and tall1>=-250
    assert tall2<200 and tall2>=-200
    assert sum<=150  and sum>=-150
    
    return sum
print(sub_funksjon(100,50))
print(sub_funksjon(-100,-50))
print(sub_funksjon(-100,50))
# Her er det en funksjon so tar to variabler og vurderer i 3 betinget. Dersom de betingelsene er oppfylt, deles første tallen med andre tallen
def div_funksjon(tall1,tall2):
    sum= tall1/tall2
    assert tall1<250 and tall1>=-250
    assert tall2<200 and tall2>=-200
    assert sum<=150   and sum>=-150
    return sum

print(div_funksjon(100,50))
print(div_funksjon(-100,-50))
print(div_funksjon(-50,100))
# Her er det en funksjon som tar en variabel som er tommer , og finner cm verdien til den variabelen.
def tommerTilCm_funksjon(Tommer):
    assert Tommer>0
    Cm= Tommer * 2.54
    return Cm
print(tommerTilCm_funksjon(10))

def skrivBeregninger():
#   her bruker jeg alle funksjonene.
  print("Utregninger:")
  brukerensTall1=float(input("Skriv inn tall 1:"))
  brukerensTall2=float(input("Skriv inn tall 2:"))
  addTall=add_funksjon(brukerensTall1,brukerensTall2)
  print("Resultat av summering %.2f:"%(addTall))
  print("Resultat av subtraksjon %.2f:" % sub_funksjon(brukerensTall1,brukerensTall2))
  print("Resultat av divisjon %.2f:" % div_funksjon(brukerensTall1,brukerensTall2))
  print("Konvertering fra tommer til cm")
  tommerTall=float(input("skriv inn et tall:"))
  print("Resultat %.2f" %tommerTilCm_funksjon(tommerTall))

skrivBeregninger()





