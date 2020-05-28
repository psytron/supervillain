
import time,sys

iter=0
x,y,z=1,1,0
starttime = time.time()
while True:
    z = x + y
    x = y
    y = z
    print( iter,' : ',z )
    #time.sleep(0.01 )
    iter+=1
    if iter > 50000: 
        print( time.time()- starttime)
        sys.exit()



    
