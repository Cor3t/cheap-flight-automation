names = [
    {
        "name": "john"
    },
    {
        "name": "james"
    },
    {
        "name": "joan"
    },
]

new_names = [name["name"].capitalize() for name in names]

# for name in names:
#     new_names.append(name.capitalize())

print(new_names)


