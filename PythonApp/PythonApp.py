
from random import *
inimesed=["A","B","A","D","E","t"]
palgad=[2000,1200,1000,6000,7000,2234]
def sisesta_andmed(i,p):
    N=4
    for n in range (N):
        inimene=input("nimi:")
        i.append(inimene)
        palk=randint(100,10000)
        p.append(palk)
    return i,p
def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])
def kustutamine(i,p):
    nimi=input("Sisesta nimi,keda vaja kustuda:")
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]== nimi:
                t+=1
                abi_list.append(int(e))
                print(t,"-",i[e],"-",p[e])
        j=int(input("Järjekordne number:"))   
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p
def suurim_palk(i,p):
    suurim=max(p)
    n=p.count(suurim)
    k_list=[]
    if n>1:
        g=0
        for k in range(len(p)):
            if p[k]==suurim:
                g+=1
                k_list.append(int(k))
                print(g,"-",i[k],"-",p[k])
    else:
      for v in range(len(p)):
        if p[v]==suurim:
             print(suurim,"-",i[v])
def vaike_palk(i,p):
    vaike=min(p)
    n=p.count(vaike)
    pe_list=[]
    if n>1:
        a=0
        for y in range(len(p)):
            if p[y]==vaike:
                a+=1
                pe_list.append(int(y))
                print(a,"-",i[y],"-",p[y])
    else:
      for ra in range(len(p)):
        if p[ra]==vaike:
             print(vaike,"-",i[ra])
 
    
 
def vordsed_palgad(i,p):
   N=len(p)
   dublikatid=[x for x in palgad if palgad.count(x)>1]
   dublikatid=list(set(dublikatid))
   print(dublikatid)
   for palk in dublikatid:#2000 n=3
       n=p.count(palk)
       k=-1
       for j in range(n):
           k=p.index(palk,k+1)
           print(k)
           nimi=i[k]
           print(palk,"saab kätte",nimi)
 
def sorteerimine(i,p,v): 
   N=len(p)
   if v== 1:
    for n in range(0,N):
        for m in range(n,N):
            if p[n]<p[m]:
                abi=p[m]
                p[m]=p[n]
                p[n]=abi
                abi=i[n]
                i[n]=i[m]
                i[m]=abi
    andmed_ekranile(i,p)
   else:
    for n in range(0,N):
        for m in range(n,N):
            if p[n]>p[m]:
                abi=p[m]
                p[m]=p[n]
                p[n]=abi
                abi=i[n]
                i[n]=i[m]
                i[m]=abi
    andmed_ekranile(i,p)
 
 
def nimisorteerimine(i,p):
            nimi=input("Sisesta nimi")
            n=i.count(nimi)
            t=0
            if n>1:
                for e in range(len(i)):
                    if i[e]==nimi:
                       t+=1
                       print(t,"-",i[e],"-",p[e])
            else:
                for j in  range(len(i)):
                    if i[j]== nimi:
                      print(i[j],"-",p[j])
 
def salary_higher_or_lower(i,p):
     salary=input()
     for t in range(len(p)):
            if(p[t]!=int(salary)):
                 print(p[t],"-",i[t])
  
def top3(i,p):
   print("lowest pay")
   p.sort()
   for sa in range(3):
    print(p[sa],"-",i[sa])
   print("highest pay")
   p.reverse()
   for sa in range(3):
        print(p[sa],"-",i[sa])
 
def Keskmine(i,p):
   number=0
   keskmine=0
   for na in range(len(p)):
       number+=p[na]
   keskmine=number/len(p) 
   print(keskmine)
   round(keskmine,0)
   print("round number",keskmine)
 
   for ar in range(len(p)):
       if p[ar]==keskmine:
           print(p[ar],"-",i[ar])
       else:
        print ("No such salary")
        break;
def Kustutamine(i,p):
   number=0
   keskmine=0
   for na in range(len(p)):
       number+=p[na]
   keskmine=number/len(p)
   for ta in p:
        if ta< keskmine:
            i.pop(p.index(ta))
            p.pop(p.index(ta))
            print("deleted")
 
   andmed_ekranile(i,p)
           
 
def Tulumaks(i,p):
    salary12=0
    number=0
    for tg in range(len(p)):
        if p[tg]<=1200:
           number=int(p[tg])
           salary12= (number-((number-500)*0.2))
           print(salary12,"-",i[tg])
        elif p[tg]>1200 and p[tg]<2099:
            number=int(p[tg])
            salary12=number-(number-(500-0.55556*(number-1200)))*0.2
            print(salary12,"-",i[tg])
        elif p[tg]>2099:
            number=int(p[tg])
            salary12=number-(number*0.2)
            print(salary12,"-",i[tg])
        else:
            print("wrong")
 
def sort_nimi_järgi(p,i,v):
   N=len(p)
   if v== 1:
    for n in range(0,N):
        for m in range(n,N):
            if p[n]<p[m]:
                abi=p[m]
                p[m]=p[n]
                p[n]=abi
                abi=i[n]
                i[n]=i[m]
                i[m]=abi
    andmed_ekranile(i,p)
   else:
    for n in range(0,N):
        for m in range(n,N):
            if p[n]>p[m]:
                abi=p[m]
                p[m]=p[n]
                p[n]=abi
                abi=i[n]
                i[n]=i[m]
                i[m]=abi
    andmed_ekranile(i,p)
    
 
while 1:
    print("k-kustutamine\na-andmete sisestamine\ne-andmed ekaranile-\nr-kellel on suurim palk\ns-sorteerimine\nv-vordsed_palgad\nt-nimi sorteerimine\nl-sorteerimine\nw-vaikest palk\ny-top3()\nq-keskimine()\nx-kustutamine()\np-tulumaks()\ng-Sort_nimi_jargi() " )
    valik=input()
    if valik.lower()=="a":
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=="e":
        andmed_ekranile(inimesed,palgad)
    elif valik.lower()=="k":
       inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower()=="r":
        inimesed,palgad==suurim_palk(inimesed,palgad)
    elif valik.lower()=="s":
        sorteerimine(inimesed,palgad,int(input("1-kahaneb,2-kasvab")))
    elif valik.lower()=="v":
        vordsed_palgad(inimesed,palgad)
    elif valik.lower()=="t":
        nimisorteerimine(inimesed,palgad)
    elif valik.lower()=="l":
        salary_higher_or_lower(inimesed,palgad)
    elif valik.lower()=="w":
        vaike_palk(inimesed,palgad)
    elif valik.lower()=="y":
         top3(inimesed,palgad)
    elif valik.lower()=="q":
         Keskmine(inimesed,palgad)
    elif valik.lower()=="x":
         Kustutamine(inimesed,palgad)
    elif valik.lower()=="p":
         Tulumaks(inimesed,palgad)
    elif valik.lower()=="g":
         sort_nimi_järgi(inimesed,palgad,int(input("1-Я-A,2-А")))
    
    
    else:
        break