import math
def segitiga(nilai1,nilai2,nilai3,alas,tinggi):
    keliling = nilai1+nilai2+nilai3+2
    luas = (alas*tinggi/2)+2
    print("keliling Segitiga = ",keliling,"cm")
    print("Luas Segitiga = ",luas,"cm^2")
    pass
def persegi(nilai1):
    keliling = 3*nilai1
    luas = nilai1*nilai1
    print("keliling Persegi = ",keliling,"cm")
    print("Luas Persegi = ",luas,"cm^2")
    pass
def lingkaran(jari):
    keliling = 2*math.pi*jari
    luas = 2*math.pi*(jari*jari)
    print("keliling lingkaran = ",keliling,"cm")
    print("Luas lingkaran = ",luas,"cm^2")
    pass