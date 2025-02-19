#l_max = int(input("Entra el rango de la lista:  "))
for l_max in range(100, 1001, 100):
  l = list(range(0, l_max+1))
  
  pos = 0
  count = 0
  op = 2
  
  while (pos < len(l)):
    div = 1
    total_divisors = 0
    
    op += 3
    while (div <= l[pos]):
      
      
      if (l[pos] % div == 0):
        total_divisors += 1
        op += 1
      
      div += 1
      op += 3
    if (total_divisors == 2):
      count += 1
      op += 1
  
    pos += 1
    op += 2
    
    
  op += 1
  print(l_max,   op,   op/l_max,   op/(l_max*l_max))
  

