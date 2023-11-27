import json

data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}
data_json = json.dumps(data, indent=4)
print(data_json)


talaba_json = """{"ism": "Hasan", "familiya": "Husanov", "tyil": 2000}"""
talaba = json.loads(talaba_json)
print(talaba['ism'], talaba['familiya'])
