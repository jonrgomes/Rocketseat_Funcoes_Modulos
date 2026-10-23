# 📊 Formação Data Analytics — Rocketseat

## Módulo: Funções e Módulos

Repositório com os estudos, anotações e exercícios do módulo **Funções e Módulos** da Formação em Análise de Dados da [Rocketseat](https://www.rocketseat.com.br/), usando **Python**.

---

## 🎯 Objetivo do módulo

Aprender a organizar o código em partes reutilizáveis, evitando repetição e facilitando a manutenção, a leitura e a evolução dos scripts de análise de dados.

---

## 📚 Conteúdo

### 1. Funções
- Definição de funções com `def`
- Parâmetros e argumentos (posicionais e nomeados)
- Valores padrão de parâmetros
- Retorno de valores com `return`
- Retorno de múltiplos valores
- `*args` e `**kwargs`
- Escopo de variáveis (local e global)
- Funções `lambda`
- Docstrings e boas práticas de nomenclatura

### 2. Módulos
- O que são módulos e para que servem
- Importação com `import`, `from ... import` e `as`
- Módulos da biblioteca padrão (`math`, `random`, `datetime`, `statistics`, `os`, `json`, `csv`)
- Criação de módulos próprios
- O uso de `if __name__ == "__main__"`

### 3. Pacotes e organização do projeto
- Estrutura de pastas e arquivos `__init__.py`
- Separação de responsabilidades (leitura, tratamento, cálculo e exibição)
- Instalação de pacotes com `pip`
- Ambientes virtuais (`venv`)

---

## 🗂️ Estrutura do repositório

```
funcoes-e-modulos/
├── README.md
├── 01-funcoes/
│   ├── funcoes_basicas.py
│   ├── parametros_e_retorno.py
│   ├── args_kwargs.py
│   └── lambda.py
├── 02-modulos/
│   ├── importacoes.py
│   ├── biblioteca_padrao.py
│   └── meu_modulo.py
├── 03-pacotes/
│   └── utils/
│       ├── __init__.py
│       ├── calculos.py
│       └── formatacao.py
└── exercicios/
    └── ...
```

---

## 💻 Exemplos

### Função com parâmetros e retorno

```python
def calcular_media(valores):
    """Retorna a média de uma lista de números."""
    return sum(valores) / len(valores)


vendas = [1200, 850, 940, 1500]
print(calcular_media(vendas))
```

### Função com valor padrão

```python
def aplicar_desconto(preco, percentual=10):
    return preco - (preco * percentual / 100)


print(aplicar_desconto(200))      # 180.0
print(aplicar_desconto(200, 25))  # 150.0
```

### Criando e importando um módulo

`calculos.py`
```python
def soma(a, b):
    return a + b


def media(valores):
    return sum(valores) / len(valores)
```

`main.py`
```python
from calculos import soma, media

print(soma(2, 3))
print(media([10, 20, 30]))
```

### Usando a biblioteca padrão

```python
import statistics

dados = [10, 20, 20, 30, 40]
print(statistics.mean(dados))
print(statistics.median(dados))
print(statistics.mode(dados))
```

---

## ▶️ Como executar

```bash
# Clonar o repositório
git clone <url-do-repositorio>
cd funcoes-e-modulos

# (Opcional) Criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

# Executar um arquivo
python 01-funcoes/funcoes_basicas.py
```

**Requisitos:** Python 3.10+ e VS Code (ou outro editor).

---

## ✅ Checklist de estudos

- [ ] Criar funções com e sem retorno
- [ ] Usar parâmetros padrão, `*args` e `**kwargs`
- [ ] Entender escopo de variáveis
- [ ] Usar funções `lambda`
- [ ] Importar módulos da biblioteca padrão
- [ ] Criar um módulo próprio
- [ ] Organizar um projeto em pacotes
- [ ] Concluir os exercícios do módulo

---

## 🧠 Aprendizados

> Espaço para anotações pessoais sobre dúvidas, dicas e insights do módulo.

-
-
-

---

## 🔗 Referências

- [Rocketseat](https://www.rocketseat.com.br/)
- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)
- [Biblioteca padrão do Python](https://docs.python.org/pt-br/3/library/index.html)

---

## 👤 Autor

Feito durante os estudos da Formação Data Analytics da Rocketseat.