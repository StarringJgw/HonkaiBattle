from random import random
import numpy as np
import matplotlib.pyplot as plt
def CalVariance(p1Rate,p1Mul,p1Vote,p2Vote):
    temp=[]
    i=0
    while i<1000:
        if random()<p1Rate:
            profit=p1Mul*p1Vote
        else:
            profit=1*p2Vote
        temp.append(profit)
        i+=1
    return [np.var(temp),np.mean(temp)]

def simulate(p1Rate,p1Mul,useColor,useLabel,total=200):

    # p1Rate=0.5453
    # p2Rate=0.4547
    # p1Mul=4
    # p2Mul=1
    # total=100
    p1Vote=0
    final=[]
    while p1Vote<total:
        p2Vote=total-p1Vote
        final.append([p1Vote]+CalVariance(p1Rate,p1Mul,p1Vote,total-p1Vote))
        p1Vote+=1

    final.sort(key=lambda x:x[2])
    plt.plot(np.asarray(final)[:,2],np.asarray(final)[:,1],color=useColor,label=useLabel)
    plt.legend(loc='upper right')

plt.figure()

simulate(0.73,1.6,useColor='green',useLabel='R2 Sakura')
simulate(0.27,5,useColor='black',useLabel='R2 Liliya')
simulate(0.5453,1.8,useColor='blue',useLabel='R3 Sakura')
simulate(0.4547,4,useColor='red',useLabel='R3 Bronya')
plt.show()
print()