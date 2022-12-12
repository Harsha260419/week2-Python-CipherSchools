mixed = (1,2,3,4,'six')
mixed2 = (1,2,3,[4,5,6])
mixed2[3].pop()
print(mixed2)
print(len(mixed2))
# when we make big programs we don't insert lists in tuples it effects the performance