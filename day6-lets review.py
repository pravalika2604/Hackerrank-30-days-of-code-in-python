# Enter your code here. Read input from STDIN. Print output to STDOUT
n  = int(input())

for i in range(0,n):
    a1 = ''
    a2 = ''
    m = str(input())
    # print(len(m))
    count = -1
    for ele in m:
        count+=1
        if count%2 == 0:
            a1=a1+ele
        if count%2 != 0:
            a2 = a2+ele
    
    print(a1+" "+a2)
    

