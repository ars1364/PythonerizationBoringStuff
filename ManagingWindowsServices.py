import wmi
import csv

serviceName = 'service'
with open('IPList.csv', 'r', newline='') as confFile:
    csvReader = csv.reader(confFile, delimiter='|')
    for fileLines in csvReader:
        w = wmi.WMI(fileLines[1], user=r"admin", password="admin1234")
        for service in w.Win32_Service():
            if serviceName.lower() in service.DisplayName.lower():
                print(service.StopService())
