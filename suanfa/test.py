# a=[1,2,3,3,5,6]
# for i in range(len(a)-1):
#     for k in range(i+1,len(a)):
#         if a[i] == a[k]:
#             print(a[i])

#len(a)-1  1 2 3 3 5

#a[i]=1 i=0  k=1-5   a[k] = 2 3 3 5 6
#a[i]=2 i=1  k=2-5   a[k] = 3 3 5 6
#a[i]=3 i=2  k=3-5   a[k] =3 5 6
#a[i]=3 i=3  k=4-5   a[k] =5 6
#a[i]=5 i=4  k=5-5   a[k] =6

#5 4 3 3 2 2 2  5x5
#4 3 3 2 2 2    4x4
#3 2 2 2        3x3
#2 2            2x2
#a[0][0] a[0][1] a[0][2] a[0][3] $$ a[1][3] a[2][3] a[3][3] $$
#a[3][2] a[3][1] a[3][0] $$ a[2][0] a[1][0]
#a[1][1] a[1][2]
#a[2][2] a[2][1]
#1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
a=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
#len(a)=4 range(len(a))= 0 1 2 3
for i in range(len(a)):
    pass