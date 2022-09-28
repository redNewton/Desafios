salario = int(input()) 
if salario <= 600.00:
  s = salario * 1.17
  r = s - salario
  p = 17
elif salario >= 600.01 and salario <= 900.00:
  s = salario * 1.13
  r = s - salario
  p = 13
elif salario >= 900.01 and salario <= 1500.00:
  s = salario * 1.12
  r = s - salario
  p = 12
elif salario >= 1500.01 and salario <= 2000.00:
  s = salario * 1.10
  r = s - salario
  p = 10
elif salario > 2000.01:
  s = salario * 1.05
  r = s - salario
  p = 5

salString = str(s)
novoSal = salString.split('.')
reString = str(r)
novoRe = reString.split('.')
print(f"Novo salario: {novoSal[0]},00 Reajuste ganho: {novoRe[0]},00 Em percentual: {p} %")
