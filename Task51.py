num = [23, 4, '4', 'dgdg', 0.45, 'zzxx']
spis1 = list(filter(lambda x: type (x) != str, num))
spis2 = list(filter(lambda x: type (x) == str, num))
print (spis1, spis2)