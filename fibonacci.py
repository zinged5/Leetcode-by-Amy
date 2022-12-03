from urllib3.connectionpool import xrange

a,b=0,1

def fibonacci(n):
    if n in [1,2]:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


a,b=0,1

for i in xrange(0,10):
    a,b=b,a+b
    print(b)
# 2,3
#
# 0,1,1,2,3,5,8,13
# a=0,b=0+1
# a=1,b=1+1