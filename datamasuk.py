import operasihitung as oh
data_in = open("input.txt","r")
data = data_in.read().split(',')
menu_awal = int(data[0])
nilai1 = int(data[1])
nilai2 = int(data[2])
nilai3 = int(data[3])
alas = int(data[4])
tinggi = int(data[5])
jari = int(data[6])

if(menu_awal==1):
    print("-------------------------------------------------")
    oh.segitiga(nilai1,nilai2,nilai3,alas,tinggi)
    pass
if(menu_awal==2):
    print("-------------------------------------------------")
    oh.persegi(nilai1)
    pass
if(menu_awal == 3):
    print("-------------------------------------------------")
    oh.lingkaran(jari)
    pass