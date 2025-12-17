

mevalar = ['olma', 'ajir', 'shaftoli', "o'rik"]
narhlar = [12000, 18000, 10900, 22000, 30000]
sonlar = ['one', 'two', 3 , 4, 5]
ismlar = []

print(mevalar)

mevalar= ['olma', 'ajir', 'shaftoli', "o'rik"]
print("Birinchi meva:", mevalar[0].title())
print("Ikkinchi meva:", mevalar[1].title())


narhlar = [12000, 18000, 10900, 22000, 30000]
print(narhlar[2] + narhlar[3])

car_models = ['Toyota', 'Ford', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen' ]
print(car_models)

narhlar = [12000, 18000, 10900, 22000, 30000]
narhlar[0]= 13000   # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2]= 11000  # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3]= narhlar[3] + 2000
print(narhlar)

mevalar = ['olma', 'ajir', 'shaftoli', "o'rik"]
mevalar.append('tarvuz')
print(mevalar)

cars = []
cars.append('Lacetti')
cars.append('Nexia 3')
cars.append('Cobalt')
print(cars)

# .insert() metodi
# Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan foydalanamiz. .insert() metodi ichida yangi elementning indeksi va qiymati beriladi:

cars= ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0,'Malibu')
print(cars)


mevalar = ['olma', 'ajir', 'shaftoli', "o'rik"]
del mevalar[1]
print(mevalar)

mevalar = ['olma', 'ajir', 'shaftoli', "o'rik"]
mevalar.remove('shaftoli')
print(mevalar)


hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove('mushuk')
print(hayvonlar)

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3)
print("Men" + mahsulot + "sotib oldim")
print("Olinmagan mahsulotlar: ",  bozorlik)


ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]

print("Salom" + ismlar[0] + "ishlaring yaxshimi?")
print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
print(ismlar[-1] + "g'ildirakni g'izillatib g'ildartti")

sonlar = [22, -58.2, 34.0, 1983, 123_456_678_000, 112.4]
print(sonlar)

sonlar[0] = sonlar[0]+sonlar[-1]
sonlar[1] = -67.8
sonlar[4] = sonlar[4] +37
del sonlar[5]
print(sonlar)

t_shaxslar = ['Amir Temur', 'Imon Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan , \n\ zamonaviy shaxslardan esa {z_shaxslar.pop(0)}  bilan, \n\ suhbat qilishni istar edim\n")

friends = []
friends.append("John")
friends.append("Alex")
friends.append("Danny")
friends.append("Sobirjon")
friends.append("Vanya")
print(friends)

friends.remove("John")
friends.remove("Alex")
print(friends)

friends.append("Hasan")
friends.insert(0,"Husan")
friends.insert(2,"Ivan")
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar:", mehmonlar)

