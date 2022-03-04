CFd = "entre.txt"
CRd = "sortie.txt"

def syracuse(entier, fw):
    with open(fw,'w') as f:
        while entier != 1:
            f.write(str(entier))
            f.write(str("\n"))
            if entier % 2 == 0:
                entier = entier/2
            else:
                entier = entier*3+1
   


with open(CFd, 'r') as f:
        entier = f.readlines()
        
        entier = ''.join(entier)
        entier = int(entier)
         
        


syracuse(entier,CRd)