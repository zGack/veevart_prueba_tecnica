
def search_word(row, col, word, matrix, dir):
  sol = [] # LISTA DONDE SE ALMACENAN LOS PASOS DE LAS SOLUCIONES

  # SE AGREGA EL PRIMER PASO
  sol.append(f"{word[0]} - [{row}, {col}]")

  w_idx = 1 # INDICE QUE INDICA SI SE HA 

  row += dir[0]
  col += dir[1]

  # COND 1: SE VERIFICA QUE NO SE HAYA ENCONTRADO LA PALABRA
  # COND 2, 3: SE VERIFICA QUE COL ESTE DENTRO DE LAS DIMENSIONES DE LA MATRIX
  # COND 4, 5: SE VERIFICA QUE ROW ESTE DENTRO DE LAS DIMENSIONES DE LA MATRIX
  # COND 6: SE VERIFICA QUE LA SIGUIENTE LETRA HAGA PARTE DE LA PALABRA OBJETIVO
  while w_idx < len(word) and \
        row >= 0 and \
        col >= 0 and \
        row < len(matrix) and \
        col < len(matrix[row]) and \
        matrix[row][col] == word[w_idx]:

    # SE AGREGAN LOS PASOS
    sol.append(f"{word[w_idx]} - [{row}, {col}]")

    # SE MODIFICA LA DIRECCION DE BUSQUEDA
    row += dir[0]
    col += dir[1]

    # SE AUMENTA EL INDICE DE LA LETRA DE LA PALABRA OBJ
    w_idx += 1

  # SE IMPRIMEN LOS PASOS DE LA SOLUCION
  if w_idx == len(word):
    for sol_step in sol: print(sol_step)

  return w_idx == len(word)

def solve(matrix, word):

  row, found = 0, False

  # SE ITERA SOBRE TODA LA MATRIX
  while row < len(matrix):
    col = 0
    while col < len(matrix[row]):
      # SE VERIFICA SI LA PRIMERA LETRA COINCIDE CON LA PRIMERA LETRA DE LA PALABRA OBJETIVO
      if matrix[row][col] == word[0]:
        
        # SE BUSCA LAS PALABRAS EN TODAS LAS DIRECCIONES (IZQ-DER), (ARR-ABJ), (DER-ARR), (DER-ABJ), (IZQ-ABJ), (IZQ,ARRIBA)
        for dir in [[0,1],[1,0],[-1,1],[1,1],[1,-1],[-1,-1]]:
          found = search_word(row, col, word, matrix, dir) or found

      col += 1
    row += 1

  return found

def main():
  matrix = ["S O L", "U N O", "N U T"]

  words = ["SUN", "SOL", "LOT","ONU", "RAY"]

  # SE DIVIDEN LAS FILAS POR ESPACIOS
  for idx in range(len(matrix)):
    matrix[idx] = matrix[idx].split(" ")

  # SE EJECUTA LA SOLUCION POR CADA PALABRA A BUSCAR
  for w in words: 
    print(f'Searching "{w}"')
    if not solve(matrix, w): print(f'"{w}" Not found')

main()