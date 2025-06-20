
# Autor : Pietro Marchetti

r0 = Relogio(12, 65, 54)  # Inválido
r1 = Relogio(17, 30, 28)
r2 = Relogio(20, 0, 30)

print(r1)          
print(r2)          

r3 = r1 + r2
print(r3)          

r4 = r3 - r2       
print(r4)          

r5 = r2 - r3       
print(r5)          

print(r1 == r2)    
r6 = Relogio(18, 37, 32)
print(r1 == r6)    

print(r1 > r3)    
print(r2 < r3)     
print(r2 > r3)     
print(r2 < r3)     
