# 03 — PRIMM: Biblioteca Digital

**PRIMM** é uma forma de aprender programação **lendo antes de escrever**. São cinco
etapas, sempre nesta ordem:

| Etapa | Em inglês | O que você faz | Arquivo |
|:-:|---|---|---|
| **P** | *Predict* | **Prever** a saída, só lendo o código | `respostas.md` |
| **R** | *Run* | **Executar** e comparar com sua previsão | `respostas.md` |
| **I** | *Investigate* | **Investigar** como cada linha funciona | `respostas.md` |
| **M** | *Modify* | **Modificar** o programa para fazer algo novo | `p4_modificar.py` ✅ |
| **M** | *Make* | **Criar** um programa novo, do zero | `p5_criar.py` ✅ |

✅ = corrigido automaticamente. As etapas P, R e I são registradas em `respostas.md`
e comentadas pelo professor no Pull Request de Feedback.

> 🧠 Não pule a previsão! Errar a previsão e descobrir **por quê** é exatamente o que
> faz você aprender.

---

## O programa

Arquivo: [`p1_programa.py`](p1_programa.py) — **não altere este arquivo.**

```python
# Programa: Biblioteca Digital
print("Bem-vindo(a) à Biblioteca Digital!")
nome = input("Qual é o seu nome? ")
print("Olá,", nome)
print("Hoje você pode emprestar até", "3", "livros.")
print("Bom estudo", nome, sep=", ", end="!\n")
```

---

## P — Prever (sem executar!)

Leia o programa e responda em `respostas.md`:

1. Quantas linhas de texto aparecerão na tela (contando a pergunta)?
2. Suponha que o usuário digite **Marina**. Escreva **exatamente** a saída completa.
3. Na linha `print("Bom estudo", nome, sep=", ", end="!\n")`, o que você acha que
   `sep` e `end` fazem?

## R — Executar

```bash
python 03-primm/p1_programa.py
```

Digite **Marina** quando o programa perguntar.

4. Sua previsão estava correta? Marque o que acertou e o que errou.
5. Se errou alguma coisa, qual foi a surpresa?

## I — Investigar

Responda observando o código e fazendo **experimentos em uma cópia** (você pode
criar um arquivo `rascunho.py` à vontade):

6. Qual linha é responsável por esperar o usuário digitar? Como você sabe?
7. Por que `nome` aparece **sem aspas** nos `print`? O que aconteceria com aspas?
8. Na linha `print("Hoje você pode emprestar até", "3", "livros.")`, quantos
   valores o `print` recebe? De onde vêm os espaços da saída?
9. Remova o `end="!\n"` (no rascunho) e execute. O que mudou?
10. Troque a ordem das linhas 3 e 4 (no rascunho), deixando o `print("Olá,", nome)`
    **antes** do `input`. Execute. Qual erro aparece? Por que isso acontece?

## M — Modificar → `p4_modificar.py`

O arquivo `p4_modificar.py` já contém uma cópia do programa. Altere-o para que:

1. A mensagem de boas-vindas seja **`Bem-vindo(a) à Biblioteca do Campus!`**
2. O programa pergunte também o curso, com o texto **`Qual é o seu curso? `**
   (logo depois de perguntar o nome).
3. Depois da linha `Olá, ...`, exiba **`Curso: <curso digitado>`**.
4. O limite de livros passe a ser **5**.
5. A última linha continue sendo `Bom estudo, <nome>!`.

Exemplo de execução (entradas em **negrito**):

<pre>
Bem-vindo(a) à Biblioteca do Campus!
Qual é o seu nome? <b>Marina</b>
Qual é o seu curso? <b>Engenharia</b>
Olá, Marina
Curso: Engenharia
Hoje você pode emprestar até 5 livros.
Bom estudo, Marina!
</pre>

## M — Criar → `p5_criar.py`

Agora, do zero, crie o programa da **Lanchonete do Campus**. Ele deve:

1. Exibir **`=== Lanchonete do Campus ===`**
2. Perguntar **`Nome do cliente: `**
3. Perguntar **`Lanche escolhido: `**
4. Perguntar **`Bebida escolhida: `**
5. Exibir **`Pedido de <nome>: <lanche> + <bebida>`**
6. Exibir **`Seu pedido está sendo preparado!`**

<pre>
=== Lanchonete do Campus ===
Nome do cliente: <b>Caio</b>
Lanche escolhido: <b>pastel</b>
Bebida escolhida: <b>suco</b>
Pedido de Caio: pastel + suco
Seu pedido está sendo preparado!
</pre>

> 💡 Dica para o item 5: use vírgulas e o parâmetro `sep`, ou vários valores no
> mesmo `print`. Pense em quais espaços e sinais (`:` e `+`) precisam aparecer.
