

def wot(city_name):
    if city_name.count("-") > 1:
        city_name = city_name.replace("-", "", city_name.count("-") - 1)  # - vs -
    return city_name

def wot2(city_name):
    while city_name.count("-") > 1:
        city_name = city_name.replace("-", "", 1)  # - vs -
    return city_name

print( wot("dupa - mapa") )
print( wot("dupa - mapa - kronika") )
print( wot("dupa--mapa") )

print( wot2("dupa - mapa") )
print( wot2("dupa - mapa - kronika") )
print( wot2("dupa--mapa") )