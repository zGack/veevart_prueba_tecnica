
def knapsack(bag, cap, N, X, values):
  # N -> pivote que se usa para recorrer la lista 
  # X -> Simula ser la mochila, es decir guarda los elementos que se van tomando
  
  # CASO # 1 no hay elementos en la lista, no se toma ninguno
  if N == 0: 
    max_value = 0
  # CASO # 2 el elemento no cabe en la mochila, se prueba con el siguiente
  elif bag[N-1][0] > X: 
    max_value = knapsack(bag, cap, N-1, X, values)
  # CASO # 3 el elemento cabe en lo mochila
  #          por lo que se recurre en 2 casos: tomarlo o no tomarloo
  #          para saber cual de estos 2 subcasos da mas beneficio
  else: 
    max_value = max(knapsack(bag, cap, N-1, X, values),                              # NO SE TOMA, se prueba con el siguiente
                   (knapsack(bag, cap, N-1, X - bag[N-1][0], values) + bag[N-1][1])) # SE TOMA, se suma el beneficio y se prueba con el siguiente

  print(max_value,bag[N-1])

  return max_value

def solve(bag, cap):
  values = dict()
  ans = knapsack(bag, cap, len(bag), cap, values)

  return ans 

def main():
  # (peso, beneficio)
  # (w, v)
  bag = [(2, 3), (3, 4), (4, 5), (5, 6)]
  cap = 8

  values = []

  # bag = [(3,4), (5,6), (5,5), (2,1)]
  # cap = 15

  print(solve(bag, cap))
  
main()