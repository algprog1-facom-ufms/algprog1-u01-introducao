# 6. Entrada de dados: `input`

Até aqui, os programas sempre mostram a mesma coisa. Com `input`, o programa
**conversa** com o usuário: ele faz uma pergunta, espera a pessoa digitar e
pressionar **Enter**.

```python
nome = input("Qual é o seu nome? ")
print("Olá,", nome)
```

Execução (o que o usuário digita está em **negrito**):

<pre>
Qual é o seu nome? <b>Ana</b>
Olá, Ana
</pre>

## Entendendo a linha `nome = input("...")`

1. `input("Qual é o seu nome? ")` mostra a pergunta (o **prompt**) e espera.
2. O usuário digita `Ana` e pressiona Enter.
3. O texto digitado é **guardado** com o nome `nome`, graças ao `=`.
4. Depois, podemos **usar** `nome` em um `print` — **sem aspas**.

> ⚠️ `print("nome")` exibe a palavra **nome**. `print(nome)` exibe **o que foi
> digitado**. As aspas fazem toda a diferença.

> ℹ️ Esse "nome para guardar um valor" se chama **variável**. Estudaremos variáveis
> em detalhes na próxima unidade. Por enquanto, basta saber guardar e usar o que foi
> digitado.

## Boas práticas para o prompt

- Termine a pergunta com **espaço** (`"Nome: "`), para o cursor não ficar colado.
- Seja claro sobre o que o usuário deve digitar.

| ❌ | ✅ |
|---|---|
| `input()` (o usuário não sabe o que digitar) | `input("Digite sua cidade: ")` |

## Vários dados

Cada `input` lê **uma** resposta. Para várias perguntas, use vários `input`, em
sequência:

```python
nome = input("Nome: ")
cidade = input("Cidade: ")
print(nome, "mora em", cidade)
```

<pre>
Nome: <b>Bruno</b>
Cidade: <b>Dourados</b>
Bruno mora em Dourados
</pre>

## O padrão Entrada → Saída

Quase todo programa desta unidade segue este modelo:

```python
# Entrada
dado = input("Pergunta: ")

# Saída
print("Mensagem usando", dado)
```

## Para verificar

1. Qual é a diferença entre `print("cidade")` e `print(cidade)`?
2. Por que é bom terminar o texto do `input` com um espaço?
3. Escreva um programa que pergunte sua comida favorita e responda
   `Eu também gosto de <comida>`.
