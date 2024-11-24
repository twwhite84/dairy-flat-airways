# this was used to convert the supplied customers csv file to a json fixture

import csv
import json

my_data = []

with open("customers.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        new_dict = {}
        fields_dict = {}
        new_dict["model"] = row["model"]
        new_dict["pk"] = row["pk"]
        fields_dict["code"] = row["code"]
        fields_dict["title"] = row["title"]
        fields_dict["first_name"] = row["first_name"]
        fields_dict["last_name"] = row["last_name"]
        fields_dict["gender"] = row["gender"].capitalize()
        fields_dict["email"] = row["email"]
        new_dict["fields"] = fields_dict
        my_data.append(new_dict)

json_str = json.dumps(my_data)
with open('customers.json', 'w') as fw:
    fw.write(json_str)