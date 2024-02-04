from  functions import *
import random

vastus = input("Kas sina sovid õppida? ja = 1 /ei = erinivad: ")
if vastus == '1':
    while True:
        option = näita_menüüd(menüü)
        if option == '1':
            oppimine() 
            jatk = input("Продолжать (1) или выйти (2) из словаря? ") 
            if jatk =='2':
                print("Head aega!")
                break

        elif option == '2':
            otsus = 0
            while otsus < 3:
                keel = input("Mis keeles? Eesti või Русский?: ").lower()
                sõna = input("Sisestage uus sõna: ").lower()
                arv = lisa_sõna(sõna, keel)
                otsus += arv
                if otsus == 1:
                    print("Пожалуйста введи слово на другом языке")
                    otsus +=1
                elif otsus == 0:
                    print("Palun veel kord")
            jatk = input("Продолжать (1) или выйти (2) из словаря? ") 
            if jatk =='2':
                print("Head aega!")
                break
        elif option == '3':
            vana_sõna = input("Sisestage vana sõna: ").lower()
            uus_sõna = input("Sisestage uus sõna: ").lower()
            keel = input("Mis keeles? Eesti või Русский?: ").lower()
            paranda_sõna(vana_sõna, uus_sõna, keel)
            jatk = input("Продолжать (1) или выйти (2) из словаря? ") 
            if jatk =='2':
                print("Head aega!")
                break
        elif option == '4':
            keel = input("Mis keeles? Eesti või Русский?: ").lower()
            tulemus = kontrolli_sõnu(keel)
            print(f"Ваш результат {tulemus}%")
            jatk = input("Продолжать (1) или выйти (2) из словаря? ") 
            if jatk =='2':
                print("Head aega!")
                break
            
else:
    print("Head aega!")
    exit