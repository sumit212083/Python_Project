import pandas


import pandas

data=pandas.read_csv("911.csv")
#print(data)
#print(type(data))

lat=list(data["lat"])
print(lat)

lng=list(data["lng"])
print(lng)

zip=list(data["zip"])
print(zip)

def colour_producer(zip):
    if (zip<19000.0):
        return("green")
    elif(19000.0<=zip<19300.0):
        return("orange")
    else:
        return("red")