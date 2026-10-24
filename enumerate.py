fruits=["apple","banana","cherry"]
for index, fruit in enumerate (fruits):
    print(index,fruits)

fruit=["apple","banana","cherry"] 
for index, fruit in enumerate (fruits, start=1):
    print(index,fruits)

    fruit=["apple","banana","cherry"] 
for index, fruit in enumerate (fruits, start=0):
    print(index,fruits)