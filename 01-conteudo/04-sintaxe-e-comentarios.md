# 4. Sintaxe básica do Python e comentários

## Sintaxe

**Sintaxe** é o conjunto de regras de escrita de uma linguagem — como a gramática
do português. Se a sintaxe estiver errada, o programa nem começa a executar.

Regras que já valem desde o primeiro programa:

| Regra | Correto | Errado |
|---|---|---|
| Uma instrução por linha | `print("Oi")` | `print("Oi") print("Tchau")` |
| Diferencia maiúsculas e minúsculas | `print` | `Print`, `PRINT` |
| Textos entre aspas (simples ou duplas) | `"Oi"` ou `'Oi'` | `Oi` (sem aspas) |
| Aspas que abrem precisam fechar igual | `"Oi"` | `"Oi'` |
| Parênteses que abrem precisam fechar | `print("Oi")` | `print("Oi"` |
| Linhas começam na coluna 1 (sem espaços à esquerda) | `print("Oi")` | `␣␣print("Oi")` → `IndentationError` |

> **Indentação** (espaços no início da linha) tem significado no Python e será usada
> mais adiante, em estruturas de decisão e repetição. Por enquanto, **não comece
> linhas com espaços**.

## Textos (strings)

Tudo o que está entre aspas é um **texto** (em programação, chamado de *string*).
O Python mostra o texto exatamente como está — incluindo espaços e acentos.

```python
print("Olá,   mundo!")   # os três espaços aparecem na tela
```

## Comentários

**Comentários** são anotações para pessoas. O interpretador os **ignora**.

Em Python, um comentário começa com `#` e vai até o fim da linha:

```python
# Este programa exibe uma saudação.
print("Olá!")   # comentário no fim da linha também vale
```

### Para que servem?

- Explicar **o objetivo** do programa (cabeçalho).
- Explicar **por que** algo foi feito de certo jeito.
- Dividir o programa em **partes** (entrada, processamento, saída).
- Desativar temporariamente uma linha durante testes.

### Cabeçalho recomendado para seus programas

```python
# Disciplina: Algoritmos e Programação I
# Autor(a): Seu Nome
# Objetivo: Exibir uma mensagem de boas-vindas.
```

### Bons e maus comentários

| ❌ Mau (repete o óbvio) | ✅ Bom (explica a intenção) |
|---|---|
| `# imprime Olá` | `# Saudação inicial exibida ao abrir o programa` |

## Docstrings

Você verá textos entre **três aspas** no início dos arquivos de atividade:

```python
"""
Atividade 01 — Olá, mundo!
"""
```

Isso é uma *docstring*: um texto de documentação. Ele também não altera o que o
programa mostra na tela.

## Para verificar

1. O que acontece se você escrever `Print("Oi")`?
2. O que o interpretador faz com uma linha que começa com `#`?
3. Escreva um cabeçalho de comentários para um programa seu.
