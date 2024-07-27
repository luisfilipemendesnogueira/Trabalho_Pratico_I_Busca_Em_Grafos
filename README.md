# Trabalho Prático I

Trabalho proposto da disciplina Algoritmos e Estrutura de Dados III em linguagem python.

## 1. Objetivos.

- Desenvolver a habilidade de programação de algoritmos em grafos.
- Reforçar o aprendizado sobre os algoritmos de busca em grafos.
- Aplicar os conhecimentos em algoritmos para resolver problemas reais.
  
## 2. Descrição

Grafos podem ser utilizados para representar e resolver computacionalmente uma vasta quantia de problemas. Nessa atividade resolveremos o problema do labirinto através de algoritmos em grafos. O labirinto será representado por uma matriz onde cada posição traz informação sobre determinada coordenada do labirinto. Essa matriz será informada ao programa através de um arquivo de texto, com apenas quatro possíveis caracteres: ‘#’ representando paredes, ‘ ’ para as passagens, ‘S’ representando o ponto de início e ‘E’, a saída do labirinto. Veja um exemplo de arquivo abaixo:

![toy](https://github.com/user-attachments/assets/4c09e5a5-7a11-434c-adef-217d5dcf44ac)

Esse labirinto pode ser resolvido ao encontrar qualquer caminho de S (nó (1,0)) a E (nó (1,8)), no grafo apresentado a seguir.

![maze_example](https://github.com/user-attachments/assets/ab91550f-44dc-43ea-b51d-618bdcb37511)

Nesse exemplo é fácil notar que o ́unico caminho de S a E é:
(1 ,0) (1 ,1) (1 ,2) (1 ,3) (2 ,3) (3 ,3) (3 ,4) (3 ,5) (3 ,6) (3 ,7) (2 ,7) (1 ,7)(1 ,8)
Foram gerados 5 labirintos de teste com auxílio do site Maze Generator1. Os arquivos também estão na pasta maze em anexo.
O algoritmo deve aplicar a busca em largura e em profundidade.

## 3. Interação com o usuário:

A interação com o usuário deve ocorrer na função main do seu programa. O mesmo deve solicitar ao usuário o arquivo de entrada e, após a execução, informar o caminho de S a E, bem como o tempo de execução. Caso o caractere 0 seja informado, o programa deve encerrar. Segue um exemplo de interação com o programa:

Informe o arquivo (0 para sair ) : <maze/toy.txt>

Processando ...

Caminho : (1 ,0) (1 ,1) (1 ,2) (1 ,3) (2 ,3) (3 ,3) (3 ,4) (3 ,5) (3 ,6) (3 ,7) (2 ,7)(1 ,7) (1 ,8)

Tempo : 0.005 s

Informe o arquivo (0 para sair ) : <0>
