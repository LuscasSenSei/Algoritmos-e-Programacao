#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759
ano = int(input(""))

salarioBase = 1000
percentual = 0.015

if 2006 > ano:
    
    print("O ano informado deverá ser > 2005!")
    
else:
    
    salarioFinal = salarioBase + (percentual * salarioBase)
    
    while ano >= 2007:
         ano = ano - 1
         percentual = percentual + 0.01
         salarioFinal = salarioFinal + (percentual * salarioFinal)
    print("Salário atual: R$%.2f"%salarioFinal)   
