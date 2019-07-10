from random import random
class Charcter:
    def __init__(self,targetName,targetLife=0,targetDamage=0,targetDefence=0,targetSpecial=0):
        self.name=targetName
        self.life=targetLife
        self.damage=targetDamage
        self.defence=targetDefence
        self.special=targetSpecial
    def baseAttack(self,target):
        target.hurt(self.damage,self)
    def baseHurt(self,data):
        finalHurt=int(min(data-self.defence,0))
        # print(self.name," -",data-self.defence)
        self.life-=data-self.defence
        if self.life<=0:
            raise Exception(self)
class Bronya(Charcter):

    def hurt(self,data,source):
        if random()<0.15:
            # print("Bronya Dodged")
            pass
        else:
            self.baseHurt(data)

    def attack(self,target):
        if self.special==2:
            temp=int(random()*100)
            # print("Bronya Ultimate: ",temp)
            target.hurt(temp,self)
            self.special=0
        else:
            self.baseAttack(target)
            self.special+=1

class Liliya(Charcter):
    def attack(self, target):
        if self.special>=7:
            # print("Liliya Ultimate")
            raise Exception(target)
        else:
            self.special+=1
            self.baseAttack(target)

    def hurt(self,data,source):
        if random()<0.15:
            # print("Liliya Counter: ",data)
            source.hurt(data+source.defence,self)
        else:
            self.baseHurt(data)

def match():
    p2=Bronya("Bronya",100,26,8)
    p1=Liliya("Liliya",100,20,11)
    try:
        i=1
        while True:
            # print("Round ",i)
            # print("P1:",p1.name,p1.life)
            # print("P2:",p2.name,p2.life)
            p1.attack(p2)
            p2.attack(p1)
            i+=1

    except Exception as e:
        # print(e.args[0].name+" Failed")
        return e.args[0].name

matchNum=10000
BronyaWin=0
LiliyaWin=0
while matchNum>0:
    fail=match()
    if fail=="Bronya":
        LiliyaWin+=1
    else:
        BronyaWin+=1
    matchNum-=1
print("Bronya Final:",BronyaWin)
print("LiliyaWinnal:",LiliyaWin)

