# i begynnelsen definerte jeg en funksjon som tar et navn for å lage et nytt brukenavn.
def lagBrukernavn(navn):
        navn1=navn.lower()
        list=[]
        etterNavnlist=[]
        # her bruker jeg en split, på den måten deler jeg navnet og etternavnet,og stter dem i en list. Etterpå lagte en ny list ved bokstaven til etternavnet.
        for ord in navn1.split():
            list.append(ord)
        for bokstav in list[1]:
            etterNavnlist.append(bokstav)
        # til slutt samler jeg førstle element i førstelist(navn) og første element i etternavnlist(første bokstaven til etternavnet)
        brukerenNavn=list[0]+etterNavnlist[0]
        
        return "brukerennavn er: "+ brukerenNavn
navn1=input("Skriv et fulltnavt med et mellomrom:")
print(lagBrukernavn(navn1))
#  her definerer jeg en ny funksjon som tar to variabel for å lage en epost addresse.
def lagEpost(brukerNavn,epostSuffix):
     epost=brukerNavn+"@"+epostSuffix
     return epost


brukerNavn1=input("skriv et brukernavn: ")
epostSuffix1= input("Skriv en epostSuffix: ")
print(lagEpost(brukerNavn1,epostSuffix1))

# jeg oppretter en ny prosedyr som tar en ordbok. etterpå deler den ordboken i to lister. 
# en av dem for nøkkelord, og den andre for innholdsverdi
def skrivUtEposter(ordbok):
     epostOrdbok=ordbok
     nøkkelVerdilist=list(epostOrdbok.keys())
     inholdsVerdilist=list(epostOrdbok.values())
    #  her bruker jeg en while-løkken,men jeg vet at æ kunne også bruke for.
    # jeg kaller også lagEpost funksjon for å lage en ny epost-addresse med de to variabler
     a=0
     while a < len(epostOrdbok):
       brukerEpost=lagEpost(nøkkelVerdilist[a],inholdsVerdilist[a])
       print( brukerEpost)
       a+=1

         
        
     
ordbokBrukeren={"olav":"ifi.uio.no","karin":"student.matnat.uio.no"}
skrivUtEposter(ordbokBrukeren)
# Her bruker jeg alle funksjonenne jeg laget før.
tomOrdbok={}
i=1
while i!=0:
    brukerenInput=input("Skriv en bosktav av de tre bokstavene 'i,p,s': ")
    if brukerenInput=="i":
        navnTilbrukeren=input("Skriv inn et fult navn med et mellomrom: ")
        suffixenTilbrukeren=input("Skriv inn en e-post suffix:")
        BrukerNavnUio=lagBrukernavn(navnTilbrukeren)
        tomOrdbok[BrukerNavnUio] = suffixenTilbrukeren
    elif brukerenInput=="p":
         tomOrdbok[BrukerNavnUio] = suffixenTilbrukeren
         skrivUtEposter(tomOrdbok)
    elif brukerenInput=="s":
         i=0








