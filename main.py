# Solicita ao usuário que digite um ano e armazena esse 
        # valor na variável 'ano'.
# A função 'int()' é usada para converter a entrada de 
        # texto para um número inteiro,
        # pois estamos trabalhando com anos que são valores numéricos inteiros.
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto com base nas regras definidas:
# 1. O ano deve ser divisível por 4 (ano % 4 == 0) E
# 2. Não deve ser divisível por 100 (ano % 100 != 0) OU
# 3. Deve ser divisível por 400 (ano % 400 == 0).
# O operador lógico 'and' é usado para garantir que ambas as 
        # condições sejam verdadeiras simultaneamente,
        # e o operador 'or' é usado para incluir a exceção 
        # dos anos divisíveis por 400.
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    
    # Se o ano atende a essas condições, ele é bissexto e esta 
            # mensagem é impressa, informando o usuário.
    print(f"O ano {ano} é bissexto.")
    
else:
    
    # Se o ano não atende a essas condições, ele não é 
            # bissexto, e esta mensagem é impressa.
    print(f"O ano {ano} não é bissexto.")
