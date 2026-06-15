import csv
def dataToCsv(data):
    listOfDicts=[]
    for user in data:
        userDict={
            "Fullname":user['name'],
            "email":user['email'],
            "WithAddressGeo":user["address"]["city"]+","+user["address"]["geo"]["lat"]+","+user["address"]["geo"]["lng"],
            "Company":user["company"]["name"]+","+user["company"]["catchPhrase"]
        }
        listOfDicts.append(userDict)        
    with open("userData.csv", "w", newline="") as csvFile:
        fieldnames=["Fullname","email","WithAddressGeo","Company"]
        writer =csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(listOfDicts)