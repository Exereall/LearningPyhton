#2. gundeyiz bugun hedefi 56-112 arası  kitabımızı okumak ve uygulamak
#bir onceki kodtan ayların gun sayisini cekiyorum
ocak=mart=mayıs=temmuz=agustos=ekim=aralik=31
nisan=harizan=eylül=kasım=30
şubat=28
#şimdi bir odev yapalim yukarda aylara atadıgımız gun degerleri ile bir şeyler hesaplayalım
#Proje konusu aylık Doğalgaz masrfımızı Hesaplamanın kolay bir yolu olsun

aylik_sarfiyat=346
fatura_tutari=273.87

birim_fiyat=fatura_tutari/aylik_sarfiyat
birim_fiyat
#birim_fiyat...0.7915317919075144

günlük_sarfiyat=aylik_sarfiyat/mart
günlük_sarfiyat
#output 11.161290322580646
nisan_faturasi=birim_fiyat*günlük_sarfiyat*nisan
nisan_faturasi
#output 265.03548387096777
şubat_faturasi=birim_fiyat*günlük_sarfiyat*şubat
şubat_faturasi
#output 247.36645161290326
#günlük sarfiyat değerini sonradan değiştirirsek  mesela 15 yapasak tum değerler değişir
#_______________________________________________________________________________________
#DEGİSKEN DEGERİNİ TAKAS ETME
osman="Arastirma Geliştirme Müdürü"
mehmet="Proje Sorumlusu"
osman
#output osman=Arastirma Geliştirme Müdürü
mehmet
#output mehmet=Proje Sorumlusu
#_______________________________________________________________________________________
#Değişken değeri takası
osman,mehmet=mehmet,osman
osman
#output osman=Proje Sorumlusu
mehmet
#output mehmet=Arastirma Geliştirme Müdürü
#_______________________________________________________________________________________
#5.1 ETKILESIMLI KABUKTA ILK ADIMLAR
osman="Arastirma Geliştirme Müdürü"
mehmet="Proje Sorumlusu"
geçici="Proje Sorumlusu"
mehmet=osman
mehmet
#out put Arastirma Geliştirme Müdürü
osman
#out put Arastirma Geliştirme Müdürü
osman=geçici

osman
#output Proje Sorumlusu
mehmet
#output Araştirma Geliştirme Müdürü
a=1
b=2

# eğer c de olsaydık yukardaki gibi bir islem ile transfer takas gerçekleştirebiliridik
# fakat biz direk bu şekilde yani aşağıdaki gibi yaparak  transferi gerçekleştiriyoruz 
a,b=b,a
b,a=a,b
#______________________________________________________________________________________
#Ogrendiklerimizi hatırlayalım len ve pow adında iki fonksiyon ve "**" işlecini öğrenmiştik
# şimdi len() fonkisiyonunun bazı kısıtlamalarını öğrenicez len ile ne yapıyorduk?

kelime="muvaffakiyet"
len(kelime)
#output 12
#unutmamak gerek biz len fonksiyonu ile sayiların uzunlugunu ölçmüyoruz bu fonksiyon bize
#characteristic array lerin uzunlugunu olcuyor yani su sekil bir kullanım
len(233423)

#kesinlikle yalnistir
#ve     Traceback (most recent call last) TypeError: object of type 'int' has no len() 
#hatasını verir

# etkileşimli kabukta alt yatay çizgi tire "_" bir onceki yapılan işlemin sonucunu verir

2345+54355
#out put 56700
   _
#output 56700
_+25
#output 56725
_
# üzerine ek bir islem yapildiğinda bir değişken gibi aynı outputu verir output 56725

# _ komutu sadece sayi icin değil aynı zamanda karakterde tutar
"wwww"
#output 'www'
_
#output 'www'
_+".istizha.com"
#output 'www.istizha.com'
# sadece shellerde kullanılır kabuk ortamı dısında geçerliliği yoktur aq niye anlattın o zaman
# PRİNT() FONKSİYONU  MILE STONE 1

#onceden su sekilde calisiyorduk
"Phyton programlama dili"
6567
# bunları yazınca kendilerinin outputların alıyorduk ama artık
#bunlar pyhtonun ekrana cıktı verebilmesi icin yeterli değildir
#bu kodları dosyaya kaydedip calıstırdımızda calismaz
#bunların cıktısı almak icin print() function kullanıyoruz
print("Pyhton Programlama dili")
#alttaki sekildede kullanabilirsiniz
dil="Phyton programlama dili"
print(dil)
#Pyhton bize 3 çeşit tırnak çeşidi sunar
#TIRNAKLAR
#Tek tırnak ('')
#Çift tırnak ("")
#üç tırnak (""" """)

