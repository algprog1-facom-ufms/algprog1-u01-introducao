# 2. Linguagens de programação e execução de programas

## Por que precisamos de uma linguagem?

O processador só entende **linguagem de máquina** — sequências de zeros e uns.
Escrever assim é praticamente impossível para pessoas. As **linguagens de
programação** são uma ponte: têm palavras e regras próximas da linguagem humana e
podem ser traduzidas para a linguagem da máquina.

| Nível | Exemplo | Quem lê com facilidade |
|---|---|---|
| Alto nível | `print("Olá")` (Python) | Pessoas |
| Baixo nível | `MOV AX, 1` (Assembly) | Especialistas |
| Máquina | `10110000 00000001` | Apenas o processador |

## Compilação e interpretação

Há duas formas principais de traduzir um programa:

- **Compilação** — um *compilador* traduz o programa inteiro antes, gerando um
  arquivo executável. Ex.: C, C++.
- **Interpretação** — um *interpretador* lê e executa o programa instrução por
  instrução. Ex.: **Python**.

## Como um programa Python é executado

```
 ola.py  ──►  interpretador Python  ──►  resultado no terminal
 (texto)        (python ola.py)           Olá, mundo!
```

1. Você escreve o código em um arquivo de texto com extensão **`.py`** (no VS Code).
2. No terminal, você pede ao interpretador para executá-lo:
   ```bash
   python ola.py
   ```
3. O interpretador lê o arquivo **de cima para baixo** e executa cada instrução.
4. O resultado aparece no **terminal**.

## Erros

Se o interpretador encontrar algo que não segue as regras da linguagem, ele para e
mostra uma mensagem de erro, indicando a **linha** do problema:

```
  File "ola.py", line 1
    print("Olá, mundo!"
         ^
SyntaxError: '(' was never closed
```

> Erros são normais e fazem parte da programação. Leia a mensagem: ela diz **onde**
> e, quase sempre, **o quê**.

## Para verificar

1. Por que não programamos diretamente em linguagem de máquina?
2. Python é compilado ou interpretado? O que isso significa?
3. Qual comando executa o arquivo `teste.py` no terminal?
