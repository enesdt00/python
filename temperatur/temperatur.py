# en funksjon definerer jeg for å ta en file, og dele elemenentene i to forskjellige lister.
# list er rekkefølge, derfor kan lage en ordbok der elementene i en list blir nøkkelord, og elementene i andre list blir innholdsverdi.
def les_temp(filnavn):
    resultatet={}

    for linje in open(filnavn):
        linje=linje.strip()
        kolonner=linje.split(",")
        noekkel=kolonner[0]
        verdi=kolonner[1]

        resultatet[noekkel]=verdi
    return resultatet
print(les_temp('max_temperatures_per_month.csv'))


# jeg definerer en ny funksjon som tar en ordbok og en file.
# det trenger jeg tre lister her for maaneder,dager og temperaturer.
def hoyesteTemp(andreFilnavn,ordbok1):

     manedList=[]
     dagList=[]
     tempList=[]
# jeg samler maaneder,dager, temperaturer i tre forskjellige lister.
     for linje in open(andreFilnavn):
        linje=linje.strip()
        kolonner=linje.split(",",2)
        manedList.append(kolonner[0])
        dagList.append(kolonner[1])
        tempList.append(kolonner[2])
        # alle lister har 365 elementer.Derfor range er 365.
     for teller in range(365):
        # ordbok er ikke rekkefølge. Derfor trenger en ny variabel så kan jeg sammeligne temperaturer.
        mon=manedList[teller] 
        
        if float(tempList[teller])>float(ordbok1[mon]):
            print("Ny varmerekord på",dagList[teller],manedList[teller],":",tempList[teller],"grader Celcius (gamle varmerekord var ",ordbok1[mon],"grader Celcius")
            ordbok1.update({mon:tempList[teller]})
        
# print(ordbok1) trenger jeg denne funksjonen i andre spørsmål derfor kan jeg ikke lage den en prosedyr.
     return ordbok1
     
      
     

maxTempOrdbok=les_temp('max_temperatures_per_month.csv')
hoyesteTemp("max_daily_temperature_2018.txt",maxTempOrdbok)
# nyVarmerekord={'Jan': '12.5', 'Feb': '13.8', 'Mar': '21.5', 'Apr': '25.4', 'May': '31.1', 'Jun': '33.7', 'Jul': '34.6', 'Aug': '34.2', 'Sep': '26.4', 'Oct': '21.0', 'Nov': '14.4', 'Dec': '12.6'}
nyVarmerekord=hoyesteTemp("max_daily_temperature_2018.txt",maxTempOrdbok)
# en prosedyr som tar en ordbok og en file.
#  jeg oppretter to list, elementer kommer fra ordboka. 
def fraOrdboktilFil(temperaturOrdbok,file):
    manedList=list(temperaturOrdbok.keys())
    tempList=list(temperaturOrdbok.values())
    #  ved while-løkken setter jeg alle elementene i de listene i en file.
    teller=0
    while teller <len(manedList):
        ut_file=open(file,'a')
        ut_file.write(manedList[teller])
        ut_file.write(',')
        ut_file.write(tempList[teller])
        ut_file.write("\n")
        ut_file.close()
        teller+=1

fraOrdboktilFil(nyVarmerekord,"ny_rekordfil.txt")



     


        


   





