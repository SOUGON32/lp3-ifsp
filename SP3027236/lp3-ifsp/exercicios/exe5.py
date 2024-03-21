def eh_valido(texto):
  for caracter in texto:
    if not caracter.isalpha():
      return False

  return True

texto = input("Digite um texto: ")

if eh_valido(texto):
  print(f"O texto '{texto}' é válido.")
else:
  print(f"O texto '{texto}' é inválido.")
