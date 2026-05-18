room = {
    "name": "Speechlab",
    "location": "2nd Floor, ICAS Bldg.",
    "n_computers": 24,
    "n_chairs": 25,
    "is_airconed": True
}

# accessing
print(room['name'])

# updating
room['name'] = "Speechlab"

# insertion
room['n_tv'] = 1

# method
print(room.keys())