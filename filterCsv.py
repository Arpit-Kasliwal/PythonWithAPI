import csv
with open("userData.csv","r") as csvFile:
    reader=csv.DictReader(csvFile)
    readerList=list(reader)
    newList=[]
    # for user in readerList:
    #     user.pop("email")
    #     user.pop("WithAddressGeo")
    for user in readerList:
        userDict={
            "Fullname":user["Fullname"],
            "Company":user["Company"]
        }
        newList.append(userDict)    
    with open("filteredUserData.csv","w",newline="") as newCsvFile:
        fieldnames=["Fullname","Company"]
        writer=csv.DictWriter(newCsvFile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(newList)
