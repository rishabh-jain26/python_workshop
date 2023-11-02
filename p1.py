'''score=85
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
else:
    print("F")

rain=True
cold=True
if rain:
    print("bring an umbrella.")
    if cold:
        print("wear a jacket.")

num=0
if num>0:
    print("it is positive.")
elif num<0:
    print("it is negative.")
else:
    print("it is zero.")

#set id a unordered collection of unique elements in pythun are sets.
myset={1,2,3,4,5,8}
print(type(myset))
myset.add(31)
print(myset)
myset.remove(2)
print(myset)
myset.discard(2)#if element does not exist it was not raise an error.
print(myset)
myset1={8,10}
print(myset.union(myset1))
print(myset.intersection(myset1))
print(myset.difference(myset1))

def intersection(set1,set2):
    find=set1.intersection(set2)
    return find
set1={"a","b","c"}
set2={"c","d","e"}
print(intersection(set1,set2))'''


