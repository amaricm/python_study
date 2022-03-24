evenlist = []
oddlist =[]
def Even_odd(l):
    for a in l:
      if a % 2 == 0:
        evenlist.append(a)
      else: 
       oddlist.append(a) 
general_l =  evenlist + oddlist
print(general_l)
