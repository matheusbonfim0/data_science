'''
Variável
  Espaço em memória, para guardar um valor durante a execução de um programa.

Ex: Você tem um programa para prever as vendas. Você vai precisar de uma 
  variável para, por exemplo, saber quantos meses para frente o programa deve
  prever. 


Varável tem um tipo
Ela pode ser:
  Texto
  Inteiro
  Float
  Lógico
  Declaração de variáveis no Py é implícita: fracamente tipada


Criar variável do tipo inteiro
  x = 1


Criar variável do tipo float
  y = 3.13


Criar variável do tipo string
  z = "Python"/'Python'


Criar variável do tipo lógica
  w = True, y = False 


Principais Operadores
  - +, -, /, *


O Py pode ser usado como uma calculadora
  x = 10
  y = 20
  z = 100
  w = (x + y) * z / 100


Exibir valores de console
  print("Este texto será impresso no console")
  print(x)
  print("Texto e duas variáveis", x, z)


Verificar Tipo
  type(x)
  x = 10 
  type(x)
  <class 'int'>

  y = "Python"
  type(y)
  <class 'str'>


Entrada de valores
  x = input("Informe o valor")
  Aguarda o usuário entrar o dado
  Criar a variável x como string e armazena o valor
  Independente do tipo de dado informado, a variável será sempre string


Conversão de valores
  x = int(z)
  w = str(m)
  t = float(1)

Estrutura de Decisão
  O programa deve decidir entre diferentes flucos, de acordo com entradas
  Ex: se a nota de um aluno é maior ou igual a 7, ele é aprovado, caso contrário
  ele é reprovado.

Operadores de comparação
  < - Menor que
  > - Maior que
  <=- Menor igual
  >=- Maior igual
  != - Diferente
  == - Igual

Operadores Lógicos
  and, or ou not

  Exemplos: 

    nota = 7 

    if nota >= 7:
      print("Aprovado")
    else:
      print("Reprovado")

Estrutura de repetição

  - While
    count = 1
    while count <= 5:
      print(count)
      count += 1

  - For
    - range -> (inicio, parada, incremento)
    - incremento é opcional mas pode ser negativo
    for n in range(0,10)

  Interrupções
    Cancela o laço
    - break
    reinicia o laço
    continue

  Criando Listas
    lst = [1, 2, 3, 4, 5]
    lst2 = [1, 2, 3, "4", True]
    lst3 = [12, [1, 2, 3, 4, 5], "a"]
    lst4 = list(range(0, 10))

  Listas
    Acesso primeiro elemento - indexadas em zero
    lst[0]

    Numero de elementos em uma lista
    len(lst)

  Dicionários
    - Conjunto de chave/valor associados
    - Declarados por chaves e separados por dois pontos
    Precos = {'lapis': 5.5, 'borracha': 7.0, 'caneta': 6.5}

  Sets
    - Conjuntos não ordenados e não repeditos de elementos
      animais = {'gato', 'cachorro'}

  Tuplas
    - São listas que não podem ser alteradas.
      tp1 = (1, 2, 3, 4, 5, 6)

  Numpy

    - Computação Cientifica: facilita operações matemáticas 
    avançadas e outros tipos de operações em muitos dados.
    - Objeto de Matriz Multidimensional.
    - Variedade de rotinas para operaçÕes rápidas em matrizes.
    - Os arrays NumPy têm um tamanho fixo na criação, ao contrário das listas
    Python (que podem crescer dinamicamente).
    - Os elementos em uma matriz NumPy devem ser todos do mesmo tipo de dados 
    e, portanto, terão o mesmo tamanho na memória.

    Ex: 
      import numpy as np
      
      -> Criar uma matriz unidimensional
      a = np.array([12, 34, 26, 18, 10])
      print(a)
      print(a.dtype)

  Pandas
    - Data Frame
    - Series
    Ex: 
      import pandas as pd

      dados = pd.read_csv('basecensus.csv')

  Módulos
    Conjuntos de funcionalidades organizadas em arquivos.

    Ex: 
      import statistics

      x = statistics.mean(z)
      y = statistics.median(z)

    Usando nome alternativo

    Ex:
      import statistics as est

      x = est.mean(z)
      y = est.meedian(z)

    Uso sem nome do módulo
      from statistics import mean, median

      mean()
      median()
    
    Ou
      from statistics import * 
  
  Packages
    Permite organizar módulos usando uma notaçao de pontos

    import cienciadedados.estatistica, cienciadedados.machinelearning

  Funções

    - Blocos de códigos reutilizáveis
    - Podem ser chamados de qualquer parte do programa
    - Podem ser chamados de outros programas

    Ex:
      
      def imprime():
        print('esta é uma função')
      
      imprime()
    
    Função com parâmetro

      def imprime(n):
        print(n)
      
      imprime('Impressão desse texto')

    Return

      def potencia(n):
        return n * n

      x = potencia(3)

    Default

      def intervalo(inic=1, fim=10):
        for inic in range(1, fim+1):
          print(inic)
      
      intervalo(1, 10)
      intervalo()
  
  Funções padrão

    Sem o uso de import
      abs()
      max()
      min()
      round()
      sum()      

'''