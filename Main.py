import apiCalling
import dataToCsv as dtc
apiData=apiCalling.api_Call()
if apiData:
    dtc.dataToCsv(apiData)
    print("Data from api is successfully written to csv file")
else:
    print("No Data from api found")