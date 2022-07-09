from camelcase import CamelCase

c=CamelCase()

s="Esta oracion necesita CamelCase!"

camelcased= c.hump(s)
print(camelcased)