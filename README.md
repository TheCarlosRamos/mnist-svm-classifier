
# MNIST SVM Classifier

Classificador de dígitos manuscritos do MNIST usando SVM (Support Vector Machine) com kernel RBF.

## Como Executar

### Pré-requisitos

Instale as dependências necessárias:

```bash
pip install numpy scipy scikit-learn matplotlib seaborn
```

### Uso Básico

1. Coloque o arquivo `mnist_784.csv` na mesma pasta do script (`svm/`).

   [mnist_784](https://api.openml.org/d/554)

3. Execute o script:

```bash
python3 exemplo_mnist.py
```

### Parâmetros Ajustáveis

No bloco `__main__` do arquivo `exemplo_mnist.py`, você pode modificar:

```python
Mtreino = M[:5000, :]   # Altere o número de amostras de treino
Mtest = M[5000:6000, :] # Altere o número/intervalo de teste
```

---

## O que o Código Faz

### Leitura de Dados
- Processa o CSV do MNIST, ignorando o cabeçalho.
- Converte pixels (0-255) e rótulos para arrays numpy.
- Opcionalmente salva em formato `.mat` para carregamento rápido futuro.

### Classificação
- Utiliza SVM com kernel RBF (default: `C=1.0`, `gamma='scale'`).
- Divide automaticamente em conjuntos de treino/teste.

### Avaliação
- Calcula acurácia global.
- Gera matriz de confusão visual/anotada.
- Mostra exemplo aleatório com predição.

---

## Melhorias Implementadas

### Tratamento Robusto de Dados
- Skip de cabeçalho.
- Conversão segura de tipos (`int(float(x))`).
- Tratamento de linhas corrompidas.

### Otimizações
- Cache de dados em formato `.mat`.
- Amostragem estratificada implícita (mantém distribuição das classes).

### Visualização
- Matriz de confusão com Seaborn.
- Plot de dígitos com matplotlib.

---

## Análise dos Resultados

### Pontos Fortes
- Alta acurácia (~95.4%) com pouco treino (5k amostras).
- Boa generalização (performance consistente no teste).
- Visualização intuitiva dos erros.

### Limitações
- Tempo de treinamento cresce exponencialmente com mais dados.
- Dificuldade com dígitos ambíguos (ex: 7 vs 9, 4 vs 9).


---

