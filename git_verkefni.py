#Git Verkefni
#Davíð Þór Gíslason

#Dæmi 1
tala1 = int(input("Sláðu inn tölu: "))
tala2 = int(input("Sláðu inn aðra tölu: "))
plus = tala1+tala2
sinnum = tala1*tala2
print ("Tölurnar lagðar saman er samtals: " +str(plus))
print ("Tölurnar margfaldaðar saman er samtals: " +str(sinnum))

#Dæmi 2
fornafn = input("Hvað er fornafnið þitt? ")
eftirnafn = input("Hvað er eftirnafnið þitt? ")
print ("Halló "+fornafn+" "+ eftirnafn)

#Dæmi 3
litill = 0
stor = 0
litillstor = 0
texti = input("Sláðu inn texta")
for i in range(len(texti)):
    if texti[i].isupper():
       stor += 1
       if texti[i+1].islower():
           litillstor += 1
    elif texti[i].islower():
        litill += 1
print ("Í þessum texta eru "+str(stor)+" hástafir, "+str(litill)+" lágstafir og "+str(litillstor)+" lágstafir koma strax á eftir hástaf")
