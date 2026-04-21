#ITERABLE: egy objektum ami képes egyesével visszaadni az elemeit (string, list, dict.keys())
#ITERATOR: egy speciális objektum amely egyszerre egy elemet ad vissza egy iterable-ből, iter() functionnel hozzuk létre, és next() function-nel működtetjük
#ITERATION: elemenkénti haladás folyamata, egyik elemről a másikra való eljutás
#LOOP: az iteráció/iteration automatizálása

#példa

#ITERABLE: spotify (vagy bármilyen) lejátszási lista, a kedvenc zenéinkkel
#ITERATOR: mi magunk, akik egyik zeneszámról a másikra tudunk ugrani a next gombbal, tudjuk hogy most melyik szám szól, és képesek vagyunk a következőre ugrani
#ITERATION: következő számra való ugrás a next gombbal
#LOOP: automatikus lejátszás anélkül, hogy mi megnyomnánk a next gombot, egészen addig amíg van zene a listában

#ITERABLE:
playlist = ["Warrior", "I'm a barbie girl", "Heavy is the crown", "I got options"]
#ITERATOR
it = iter(playlist)
print(it)
print(type(it))

#ITERATION
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
