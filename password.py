import time, getpass, sys, json, os, random, string

nekru = [
    "Moro",
    "mds"
]

def passwordsaverStart():
    print("❗Password saver❗")
    print("N = Tee uusi salasana🔐")
    print("U = Tee random salasana 🗝")
    print("K = Katso vanhat salasanasi🔑")
    print("P = Poistu❔")
    newPassword = input("Aseta toiminto: ")
    if newPassword == "N" or newPassword == "n":
        createPassword()
    if newPassword == "U" or newPassword == "u":
        randomPassword()
    if newPassword == "K" or newPassword == "k":
        showPasswords()
    if newPassword == "P" or newPassword == "p":
        sys.exit("Closed")

def showPasswords():
    if not os.path.exists("sala.json"):
        print("Ei tallennettuja salasanoja.")
        return

    with open("sala.json", "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("Tiedosto on tyhjä tai virheellinen.")
            return
        
    if len(data) == 0:
        print("Ei tallennettuja salasanoja.")
    else:
        print("Tallennetut salasanat:")
        for entry in data:
            print(f"Otsikko: {entry['otsikko']}, Salasana: {entry['salasana']}")



        
def createPassword():
    passwordTopic = input("Aseta otsikko: ")

    time.sleep(1)
    hidePas1s = getpass.getpass(prompt='Password: ', stream=None)
    hidePas2s = getpass.getpass(prompt='Confirm Your Password: ', stream=None)

    if hidePas1s != hidePas2s:
        print("Salasanat eivät täsmää! Yritä uudelleen.")
        return  

    password_entry = {
        "otsikko": passwordTopic,
        "salasana": hidePas1s
    }

    if os.path.exists("sala.json"):
        with open("sala.json", "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(password_entry)

    with open("sala.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Salasana '{passwordTopic}' tallennettu onnistuneesti!")

passwordsaverStart()