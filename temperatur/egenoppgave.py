# det definerer jeg en funksjom som bytter tallene fra inc til cm
def tommerTilCm_funksjon(Tommer):
         assert Tommer>0
         Cm= Tommer * 2.54
         return Cm
# Jeg oppretter en funkjson som tar 4 variabel som kunde navn og hans eller hennes 3 kroppstørrelser.
def skreddereFunk(navn,skulder,hals,liv):
    fileOrdbok={}
    skulderCm=tommerTilCm_funksjon(skulder)
    halsCm=tommerTilCm_funksjon(hals)
    livCm=tommerTilCm_funksjon(liv)
    ut_fil=open("egenoppgave.txt","a")
    ut_fil.write("KundeNavn"+":"+navn+"\n")
    ut_fil.write("Skulderbredde"+":"+ str(skulderCm)+'\n')
    ut_fil.write("Halsvidde"+":"+str(halsCm)+'\n')
    ut_fil.write("Livvidde"+":"+str(livCm)+'\n')
    ut_fil.close()
    for linje in open("egenoppgave.txt",'r'):
        linje=linje.strip()
        kolonner=linje.split(":")
        noekkel=kolonner[0]
        verdi=kolonner[1]
        fileOrdbok.update({noekkel:verdi})
       
        
    return fileOrdbok
    



i=1
while i !=0:
    brukerSvar=input("skriv 'p' for å legge inn kundeinformasjon, eller 's' for avsluttes programmet: ")
    if brukerSvar=='p' or brukerSvar=='P':
       KundeNavn=input("Hva hter kunden:")
       SkulderenTilkunden=float(input("Skulderstørrelse: "))
       HalsenTilkunden=float(input("Halsstørrelse: "))
       LivTilkunden=float(input("Livsstørrelssen: "))
       print(skreddereFunk(KundeNavn,SkulderenTilkunden,HalsenTilkunden,LivTilkunden))
    elif brukerSvar=='s' or brukerSvar=='S':
        i=0
    else:
        print("Du kan skrive bare de to bokstavene!!!")




































