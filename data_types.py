# dowolną wartość logiczną, 
# dowolną dwuelementową krotkę przechowującą tylko wartości typu int
# dowolną trzyelementową krotkę przechowującą tylko wartości typu str
var1 = True
var2 = (1, 1)
var3 = ('a', 'Tomek', 'test')
var = [var1, var2, var3]

for data in var:
    print(type(data))

print('---')
# dowolny trzyelementowy słownik o wszystkich kluczach typu str
# dowolną trzyelementową listę przechowującą tylko wartości typu str
# dowolny trzyelementowy zbiór przechowujący tylko wartości typu str
    
var4 = {"dog": "pies", "coffee": "kawa", "gym" : "siłownia"}
var5 = ['a', 'b', 'c']
var6 = {'d', 'e', 'f'}


print('---')

# wydrukuj typy podanych zmiennych w podanej kolejności
followers = ['john', 'jane', 'jacob', 'jessica', 'jenny']
profile_picture = 'https://example.com/profile.jpg'
post_ids = [1, 2, 3, 4, 5]
bio = 'Travel enthusiast | Photographer | Nature lover'
timestamp = 1649499360

type_info = [followers, profile_picture, post_ids, bio, timestamp]
my_type_info = []

for data_type in type_info:
    my_type_info.append(type(data_type))
    print(type(data_type))

print('---')

