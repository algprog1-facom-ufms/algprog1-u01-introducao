"""
PRIMM — Etapa M (Modificar)

Altere o programa abaixo seguindo as instruções da seção
"M — Modificar" do arquivo 03-primm/README.md.

Resumo:
  1. Boas-vindas: "Bem-vindo(a) à Biblioteca do Campus!"
  2. Perguntar também: "Qual é o seu curso? " (depois do nome)
  3. Exibir "Curso: <curso>" logo depois de "Olá, <nome>"
  4. Limite de livros: 5
  5. Manter a última linha "Bom estudo, <nome>!"
"""

# Programa: Biblioteca Digital
print("Bem-vindo(a) à Biblioteca Digital!")
nome = input("Qual é o seu nome? ")
print("Olá,", nome)
print("Hoje você pode emprestar até", "3", "livros.")
print("Bom estudo", nome, sep=", ", end="!\n")
