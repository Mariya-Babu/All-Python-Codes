from logic import *
p,q,r,s,t,u,v=vars('p','q','r','s','t','u','v')
print(p|q)
print(p&q)
print(p>>q)
print(p<<q)
print(p.iff(q))
print(~p)
f1=((p|q)&~p)>>q
print(f1)
f1.print_truth_table()
print(f1.is_tautology())
f2=(p&q)>>r
print(f2)
f2.print_truth_table()
print(f2.is_contingency())
f3=p>>(q>>r)
f3.print_truth_table()
print(f2==f3)
(p&~p).print_truth_table()
print((p&~p).is_contradiction())
f4=(p>>q)|(~p>>r)
f4.print_truth_table()
if(f4.is_tautology()==True):
    print("It is Tautology")
elif(f4.is_contradiction()==True):
    print("It is Contradiction")
else:
    print("It is Contingency")
f5=~((p>>q)>>((r|p)>>(r|q)))
f5.print_truth_table()
if(f5.is_tautology()==True):
    print("It is Tautology")
elif(f5.is_contradiction()==True):
    print("It is Contradiction")
else:
    print("It is Contingency")

f6=((p|q)&~r)>>~p|r
print(type(f6))
f6.print_truth_table()
if(f6.is_tautology()==True):
    print("It is Tautology")
elif(f6.is_contradiction()==True):
    print("It is Contradiction")
else:
    print("It is Contingency")
    

f7=(~(p|q|~r))&((r>>p)|(r>>q))
f7.print_truth_table()
if(f7.is_tautology()==True):
    print("It is Tautology")
elif(f7.is_contradiction()==True):
    print("It is Contradiction")
else:
    print("It is Contingency")


f8=((p&(p>>~q))|(q>>~q))>>~q
f8.print_truth_table()
if(f8.is_tautology()==True):
    print("It is a Tautology")
elif(f8.is_contradiction()==True):
    print("It is Contradiction")
else:
    print("It is Contingency")

f9=~((p&q)>>r|(s&t>>u))
f9.print_truth_table()
if(f9.is_tautology()==True):
    print("It is a Tautology")
elif(f9.is_contradiction()==True):
    print("It is Contradiction")
else:
    print("It is Contingency")


