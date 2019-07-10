from random import random

class Charcter:
    def __init__(self,targetName,targetLife=0,targetDamage=0,targetDefence=0,targetSpecial=0):
        self.name=targetName
        self.life=targetLife
        self.damage=targetDamage
        self.defence=targetDefence
        self.special=targetSpecial
    def baseAttack(self,target,type=0):
        target.hurt(self.damage,self,type)
    def baseHurt(self,data,type=0):
        finalHurt=0
        if type==0:
            finalHurt=int(max(data-self.defence,0))
        elif type==1:
            finalHurt=int(max(data,0))
        elif type==2:
            finalHurt=2*int(max(data-self.defence,0))

        print(self.name," -",finalHurt)
        self.life-=finalHurt
        if self.life<=0:
            raise Exception(self)
    def hurt(self,data,source,type=0):
        self.baseHurt(data,type)

class Bronya(Charcter):

    def hurt(self,data,source,type=0):
        if random()<0.15:
            print("Bronya Dodged")
            pass
        else:
            self.baseHurt(data,type)

    def attack(self,target):
        if self.special==2:
            temp=int(random()*100)
            print("Bronya Ultimate: ",temp)
            target.hurt(temp,self)
            self.special=0
        else:
            self.baseAttack(target)
            self.special+=1

class Liliya(Charcter):
    def attack(self, target):
        if self.special>=7:
            print("Liliya Ultimate")
            raise Exception(target)
        else:
            self.special+=1
            self.baseAttack(target)

    def hurt(self,data,source,type=0):
        if random()<0.15 :
            print("Liliya Counter: ",data)
            source.hurt(data+source.defence,self,type)
        else:
            self.baseHurt(data,type)

class Sakura(Charcter):

    def attack(self,target):
        if random()<0.2:
            print("Sakura Flame Triggered")
            self.special=3
        if self.special>0:
            target.hurt(5,self,1)
            self.special-=1
        if random()<0.25:
            print("Sakura Crit")
            target.hurt(self.damage,self,2)
        else:
            target.hurt(self.damage,self,0)

def match():
    # p2=Bronya("Bronya",100,26,8)
    p2=Sakura("Sakura",100,28,7)
    p1=Liliya("Liliya",100,20,11)
    try:
        i=1
        while True:
            print("Round ",i)
            print("P1:",p1.name,p1.life)
            print("P2:",p2.name,p2.life)
            p1.attack(p2)
            p2.attack(p1)
            i+=1

    except Exception as e:
        # print(e.args[0].name+" Failed")
        if e.args[0]==p1:
            return p2.name
        else:
            return p1.name

matchNum=10000
score={}
while matchNum>0:
    winner=match()
    score[winner]=score.get(winner,0)+1
    matchNum-=1
for x in score:
    print(x,score[x])
