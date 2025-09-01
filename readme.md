
# Simulação da Propagação de Doenças com Autômatos Celulares (Modelo SIR+M)

Este projeto apresenta uma simulação computacional da propagação de doenças infecciosas (como dengue) em uma população, utilizando autômatos celulares e o modelo SIR estendido para incluir óbitos e vacinação.

## Objetivo

Visualizar e analisar como doenças podem se espalhar em uma população, considerando fatores como recuperação, mortalidade, vacinação e isolamento social.

## Descrição do Modelo

- Cada célula da grade representa um indivíduo, que pode estar em um dos quatro estados:
  - Suscetível (S)
  - Infectado (I)
  - Recuperado/Imune (R)
  - Morto (M)
- A propagação ocorre localmente: infectados podem transmitir a doença para vizinhos suscetíveis.
- Indivíduos infectados podem se recuperar, morrer ou continuar transmitindo.
- Indivíduos suscetíveis podem ser vacinados e se tornam imunes.
- O isolamento social pode ser ativado para reduzir a propagação.
- O código gera uma animação mostrando a evolução dos estados ao longo do tempo.

## Parâmetros do Código

- Tamanho da grade: 50x50
- Tempo de simulação: 100 passos
- Probabilidade de infecção: 0.3
- Probabilidade de recuperação: 0.1
- Probabilidade de morte: 0.02
- Taxa de vacinação: 0.005
- Isolamento social: ativado por padrão

## Como executar

1. Instale as dependências:
   ```
   pip install numpy matplotlib
   ```
2. Execute o script principal:
   ```
   python epidemiology/epidemiology_2025_2.py
   ```

## Créditos

Autor do código: Kelves N D Costa

## Referências

- Kermack, W.O., McKendrick, A.G. (1927). A Contribution to the Mathematical Theory of Epidemics.
- Keeling, M.J., Rohani, P. (2008). Modeling Infectious Diseases in Humans and Animals.

---