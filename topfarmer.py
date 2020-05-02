


import os

first_names = ['john','ron','burt','bob','garry', 'moe','tom','frank','chris','will','johnny','nick']
last_names = ['smith','johnson','thompson','williamson','mcdonald','brown','ericson']
#first_names = ['apple','moon','star','summer','rain','lilly','rosemarry','basil']
first_names = ['ap','bo','ja','al','za']
last_names = ['dex','jax','dax','vue']

all_names = []
for f in first_names:
    for l in last_names:
        print(f+''+l)
        

import random
while False:
    os.system('say '+ all_names[ int(random.random()*79) ]  )