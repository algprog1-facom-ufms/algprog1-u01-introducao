# Unidade 01 — Introdução à Programação

**Algoritmos e Programação I** · Python · GitHub · VS Code · Classroom 50

Bem-vindo(a) à primeira unidade da disciplina! Aqui você vai entender o que é um
algoritmo, como um programa é executado pelo computador e vai escrever seus
primeiros programas em Python, usando os comandos `print` e `input`.

---

## 🎯 Objetivos de aprendizagem

Ao final desta unidade, você será capaz de:

1. Diferenciar **algoritmo** e **programa**.
2. Explicar o papel de uma **linguagem de programação** e como um programa Python é **executado**.
3. Organizar instruções em uma **sequência** lógica.
4. Reconhecer a **sintaxe básica** do Python (linhas, indentação, aspas, parênteses).
5. Escrever **comentários** que documentam o código.
6. Exibir mensagens na tela com **`print`**.
7. Ler dados digitados pelo usuário com **`input`**.
8. Construir **pequenos programas** completos combinando saída e entrada.

> ℹ️ Variáveis, tipos de dados e operadores serão estudados com profundidade nas
> próximas unidades. Aqui usamos apenas o mínimo necessário para guardar o que o
> usuário digitou.

---

## 🗺️ Roteiro de estudo (siga nesta ordem)

| Passo | Pasta | O que fazer | Tempo estimado |
|:---:|---|---|:---:|
| 1 | [`01-conteudo/`](01-conteudo/) | Ler o material explicativo (6 tópicos) | 1h30 |
| 2 | [`02-exemplos/`](02-exemplos/) | Executar e ler os exemplos comentados | 40 min |
| 3 | [`03-primm/`](03-primm/) | Fazer a sequência PRIMM (Prever → Executar → Investigar → Modificar → Criar) | 1h |
| 4 | [`04-atividades/`](04-atividades/) | Resolver as 6 atividades de fixação | 1h30 |
| 5 | [`05-desafios/`](05-desafios/) | Resolver os 3 desafios autônomos | 1h |
| 6 | [`06-autoavaliacao/`](06-autoavaliacao/) | Responder o questionário e a reflexão | 30 min |

---

## 🛠️ Como trabalhar neste repositório

### 1. Abra no VS Code

```bash
git clone <endereço-do-seu-repositório>
cd <nome-do-seu-repositório>
code .
```

> Ao abrir, o VS Code vai sugerir a extensão **Python** (Microsoft). Instale-a.

### 2. Execute um programa

No terminal do VS Code (menu **Terminal → New Terminal**), a partir da pasta raiz:

```bash
python 02-exemplos/ex01_ola_mundo.py
```

> No Linux/macOS pode ser necessário usar `python3` no lugar de `python`.

### 3. Resolva as atividades

Cada arquivo em `03-primm/`, `04-atividades/` e `05-desafios/` contém o enunciado
no topo e um espaço marcado com `# TODO` onde você deve escrever seu código.

⚠️ **Não renomeie nem mova os arquivos** — a correção automática procura por eles
exatamente nesses caminhos.

### 4. Envie (commit + push)

```bash
git add .
git commit -m "Resolve atividade 01"
git push
```

Você pode (e deve!) enviar várias vezes. **Cada `push` dispara a correção automática.**

---

## ✅ Correção automática e feedback

- A cada `push`, o Classroom 50 executa seus programas e verifica se eles exibem as
  mensagens esperadas, pedem as entradas previstas e produzem as saídas corretas.
- O resultado aparece em **Releases** (tabela PASS/FAIL por teste) e na aba **Actions**.
- Na aba **Pull requests** existe um PR chamado **Feedback**. É lá que o professor
  comenta seu código. **Não feche nem faça merge desse PR.**

> 💡 Dica: siga **exatamente** os textos pedidos nos enunciados (acentos, pontuação e
> letras maiúsculas). Para o computador, `Olá, mundo!` e `ola mundo` são diferentes.

### Distribuição da pontuação

| Bloco | Pontos |
|---|:---:|
| 03 – PRIMM (Modificar + Criar) | 20 |
| 04 – Atividades (6) | 55 |
| 05 – Desafios (3) | 25 |
| **Total** | **100** |

O questionário de autoavaliação não vale nota automática, mas é parte da entrega.

---

## 📁 Estrutura

```
.
├── README.md
├── 01-conteudo/        Material explicativo
├── 02-exemplos/        Programas comentados para executar e estudar
├── 03-primm/           Sequência Predict–Run–Investigate–Modify–Make
├── 04-atividades/      Exercícios de aprendizagem e fixação
├── 05-desafios/        Problemas para resolução autônoma
└── 06-autoavaliacao/   Questões de revisão e reflexão
```

---

Dúvidas? Abra uma **Issue** neste repositório ou comente no Pull Request de Feedback.
