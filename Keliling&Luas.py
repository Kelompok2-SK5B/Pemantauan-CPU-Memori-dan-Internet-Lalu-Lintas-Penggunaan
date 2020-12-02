
#Program Luas dan Keliling Lingkaran
print("Lingkaran")
import math

def luas_lingkaran(r):
    luas = (math.pi * (r ** 2))
    print("luas lingkaran = ", luas)

def keliling_lingkaran(r):
    keliling = 2 * (math.pi * r)
    print("Keliling lingkaran = ", keliling)

angka = int(input("Masukkan Jari-jari lingkaran :"))
keliling_lingkaran(angka)
luas_lingkaran(angka)

#Program luas dan Keliling  Persegi
print("Persegi")
def luas_persegi (s):
    luas3 = s**2
    print("Luas Persegi :", luas3)

def keliling_persegi (s):
    keliling3 = 4 * s
    print("Keliling Persegi :", keliling3)

a = int(input("Masukkan panjang sisi :"))
luas_persegi(a)
keliling_persegi(a)

#Program luas dan keliling Segitiga'''
print("Segitiga")
def luas_segitiga(a,t):
    luas2 = 0,5 * a * t
    print("Luas segitiga :", luas2)

def keliling_segitiga(a,b,c):
    keliling2 = a+b+c
    print("Keliling segitiga :", keliling2)

a = int(input("Panjang alas segitiga = "))
b = int(input("Panjang sisi b = "))
c = int(input("Panjang sisi c = "))
t = int(input("Tinggi segitiga = "))

luas_segitiga(a, t)
keliling_segitiga(a, b, c)

