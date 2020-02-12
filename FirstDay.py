23
4567
2.3
(10+2j)

5+2
25*25
5/2
10-3
34567
"34567"
type(34567)

type("34567")

23+65
# burda daha farklı bir islem soz konusu
"23"+"65"

45+"45"
#karakter dizisi ile sayılar toplanamaz
#SAYI ILE SAYI TOPALANIR

45+45
# KARAKTER İLEDE KARAKTER + ISARETİ İLE BİRLEŞTİRİLİR

"istizha."+"com"

# " * " İSARETİ BİR KARAKTER DİZİSİ İLE YAN YANA KOYULUP SAI GİRİLİRSE GİRİLEN SAYI AKDAR O DİZİYİ TERKRARLAR */
"w"*3
25*3

#some basic functions len()  type();
#len for calculate he legth of the string
#type for take a output of variable type name


len("hilmi_ozdemir_1998")

len("rT%65#$hGfUY56123")
#we want to control the user name and pass word lengt shouldnt be over than 40

len("hilmi_ozdemir_1998"+"rT%65#$hGfUY56123")
#as you seee output is 35 len is numerical variable 
#that my comment

type(len("rT%65#$hGfUY56123"))
# as you can see cvlass is int

# değer atama gösteriyo
n=5
#burda n'e 5 değerini atadık ve artık 5 ile ytapılcak hgerahangi bir işlemde sadece "n" değerini çağırarak işlem yapabiliriz
# KENDİ NOTUM DEĞERİ ATADIKTAN SONRA SHIFH ENTER İLE ATADIKTAN SORA SHELLİ CALISTIR KI GORSUN

n*2 
#gordugunuz gibi n *2 ye 10 degerini verdim
n*10
n/2

#şimdide pi değerini atıyacağız pi ye>;

pi=3.14
pi+n

username="Hilmi_ozdemir_1998"
password="rT%65#$hGfUY56123"


