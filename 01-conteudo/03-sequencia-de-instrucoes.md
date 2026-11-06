# 3. Organização sequencial de instruções

## A estrutura sequencial

A forma mais simples de organizar um programa é a **sequência**: as instruções são
executadas **uma após a outra**, na ordem em que aparecem, **de cima para baixo**.

```python
print("Primeiro")
print("Segundo")
print("Terceiro")
```

Saída:

```
Primeiro
Segundo
Terceiro
```

## A ordem muda o resultado

Compare os dois programas:

| Programa A | Programa B |
|---|---|
| `print("Abra a porta.")`<br>`print("Entre na sala.")` | `print("Entre na sala.")`<br>`print("Abra a porta.")` |

Os dois têm as mesmas instruções, mas o **B** descreve algo impossível. O
computador executa o B sem reclamar — **a responsabilidade pela lógica é de quem
programa**.

## Rastreando um programa

**Rastrear** (ou fazer o "teste de mesa") é simular a execução linha a linha,
anotando o que acontece. É a principal habilidade da etapa *Predict* do PRIMM.

```python
print("A")      # linha 1
print("B")      # linha 2
print("A")      # linha 3
```

| Linha executada | O que aparece na tela |
|:-:|---|
| 1 | `A` |
| 2 | `B` |
| 3 | `A` |

## Para verificar

1. O que significa dizer que um programa é "sequencial"?
2. Se trocarmos a ordem de duas linhas `print`, o programa dá erro? O que muda?
3. Faça o rastreamento de um programa com quatro `print` à sua escolha.
