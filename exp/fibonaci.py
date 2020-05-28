
import time,sys

iter=0
x,y,z=1,1,0
while True:
    z = x + y
    x = y
    y = z
    print( iter,' : ',z )
    #time.sleep(0.01 )
    iter+=1
    if iter > 100000: sys.exit()



    
