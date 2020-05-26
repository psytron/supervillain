


import os

first_names = ['john','ron','burt','bob','garry', 'moe','tom','frank','chris','will','johnny','nick']
last_names = ['smith','johnson','thompson','williamson','mcdonald','brown','ericson']
#first_names = ['apple','moon','star','summer','rain','lilly','rosemarry','basil']
#first_names = ['ap','bo','ja','al','za']
#last_names = ['dex','jax','dax','vue']

all_names = []
for f in first_names:
    for l in last_names:
        all_names.append(f+' '+l)
        print(f+' '+l)
        

import random
iter = 0
while True and iter < 100:
    curname = all_names[ int(random.random()* len( all_names)-1 ) ]
    os.system('say '+ curname  )
    iter += 1
    print( iter, curname )