print('Pyhton programlama dili')
print("Pyhton Programlma dili")             # hepsinin outputu ayni
print(""" Pyhton Programlama Dili""")
#Peki fark ne?
#mesela soyle bir ornek vermek istiyorsunuz 
#Pyhton programlama dilinin adı "piton" yılanından gelmez
print("Pyhton programlam dilinin adı "piton" yılanından gelmez.")
#hatalı bir kodlamadır ve invalid  syntax error verir
print('Pyhton programlama dilinin adı "piton " yılanından gelmez.')
# bu doğru bir kullanımdır  diğerini 2 adet cift tırnak oldugundan ayırt edemez
#2. orengimizde ise
print('İstanbul'un 5 gunluk hava durum tahmini')
#burdada pyhton size syntax invalid error vericektir
#aynı sebepten dolayıdır
print("İstanbul'un 5 gunluk hava tahmini")
#bu kullanımsa doğrudr peki 3 tırnak neden var diye sorarsanız
#3 tırnakla asagıdakileri yapabilrisiniz ve hepsinde sorunsuz calısır
print(""" İstanbul'un 5 gunluk hava durum tahmini """)
print("""Pyhton programlam dilinin adı "piton" yılanından gelmez. """)
# ikiside dogru kullanımlardır ve dogru sonucu verir peki  o zaman ben hep 3 tırnak kullanıyım
#diyebilirsiniz
#ama 3 tırnağın asıl kullanım yeri asagıdaki gibi coklu karakter dizisine sahip seyler
#bastırırken kullanılır
print("""
[ hbo]================[hbo][-][o][X]
I                                  I    
I       Programa Hos geldiniz      I
I          sürüm 0.8               I  
I     Devam etmek icin her hangi   I                         
I       bir tusa basiniz           I
I==================================I
""")
print(""".
Game over 
insert coin
""")
#diğer tırnaklarla bunu yapamazsınız
#print bir fonsiyondur ve tıpkı len ve pow gibi () içindeki parametreler ile kullanılır
print('En az 8 haneli bir parola belirleyin')
print('fırat','ozgul')# burda aynı pow fonksiyonu gibi parcalara bolundugunu gorebilirsiniz

print("Pyhton","Programlama","Dili")
#output Pyhton Programlama Dili

print ('Fırat','ozgul','Adana',1980)

#output Fırat Özgül Adana 1980
# hangi tırnak tipi ile basladıyysanız virgüle yada soana kadar o tırnak tipi ile gitmeniz onemlidir
print("Karakter dizisi')
print('karakter dizisi")
#bunlar yalnistir
#PARAMETRELERİ

#6.4.1
#SEP

print('Fırat','ozgul')

print("Pyhton","Php","C++","C","Erlang")
#print fonksiyonunda virgulle beraber direkt olarak bosluk verir
#output:Pyhton Php C++ C Erlang
#çogu zaman ise yarasada bazen yaramaz mesela

print("http://","www",".","istizha",".","com")
# out put http:// www . istizha . com  gibi 
# bu durumlarda ne yapmalıyız?
#print fonksiyonunu özelleştiririz
print("Mehmet","Öz","İstanbul","Çamlıca",156,"/",45)
#Pyhtonda print fonksiyonun icinde hep sep parametresi vardır gorunmese bile ordadır
print("http://","www",".","istizha",".","com",sep=" ")# gorunmeyen default hali boyledir
print("http://","www",".","istizha",".","com",sep="") #boslugu dusurup 0 bosluga inidirince
#output istediğimiz olur :http://www.istizha.com
#Tek kullanım alanı bosluk degildir
# . koyabilirsiniz ya da virgül ne isterseniz ozel kullanılmıcak degerler haric sanırım deneyelim
print("t","c" ,sep=".")
#output t.c
print("t","c",sep='as')# kullanılabiliyormus :d
print("t","c",sep='\n') # bu kitapta yoktu ama bu sekilde alt alta alabilirsiniz ama """ """ yeterlidir
print("t","c",sep=0) #düz sayı değeri konulamaz ama tırnak icinde septe kullanılabilir
print("t","c" ,sep=None)
# normal default hali ile aynı islemdir
#END
#bu kadar detaycı olmama kararı alındı ileride 19 gun sonunda update edilecek ve duzeltilecek
# 4 te kalkılıp devam edilecek ders baslayana kadar



















