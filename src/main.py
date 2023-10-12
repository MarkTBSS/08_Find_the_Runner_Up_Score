a = "2 3 6 6 5"
a = a.split()
print(a)
a = [int(i) for i in a]
print(a)

a.sort( reverse=True )
print(a)

b = a[0]
for i in range(len(a)):
    print(str(i) + " : " + str(a[i]))
    if a[i] < b:
        print(a[i])
        break