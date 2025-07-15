# Documentação Detalhada dos Resultados - MNIST SVM Classifier

## Configuração do Experimento

- **Número de amostras de treino:** 5.000
- **Número de amostras de teste:** 1.000
- **Total de classes:** 10 (dígitos de 0 a 9)
- **Kernel SVM:** RBF (C=1.0, gamma='scale')
- **Divisão dos dados:**
  - Treinamento: `Mtreino = M[:5000, :]`
  - Teste: `Mtest = M[5000:6000, :]`

## Resultados Obtidos

- **Acurácia global:** 0.9540 (95.40%)

### Matriz de Confusão

```
[[111   0   0   0   1   0   0   0   1   0]
 [  0 105   1   1   0   0   0   0   0   1]
 [  2   1  85   2   1   0   0   2   0   0]
 [  1   1   1 111   0   0   0   0   1   0]
 [  0   0   0   0  86   0   0   0   0   2]
 [  0   0   0   2   0  78   0   0   0   0]
 [  0   0   2   0   0   2 103   0   0   0]
 [  0   0   0   0   1   0   0  95   0   5]
 [  0   0   1   0   0   2   2   1  82   1]
 [  0   0   0   2   4   0   0   1   1  98]]
```

## Análise dos Resultados

### Pontos Fortes
- **Alta acurácia:** O modelo atingiu 95,4% de acerto, mesmo utilizando apenas 5.000 amostras para treino.
- **Generalização:** O desempenho no conjunto de teste é consistente, indicando boa capacidade de generalização.
- **Erros intuitivos:** A maioria dos erros ocorre entre dígitos visualmente semelhantes, o que é esperado para classificadores de imagens manuscritas.

### Limitações e Observações
- **Tempo de treinamento:** O tempo de treinamento cresce rapidamente com o aumento do número de amostras, devido à natureza do SVM.
- **Dígitos ambíguos:** Os principais erros estão em dígitos como 7 vs 9, 4 vs 9, e 8 vs 9, que possuem traços parecidos.
- **Distribuição dos erros:** A matriz de confusão mostra que a maioria dos erros está concentrada em pares específicos de classes, sugerindo que melhorias podem ser obtidas com técnicas de pré-processamento ou aumento de dados.

### Sugestões de Melhorias Futuras
- **Aumentar o conjunto de treino:** Pode melhorar a acurácia, mas com custo computacional maior.
- **Testar outros kernels ou ajustar hiperparâmetros:** Pode ajudar a separar melhor classes ambíguas.
- **Pré-processamento de imagens:** Normalização, aumento de dados ou extração de características podem ajudar a reduzir erros.

---

**Resumo:**
O classificador SVM com kernel RBF apresentou excelente desempenho no MNIST, mesmo com um conjunto de treino reduzido. A análise da matriz de confusão revela que os erros são, em sua maioria, compreensíveis e concentrados em dígitos visualmente próximos. O modelo é robusto para aplicações didáticas e demonstra o potencial do SVM para tarefas de classificação de imagens. 