len(username)
len(password
len(username)+len(password)
u_length=len(username)
p_legth=len(password)

type(u_length)

# atanılan degerler sayi ile baslayamaz karakteristik array olmak zorunda sayi ile baslayamaz
#yanlis
#   ""3_kilo_elma="5tl""" bu kullanım yalnistir  yukardaki sebepten oturu
#doğrusu
kilo_elma="5TL"
#yalnis
#+deger=456
#dogrulari
_deger=4568
deger=4568

#degisken adi olrak kullanılmıcak kelimeler---------------------------------------------------------------------------------------------------------------------------------------------
'or','False','None','True', 'and','assert','break','class','continue','def','del','elif','else','expect','finally','for','from','in'
'not''pass','raise','return','try','while','with','yield','is','lambda ','nonlocal','if','import ','in','global',' if',' import','as'
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Examples
elif="Hos Kız"
as="kare"
False=45
error="File <stdin>line 1"
eror="SyntaxError:assignment to keyword"

# >>> import keyword
# >>> keyword.kwlist
import keyword
keyword.kwlist
# bu komut asagıdaki kullanılmayan Değer atanan listesini otomatik gösterir burdan barakarak pğropgramınızın daha rahat calısabilmesini safglayabnilirsinizi


len(keyword.kwlist)

kk=keyword.kwlist
len(kk)

#type ve len ismindeki değertlşer atarsanız bu fonksiyonları kkodun icinde bir daha kullanamazsınız

type="elma"

type(234)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'str' object is not callable
# bu eroru alırısınız cunki daha ocne bu isimde bir deger atamsı yapmısınmızdır


# del type kullanarak eski halşine getirebilirsiniz ya da type ı tanımalşdıgınız shelli ac klapa yaprak tekrardan aktif hale getirebilirisiniz
#misal
del type
type(23423)
#ouput <class 'int'>


# degisken adı olustururken aradca bosluk kullanamazsınız
#dogru
kullanici_adi="elma"
#yanlis
#kullanici adi=elma
# yada 2. dogru
kullaniciAdi="elma"
personelSayisi=45
sayı=45
#degisken isimlerini kısa ama betimleyici tutmak guzeldir

 a=3456578
# bu iki degiskende hic hos durmuyor değil mi biri fazla kısa digeri fazla uzundur
 türkiye_büyük_millet_meclisi_millet_vekili_sayisi=550
#onun yerine soyle yapsak
tbmm_mv_sayisi=550
# best case
#________________________________________________________________________________________________________________________________________________________________________
# Odev zamanı Proje :Aylik yol masrafinizi hesaplamak uzere bir program yapıyoruz
# Pazar haric tum gunler calisiyoruz (Her ay icin gecerli değil ama 1 aydan pazar günlerini cıkarırsak eger) geriye 26 gun kalir
# evden okula giderken günlük 1 dolmus 1 metrobüs yapıyoruz
# okuldan eve donerken 1 metrobüs 1 dolmus yapiyoruz
# ana hesapta yapılması gereken algoritma 26*(1metrobus +1 dolmus)+(1dolmus +1metrobüs))=aylik ulaşim masrafimiz
# tanimlanması gerek değişkenler  gun sayisi , metrobus ,dolmus ,gidis ,gelis,aylik masraf
gunSayisi=26
Metrobus=1.25
Dolmus=1.25
gidis=Dolmus+Metrobus
gelis=Metrobus+Dolmus
aylikMasraf=gunSayisi*(gidis+gelis)
print(aylikMasraf)
#out put 130

#bitiş
#eğer aylik masraf degiskeninde parantezleri kullanmasak ne olurdu bakalım
aylikMasraf1=gunSayisi*gidis+gelis
print(aylikMasraf1)
#out put 67.50
#___________________________________________________________________________________________
#Odev Zamani Proje:Daire alani cevresini hesaplayan Program
#Onceden belirli tek bir sey var bu da pi sayisi once onu belirliyip "pi" ye eşitleyelim 
#Cevre icin 2*pi*r
#alan icin pi r^2
#r=yaricap icin R/2
#bize gereken degerler R  r pi
R=5
r=R/2
pi=3.1415
alan=pi*r*r
cevre=2*pi*r
print("Cap R=",R,"Alan=",alan,"dir","Çevresi ise =",cevre)
#mission complated    alan= 19.634375000000002
#:D
#____________________________________________________________________________________________
# Kare Küp üslü sayilar icin Pyhtonun bazı Extra guzel Ozellikleri
#mesela 12 nin karesini almak isterken
12**2 
#144
#küpü için
12**3
#1728
#karakökü icin 
144**0.5
#12
#üzeri 4 icin
12**4
#20736
alan=pi*(r**2)
print(alan)
#ayni değer yukardaki ile 19.634375000000002
#_____________________________________________________________________________________________
#YENİ FONKSIYON POW FONKSİYON
pow(12,2)
#144
pow(23,3)
#12167
pow(144,0.5)
#12
#yukarda anlatılan üst kok alma işaretini bir fonksyion olarak kullanmak  istersen kullan
#POW FONKSİYONUN FARKLI OLARAK BİR OZELLİGİ DAHA VARDIR
#3. BİR PARAMETRE ALARAK FARKLI İSLEMLER YAPILABİLİR DENİYORUM 1 DK :)
pow(16,2,2)
# 0
#bunun anlamı 16 nın 2 ci kuvvetini al sonra 2 ye bolumunden kalanı verir
pow(16,2,3)
#1
#______________________________________________________________________________________________

#ESİT DEGERDE 2 DEGİSKEN TANIMLAMA

A=4
B=4
#OKEY BİR DURUM AMA SU SEKİLDE YAPRSAK DAHA KOLAY OLACAKTIR
A=B=4

ocak=mart=mayıs=temmuz=agustos=ekim=aralik=31
nisan=harizan=eylül=kasım=30
şubat=28

#_________________________________ First Day Finished_________________________










