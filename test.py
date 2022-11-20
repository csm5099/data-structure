obj1 = "사과"
obj2 = "바나나"

id_obj1 = id(obj1)
id_obj2 = id(obj2)

print(f"{obj1} {obj2}")
print(f"{id_obj1} {id_obj2}")

obj1 = obj2

id_obj1 = id(obj1)
id_obj2 = id(obj2)

print(f"{obj1} {obj2}")
print(f"{id_obj1} {id_obj2}")