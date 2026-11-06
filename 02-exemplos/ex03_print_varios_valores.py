# Exemplo 03 — Explorando o print
# Objetivo: exibir vários valores, linhas em branco e usar sep/end.

# Valores separados por vírgula: o print coloca um espaço entre eles.
print("Python", "é", "uma", "linguagem")

# print() vazio exibe uma linha em branco.
print()

# sep define o que vai ENTRE os valores.
print("06", "11", "2026", sep="/")
print("algprog1", "u01", "introducao", sep="-")

# end define o que vai no FINAL (o padrão é pular linha).
print("Carregando", end="")
print("...", end="")
print(" pronto!")
