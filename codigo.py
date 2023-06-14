vetor = ['x','y','z'] # Matriz "vetor" que armazena strings, no caso 'x', 'y' e 'z'.
x = 'r' in vetor # Verificação para descobrir se 'r' está armazenada na matriz "vetor", caso verdadeiro, a variável x obterá o valor True, caso contrário x obtera o valor False. Neste caso, x = True

if x is True: # Verificação do valor da variável x, neste caso, se x for verdadeiro, o programa executará a linha 5.
  print("Correto") # O programa imprime a palavra "Correto".
elif x is not False: # Outra condicional igual a linha 4, verificando se x é verdadeiro. Caso x = True, o programa executa a linha 7. (Essa linha de código só é executada caso o teste da linha 4 retornar x = False)
  print("Continua Correto") # O programa imprime as palavras "Continua Correto".
else: # Caso as condições não sejam satisfeitas, essa linha dá o comando para o programa executar a linha 9. (Essa linha de código só é executada quando os testes anteriores retornarem x = False)
  print("Errado") # O programa imprime a palavra "Errado".
