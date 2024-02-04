import random


def loe_failist(f):
    fail = open(f, 'r', encoding="utf-8")
    mas = []
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas


def kirjuta_faili(f: str, mas: list):
    fail = open(f, 'w', encoding='utf-8')
    for sõna in mas:
        fail.write(sõna + '\n')
    fail.close()


def lisa_sõna(sõna, keel):
    rus: list = loe_failist("rus.txt")
    est: list = loe_failist("est.txt")
    if keel == 'русский':
        if sõna in rus:
            print(f"Слово '{sõna}' уже есть в русском словаре.")
            return 0
        else:
            rus.append(sõna)
            kirjuta_faili('rus.txt', rus)
            print(f"Слово '{sõna}' добавлено в русский словарь.")
            return 1
    elif keel == 'eesti':
        if sõna in est:
            print(f"Sõna '{sõna}' on juba eesti sõnastikus.")
            return 0
        else:
            est.append(sõna)
            kirjuta_faili('est.txt', est)
            print(f"Sõna '{sõna}' lisati eesti sõnastikku.")
            return 1
    else:
        return 0


def paranda_sõna(vana_sõna, uus_sõna, keel):
    rus: list = loe_failist("rus.txt")
    est: list = loe_failist("est.txt")
    if keel == 'русский':
        if vana_sõna in rus:
            i = rus.index(vana_sõna)
            rus[i] = uus_sõna
            kirjuta_faili('rus.txt', rus)
            print(f"Слово '{vana_sõna}' исправлено на '{
                  uus_sõna}' в русском словаре.")
        else:
            print(f"Слово '{vana_sõna}' не найдено в русском словаре.")
    elif keel == 'eesti':
        if vana_sõna in est:
            i = est.index(vana_sõna)
            est[i] = uus_sõna
            kirjuta_faili('est.txt', est)
            print(f"Sõna '{vana_sõna}' parandati '{
                  uus_sõna}' peale eesti sõnastikus.")
        else:
            print(f"Sõna '{vana_sõna}' ei leitud eesti sõnastikust.")
    else:
        print("Palun valige keel.")


def kontrolli_sõnu(keel):
    jatk = str
    õiged = 0
    valed = 0
    while jatk!='2':
        rus: list = loe_failist("rus.txt")
        est: list = loe_failist("est.txt")
        if keel == 'русский':
            sõna = random.choice(rus)
            print(f"Как перевести слово '{sõna}' с русского на эстонский?")
            vastus = input().lower()
            rus_index = rus.index(sõna)
            tõlgi_sõna = est[rus_index]
            if vastus == tõlgi_sõna:
                print("Верно!")
                õiged += 1
            else:
                print(f"Неверно. Правильный ответ: {tõlgi_sõna}")
                valed += 1
        elif keel == 'eesti':
            sõna = random.choice(est)
            print(f"Kuidas tõlkida sõna '{sõna}' eesti keelest vene keelde?")
            vastus = input().lower()
            est_index = est.index(sõna)
            tõlgi_sõna = rus[est_index]
            if vastus == tõlgi_sõna:
                print("Õige!")
                õiged += 1
            else:
                print(f"Vale. Õige vastus: {tõlgi_sõna}")
                valed += 1
        jatk = input("Продолжать (1) или выйти (2) из словаря? ") 
    return round((õiged/(õiged+valed)*100),0)


def näita_menüüd(menüü):
    numbrid = sorted(menüü.keys())
    for number in numbrid:
        print(f"{number}. {menüü[number]}")
    valik = input("Palun valige number: ")
    if valik in numbrid:
        return valik
    else:
        print("Vigane number. Palun proovige uuesti.")
        return None


menüü = {}
menüü['1'] = "Sõnade õppimine."
menüü['2'] = "Lisa sõna."
menüü['3'] = "Paranda sõna."
menüü['4'] = "Kontrolli sõnu."


def oppimine():
    with open("rus.txt", "r", encoding="utf-8") as rus_file, open("est.txt", "r", encoding="utf-8") as est_file:
        rus_sonad = rus_file.read().splitlines()
        est_sonad = est_file.read().splitlines()
        i = 0
        while i < len(rus_sonad) and i < len(est_sonad):
            print(f"Русское слово: '{
                  rus_sonad[i]}', Эстонское слово: '{est_sonad[i]}'")
            jarkmine = input("Продолжить? (Введите '1'): ")
            if jarkmine != "1":
                break
            else:
                i += 1
