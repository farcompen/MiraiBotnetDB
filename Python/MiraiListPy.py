#! /usr/bin python3
# -*- coding:utf-8 -*-



import  sqlite3
from datetime import datetime

giris = """
              *********************************
             *                                *
             *        Mirai Botnet            *
             *       İp Veritabanı            *
             *                                *
             *      Faruk GÜNGÖR@2017         *
             *                                *
             **********************************



       """
print(giris)
#buraya db yolu girilecek 
baglanti = sqlite3.connect('DB/MiraiBotnetIpDB.sqlite')
if baglanti:
    print ("bağlantı başarılı")
else:
    print ("bağlantı başarısız")
baslangic = datetime.now()
parametre = """
              *****************************************************
              1- Tüm Veritabanı Listele
              2- Sadece Türkiye İP'leri listele
              3- İlk 1000 Kayıt Getir
              4- İP Ara

             ******************************************************
           """

print(parametre)

secim = input("Seçiminiz : \t")
dbSecim = baglanti.cursor()
sorgu = {1:"Select rowid,ASNINFO,IPAddress,DateFirstSeen,Country from mirai ", 2:"Select rowid,ASNINFO,IPAddress,DateFirstSeen,Country from mirai where Country='TR'", 3:"Select rowid,ASNINFO,IPAddress,DateFirstSeen,Country from mirai  LIMIT 1000", }

sorguNo = int(secim)
kayitGetir = dbSecim.execute(sorgu[sorguNo])
for veriler in kayitGetir.fetchall():
    print('Sıra : %d - ASNBilgi: %s - IP:%s- TespitTarihi : %s - Ulke: %s '%veriler)
    print("")
baglanti.commit()
baglanti.close()
bitis = datetime.now()

total = bitis - baslangic

print ("toplam işlem süresi : {}".format(total))
