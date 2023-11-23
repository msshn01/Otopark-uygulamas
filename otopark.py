import json
import os
import time






class Araçlar:
    def __init__(self,plaka,tür,saat,dk):
        self.plaka = plaka
        self.tür = tür
        self.saat = saat
        self.dk = dk




class OtoYönetim:
    def __init__(self) -> None:
        self.kullanicilar=[]
        self.loadaraç()
    
    def loadaraç(self):
        if os.path.exists("cars.json"):
            with open("cars.json","r",encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newuser = Araçlar(plaka=user["plaka"],tür=user["tür"],saat=user["saat"],dk=user["dk"])
                    self.kullanicilar.append(newuser)


    
    def giriş(self,car:Araçlar):
        self.kullanicilar.append(car)
        liste = []    
        for user in self.kullanicilar:
            a = json.dumps(user.__dict__)
            liste.append(a)


        with open("cars.json","a",encoding="utf-8") as file:
                json.dump(liste,file)



    def çikiş(self,plaka):
        for i in self.kullanicilar:
            if i.plaka == plaka:
                if i.tür == "s":
                    dakika = ((time.localtime().tm_hour) - i.saat)*60 + ((time.localtime().tm_min) - i.dk)
                    ucret = dakika*0.5
                    print(f"geçirilen süre : {dakika} \nAraç türü:{i.tür} \n fiyat : {ucret} TL")
                else:
                    dakika = (i.saat) * 60 + i.dk
                    ucret = dakika*1
                    print(f"geçirilen süre : {dakika} \nAraç türü:{i.tür} \n fiyat : {ucret} TL")
            else:
                continue
                     
            


                
        













kontrol = OtoYönetim()



while True:
    print("**************menü****************")
    seçim = input("1-Giriş \n2-Çıkış \n3-Ücret tarifesi \nq-Quit \nSEÇİMİNİZ: ")
    if seçim == "q":
        break
    else:
        if seçim == "1":
            plaka = input("plaka(38-agp-456): ")
            tür = input("tür(s/k): ")
            saat = time.localtime().tm_hour
            dk = time.localtime().tm_min
            user = Araçlar(plaka=plaka,tür=tür,saat=saat,dk=dk)
            kontrol.giriş(car=user)

        elif seçim =="2":
            x = input("plaka(38-agp-456): ")
            kontrol.çikiş(plaka=x)
        elif seçim == "3":
            print("s==>sedan=====>0.5 dk/tl")
            print("k==>kamyon=====>1 dk/tl")

        else:
            print("geçersiz giriş")
    


    


        
   
       

        



















    
