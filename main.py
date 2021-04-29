#import gspread

#gc = gspread.service_account("./login.json")

#sht1 = gc.open_by_key('1EH_i-NzxYkkgBjULl7g1SO4N8QEtc8u__R0n4iGGyIs')

#sht1 = gc.open_by_key('1X7tqWu036hJYexlVUAOHv64eF5Nfn71XGtlYjMxP8lw')
#worksheet = sht1.worksheet("Oxygen")

#worksheet_list = sht1.worksheets()

#values_list = worksheet.get_all_values()
#print(values_list)
from fastapi import FastAPI
import gspread
import json

app = FastAPI()

#Gspred Credentials
gc = gspread.service_account("./login.json")

#SpreedSheet id
sht1 = gc.open_by_key('1X7tqWu036hJYexlVUAOHv64eF5Nfn71XGtlYjMxP8lw')

#Hospitals
hospitalsheet = sht1.worksheet("Hospitals")
hos_title = hospitalsheet.get_all_values()

#Oxygen Sheet
oxygensheet = sht1.worksheet("Oxygen")
oxy_title = oxygensheet.get_all_values()


#Route
@app.get("/")
async def root():
    return {"made": "Gourab"}
    
@app.get("/hospital")
async def root():
    return hos_title


@app.get("/oxygen")
async def root():
    return oxy_title
