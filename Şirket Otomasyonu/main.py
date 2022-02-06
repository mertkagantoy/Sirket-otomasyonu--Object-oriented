class Sirket():
    def __init__(self,ad): #init fonksiyonu otomatik çalışır ve sınıf çağırılırken parametre olarak girilen isim kaydedilir.
        self.ad = ad
        self.calisma = True #Sınıf dışında bir while döngüsü ile programı sınırsız döngüde çalıştırmak için kullanıcam.

    def program(self):
        secim = self.menuSecim() #Program çalıştırılınca önce işlem girdisini almak için menuSecim fonksiyonunu çağırdık.
                                 #menuSecim fonksiyonundan alınan işlem numarasına göre gerekli fonksiyon çağırılır.
        if secim == 1:
            self.calisanekle()
        if secim == 2:
            self.calisancikar()
        if secim == 3:
            ay_yilSecim = input("Maaş toplamını yıllık bazda görmek istermisiniz ?(EVET/HAYIR)")
            if ay_yilSecim == "EVET":
                self.verilecekmaasgoster(hesap="y")
            else:
                self.verilecekmaasgoster()
        if secim ==4:
            self.maaslariver()
        if secim == 5:
            self.masrafgir()
        if secim == 6:
            self.gelirgir()



    def menuSecim(self): #Bu fonksiyon kullanıcıdan işlem girdisini alıcam.
        secim = int(input('**** {} otomasyonuna hoş geldiniz ****\n\n1-Çalışan Ekle\n2-Çalışan Çıkar\n3-Verilecek maaş göster\n4-Maaşları Ver\n5-Masraf Gir\n6-Gelir Gir\nSeçiminizi Giriniz:'.format(self.ad)))
        while secim<1 or secim>6:
            secim = int(input("Lütfen 1 - 6 arasında belirtilen seçeneklerden birini giriniz:"))
        return secim

    def calisanekle(self):
        id = 1
        ad = input("Çalışanın adını giriniz:")
        soyad = input("Çalışanın soyadını giriniz:")
        yas = int(input("Çalışanın yasını giriniz:"))
        cinsiyet = input("Çalışanın cinsiyetini giriniz:")
        maas = int(input("Çalışanın maasını giriniz:"))

        with open("calısanlar.txt","r") as dosya:
            calisanlistesi = dosya.readlines()
        if len(calisanlistesi) == 0:
            id = 1
        else:
            with open("calısanlar.txt","r") as dosya:
                id = int((dosya.readlines()[-1].split(")")[0])) + 1

        with open("calısanlar.txt","a+") as dosya:
            dosya.write("{}-){}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))



    def  calisancikar(self):
        with open("calısanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        gcalisanlar = []

        for calisan in calisanlar:
            gcalisanlar.append(" ".join(calisan[:-1].split("-")))

        for calisan in gcalisanlar:
            print(calisan)
        secim = int(input("Lütfen çıkarmak istediğiniz çalışanın numarasını giriniz.(1-{} arasında".format(len(gcalisanlar))))
        while secim < 1 or secim > len(gcalisanlar):
            secim = int(input(" Lutfen (1-{}) arasında bir numara giriniz".format(gcalisanlar)))
        calisanlar.pop(secim-1)

        dcalisanlar = []

        sayac = 1
        for calisan in calisanlar:
            dcalisanlar.append(str(sayac) + ")" + calisan.split(")")[1])
            sayac += 1
        with open("calısanlar.txt","w") as dosya:
            dosya.writelines(dcalisanlar)



    def verilecekmaasgoster(self,hesap = "a"):
        """hesap: a ise aylık , y ise yıllık hesep"""
        with open("calısanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        toplam = 0
        for  topla in maaslar:
            toplam = toplam + int(topla)
        if hesap=="a":
            print("Bu ay toplam {} TL maaş verilicek".format(toplam))
        else:
            print("Bu yıl ödenecek toplam maas {} TL'dir".format(toplam*12))




    def maaslariver(self):
        with open("calısanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        maas_toplam = 0
        for maas in maaslar:
            maas_toplam = maas_toplam + int(maas)
        ### Bütçeden maasi alma ve bütçeyi yenileme ###
        with open("butce.txt","r") as dosya:
            butce = int(dosya.readlines()[0])
        butce = butce - maas_toplam

        with open("butce.txt","w") as dosya:
            dosya.write(str(butce))

    def masrafgir(self):
        masraf_nedeni = input("Lütfen masraf nedenini yazınız.")
        masraf = int(input("Lütfen masrafı giriniz"))
        id = 1
        with open("masraflar.txt","r") as dosya:
            masraflistesi = dosya.readlines()

        if len(masraflistesi) == 0:
            id = 1
        else:
            with open("masraflar.txt","r") as dosya:
                id = int((dosya.readlines()[-1].split(")")[0])) + 1

        with open("masraflar.txt","a+",encoding="utf-8") as dosya:
            dosya.write("{})Masraf nedeni: {} , Masraf: {}\n".format(id,masraf_nedeni,masraf))

        with open("butce.txt","r") as dosya:
            butce = int(dosya.readlines()[0])

        butce = butce - int(masraf)

        with open("butce.txt","w") as dosya:
            dosya.write(str(butce))


    def gelirgir(self):
        gelir_nedeni = input("Lütfen gelir nedenini yazınız.")
        gelir = int(input("Lütfen geliri giriniz"))
        id = 1
        with open("gelirler.txt", "r") as dosya:
            gelirlistesi = dosya.readlines()

        if len(gelirlistesi) == 0:
            id = 1
        else:
            with open("gelirler.txt", "r") as dosya:
                id = int((dosya.readlines()[-1].split(")")[0])) + 1

        with open("gelirler.txt", "a+",encoding="utf-8") as dosya:
            dosya.write("{})Gelir nedeni: {} , Gelir: {}\n".format(id, gelir_nedeni, gelir))

        with open("butce.txt","r") as dosya:
            butce = dosya.readlines()[0]

        butce = int(butce) + gelir

        with open("butce.txt","w") as dosya:
            dosya.write(str(butce))

#sirket_adi = input("Lütfen şirket adını giriniz:") ŞİRKETİN ADINI
sirket = Sirket("MERT")
while sirket.calisma:
    sirket.program()







