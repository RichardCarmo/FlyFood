# FlyFood

Projeto da disciplina PISI2 — Desenvolvimento de um algoritmo de roteamento para entregas com drones.

## Contexto

No ano de 2030, o trânsito está caótico e as empresas de delivery não conseguem mais fazer entregas em um tempo aceitável. Um ex-aluno do BSI-UFRPE cria a empresa **FlyFood**, que realiza entregas utilizando drones.

Os drones podem sair do local de origem do pedido com vários pedidos no compartimento de carga e entregá-los em vários endereços espalhados pela cidade. Porém, a capacidade das baterias ainda é um problema, então é preciso otimizar ao máximo o trajeto do drone para concluir todas as entregas dentro do ciclo da bateria.

O objetivo é elaborar um **algoritmo de roteamento**: um algoritmo capaz de definir o menor trajeto para a realização de todas as entregas do drone.

## Modelagem

Para abstrair as questões de encontrar endereços e obter coordenadas GPS, o problema utiliza uma **matriz** que representa os pontos da cidade:

- O ponto R é considerado, por convenção, a **origem** e o **retorno**, sendo representado pela coord. (0, 0).
- Cada ponto de entrega é identificado por uma letra ('A', 'B', 'C', 'D', ...).

O drone **não anda na diagonal** — ele só percorre a matriz na horizontal ou na vertical. A distância é medida em **dronômetros**.

## Formato de entrada

O arquivo de entrada segue o formato texto abaixo: a primeira linha traz a quantidade de linhas e colunas da matriz, e as linhas seguintes representam a matriz em si, com "0" indicando posições vazias. Exemplo (entradas/matriz1.txt):

```text
4 5
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0
```


## Saída esperada

O projeto conta com duas implementações do algoritmo de roteamento, cada uma em seu próprio arquivo. Ambas vão ler a mesma entrada e resolver o mesmo problema, mas com estratégias diferentes, por isso o formato de saída de cada uma é documentado separadamente.

src/main.py - força bruta (**permutação completa**): 

```text
Melhor trajeto: R -> A -> D -> C -> B -> R
Distância total: 14
Tempo percorrido: 14 minutos
```

main2.py - busca com poda (**backtracking otimizado**):

```text
Melhor trajeto: A D C B
Distância total: 14 dronômetros
Tempo de execução do sistema: 0.1234 ms
```


## Estrutura do projeto

```text
FlyFood/
├── entradas/
│   ├── matriz1.txt      (4 pontos de entrega)
│   ├── matriz2.txt      (6 pontos de entrega)
│   ├── matriz3.txt      (8 pontos de entrega)
│   ├── matriz4.txt      (10 pontos de entrega)
│   └── matriz5.txt      (12 pontos de entrega)
├── src/
│   ├── leitura_entrada.py   # leitura e tratamento do arquivo de entrada
│   └── main.py              # algoritmo de força bruta (permutação completa)
├── main2.py                 # algoritmo otimizado (backtracking com poda)
├── .gitignore
└── README.md
```


## Como rodar o projeto 

**Pré-requisito**: ter o Python 3 instalado. 

1. Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/RichardCarmo/FlyFood.git
cd FlyFood
``` 

2. Rodando a versão de força bruta (src/main.py):

```bash
python src/main.py
```

3. Rodando a versão otimizada (main2.py):

```bash
python main2.py
```