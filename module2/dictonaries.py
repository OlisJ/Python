#collection of items, mutable, not indexable, works on a pair key:value
contact_info={
    "Alma":"049123456",
    "Erin":"049654321"
}
print(contact_info)
alma_info=contact_info["Alma"]
print(alma_info)
contact_info["Orkidea"]="049000123"
print(contact_info)
del contact_info["Orkidea"]
print(contact_info)
keys=contact_info.keys()
print(keys)
valuesci=contact_info.values()
print(valuesci)
items=contact_info.items()
print(items)