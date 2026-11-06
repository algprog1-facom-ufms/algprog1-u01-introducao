# 5. Saída de dados: `print`

`print` é uma **função**: um comando com nome, seguido de parênteses, que realiza
uma tarefa. A tarefa de `print` é **exibir algo no terminal**.

```python
print("Olá, mundo!")
```

```
Olá, mundo!
```

## Cada `print` termina com uma quebra de linha

```python
print("Linha 1")
print("Linha 2")
```

```
Linha 1
Linha 2
```

Um `print()` vazio exibe uma **linha em branco**:

```python
print("Antes")
print()
print("Depois")
```

```
Antes

Depois
```

## Vários valores em um mesmo `print`

Separe os valores por **vírgula**. O `print` coloca **um espaço** entre eles:

```python
print("Python", "é", "legal")
```

```
Python é legal
```

## Personalizando: `sep` e `end`

| Parâmetro | Controla | Valor padrão |
|---|---|---|
| `sep` | O que vai **entre** os valores | `" "` (um espaço) |
| `end` | O que vai **no final** | `"\n"` (quebra de linha) |

```python
print("10", "11", "2026", sep="/")
print("Carregando", end="...")
print("pronto!")
```

```
10/11/2026
Carregando...pronto!
```

## Caracteres especiais

| Escrita | Efeito |
|---|---|
| `\n` | Quebra de linha dentro do texto |
| `\t` | Tabulação |
| `\"` | Aspas duplas dentro de texto com aspas duplas |

```python
print("Nome:\tAna\nCurso:\tSI")
print("Ela disse: \"Oi!\"")
```

```
Nome:	Ana
Curso:	SI
Ela disse: "Oi!"
```

## Para verificar

1. Quantas linhas o programa abaixo exibe? Quais?
   ```python
   print("A", "B")
   print()
   print("C", end="")
   print("D")
   ```
2. Como exibir `2026-11-06` usando três valores separados e `sep`?
