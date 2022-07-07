flag = [-111, -47, -47, -79, -39, -39, 49, -79, 97, -127, -79, 49, -55, 9, 27, 89, -19, 59, 97, 49, -19, 89, -37, 121, -37, 89, -69, -37, -19, -111, 89, -37, -19, 113, -71, 97, -19, -101, 49, 49, 11, 91, -69, 11, -79, -87]
a=[0 for i in range(46)]
b=[0 for i in range(46)]
c=[0 for i in range(46)]
def one():
    for i in range(0,len(flag),1):
        flag[i] = 23 ^ flag[i]
        if (flag[i] < 0):
            flag[i] = 256 + flag[i]
        a[i] = flag[i]

one()

def to_bin():
    for i in range (0,len(a),1):
        b[i]='{0:08b}'.format(a[i])
    
to_bin()


for i in range (0,len(b),1):
    c[i]=b[i][::-1]
    print(c[i])
