
import time,sys

iter=0
x,y,z=1,1,0
starttime = time.time()
finalnum = 0 
while True:
    z = x + y
    x = y
    y = z
    finalnum = z
    #print( iter,' : ',z )
    #time.sleep(0.01 )
    iter+=1
    if iter > 1000000: 
        print( finalnum )
        print( time.time()- starttime)
        sys.exit()



    
