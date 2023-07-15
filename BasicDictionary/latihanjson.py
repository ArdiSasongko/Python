import json

data = {
    "Name": "Paeno",
    "Age": 55,
    "Hobbies": [
        "Basketball", "Football"
    ],
    "Family": {
        "Father": "Karyowijoyo",
        "Mother": "Sainem"
    },
    "Married": True
}

json_data = json.dumps(data)
person = json.loads(json_data)

print(json_data)
print(person["Family"])
