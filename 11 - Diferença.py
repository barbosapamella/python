'''
Lista de exercícios para treinamento de: (a) constantes; (b) operadores aritméticos; (c) variáveis; (d) expressões aritméticas; (e) entrada de dados; (f) saída de dados; (g) estrutura sequencial de controle de fluxo de execução. Essa lista não será considerada para fins avaliativos.

Diferença

Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

Exemplos de Entrada
5
6
7
8
Exemplos de Saída
DIFERENCA = -26
'''

A = int(input())
B = int(input())
C = int(input())
D = int(input())

DIFERENCA = (A*B-C*D)

print("DIFERENCA =",DIFERENCA)
