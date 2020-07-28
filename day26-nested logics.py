# Enter your code here. Read input from STDIN. Print output to STDOUT
# a,b,c = map(int,input().split())
# d,e,f = map(int,input().split())
# m = 0
# t =0
# if c!=f:
#     print(10000)

# elif b>=e:
#     m = (b-e)*500
#     if a>d:
#         t = (a-d)*15
#     a = m+t
#     print(a)
rd, rm, ry = [int(x) for x in input().split(' ')]
ed, em, ey = [int(x) for x in input().split(' ')]

if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)
