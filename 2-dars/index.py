#
#
# shahar = "quqon"
# viloyat = 'Fargona'
#
#
# ism = "Sirojbek Muxtorov"
# matn = " Men yangi 📱 oldim"
#
# print(ism)
# print(matn)
# smayl = '🚀'
# print(smayl)

# ism = 'Sirojbek'
# print("Mening ismi:"  + ism)
#
# ism = 'Sirojbek'
# familiya = 'Muxtorov'
# print(ism + familiya)
# print(ism + ' ' + familiya)

#  f-string

# ism = 'Sirojbek '
# familiya = 'Muxtorov'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)


# ism = 'James'
# famaliya = 'Bond'
# print(f"Salom, mening ismim {famaliya} {ism} {famaliya}!")


#  MAHUS BELGILAR

# print('Hello World')
# print('Hello \tWorld')
# print('Hello \nWorld')

# ism = 'James'
# familiya = 'bond'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())
# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())


# meva = "  olma  "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men" +  meva.rstrip() + " yaxshi ko'raman")
# print("Men" +  meva.strip() + " yaxshi ko'raman")
# print("Men" + meva + " yaxshi ko'raman")

#  Input

# ism = input("Ismingiz nima?")
# print("Assalom alaykum," + ism)


# ism = input("Ismingiz nima:")
# print("Assalom alaykum," + ism.title())
#
#
# kocha = "Bog'bon"
# mahalla = "sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
#
# print(kocha  + "ko'chasi," + mahalla + " mahallasi, " + \
#       tuman  + "tumani," + viloyat + "viloyati")
#
# print("Iltimos , quyadgi malumotlari kiriting:")
# kocha = input("Ko'changiz:")
# mahalla = input("Mahallangiz:")
# tuman = input("Tumaningiz:")
# viloyat = input("Viloyatingiz:")
# print(kocha  + "ko'chasi," + mahalla + " mahallasi, " + \
#       tuman  + "tumani," + viloyat + "viloyati")
#
# print(kocha  + "ko'chasi,\n" + mahalla + " mahallasi,\n " + \
#       tuman  + "tumani,\n" + viloyat + "viloyati")
#
# mazil = f"{kocha} ko'chasi, {mahalla} mahllasi, {tuman} tumani, {viloyat} viloyati"
# print(mazil)
#
# print(mazil.upper())
# print(mazil.lower())
# print(mazil.title())


ism = input("Ismingiz nima:")
print("Assalom alaykum," +  ism.title())


kocha = "Bog'bon"
mahalla = "sog'bon"
tuman ="Bodomzor"
viloyat = "Samarqand"

print(kocha + "ko'chasi," + mahalla + "mahallasi,"  + \
       tuman + "tumani," + viloyat + "viloyati" )

print("Iltimos, quyadgi malutlari kiriting:")
kocha = input("Ko'changiz:")
mahalla = input("Mahallangiz:")
tuman = input("Tumaningiz:")
viloyat = input("Viloyatingiz:")
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")

print(kocha + " ko'chasi, \n " + mahalla + " mahallasi,\n " + \
      tuman + " tumani, \n " + viloyat + " viloyati")

mazil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(mazil)

print(mazil.upper())
print(mazil.lower())
print(mazil.title())