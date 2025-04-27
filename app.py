
import os 

restaurante = [{'nome': 'Central', 'categoria': 'buffet', 'ativo': True},
               {'nome': 'Bobs', 'categoria': 'fast food', 'ativo': False},
               {'nome': 'Japex', 'categoria': 'frutos do mar', 'ativo': False}] 

def main():
    ''' Função principal que inicia o programa '''
    os.system ('cls') 
    exibir_titulo()
    exibir_menu()
    exibir_opcao()
    
def exibir_titulo():
    ''' Exibe o título estilizado do projeto na tela '''
    print('*** 𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼 ***\n')

def exibir_menu():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print("3. Alterar ativação do Restaurante")
    print('4. Sair\n')

def exibir_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input ("Escolha uma opção "))
        match opcao_escolhida:
                case 1:
                    cadastrar_restaurante()
                case 2:
                    listar_restaurantes()
                case 3:
                    alterar_ativacao()
                case 4:
                    finalizar_app()  
                case _:
                    opcao_invalida()
    except:
            opcao_invalida()

def finalizar_app(): 
    ''' Exibe mensagem estilizada de finalização do aplicativo '''
    os.system ('cls')
    print ("𝕒𝕡𝕝𝕚𝕔𝕒𝕔̧𝕒̃𝕠 𝕖𝕟𝕔𝕖𝕣𝕣𝕒𝕕𝕒\n")

def chamar_menu (msg):
    ''' Solicita uma tecla para voltar ao menu principal 
    Outputs:
    - Retorna ao menu principal
    '''
    input (msg)
    main()

def imprimir_cabecalho(msg):
    ''' Exibe um subtítulo estilizado na tela 
    Inputs:
    - msg: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '=' * len(msg)
    print(linha)
    print(msg)
    print(f'{linha}\n')

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida!\n')
    texto = "opção inválida. Digite uma tecla para volta ao menu"
    chamar_menu(texto)

def cadastrar_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    Inputs:
    - Nome do restaurante
    - Categoria
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    texto = '*** Cadastramento de Restaurante ***'
    imprimir_cabecalho(texto)
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    restaurante.append({'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo': False})
    texto = f'\nRestaurante {nome_restaurante} cadastrado com sucesso! Tecle algo para continuar.'
    chamar_menu(texto)

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    texto = '*** Listagem de Restaurantes ***'
    imprimir_cabecalho(texto)
  
    if len(restaurante) > 0:
        print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
        for conteudo in restaurante:
            status = 'ativado' if conteudo['ativo'] == True else 'desativado' 
            print(f'- {conteudo['nome'].ljust(20)} | {conteudo['categoria'].ljust(20)} | {status}')
        texto = f'\nRestaurantes listados com sucesso! Tecle algo para continuar.'
    else:
        texto = 'Lista de restaurantes inexistente. Tecle algo para continuar.'
    chamar_menu(texto)

def alterar_ativacao():
    ''' Altera o estado ativado/desativado de um restaurante 
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    texto = '*** Alterar ativação de Restaurante ***'
    imprimir_cabecalho(texto)
    nome_restaurante = input('Digite o nome do restaurante para alteração da ativação: ')

    encontrado = False
    for conteudo in restaurante:
        if conteudo['nome'] == nome_restaurante:
            encontrado = True
            conteudo['ativo'] = not conteudo['ativo']
            if conteudo['ativo'] == True:
                status = 'ativado'
            else:
                status = 'desativado'
            texto = f'\nRestaurante {nome_restaurante} {status} com sucesso! Tecle algo para continuar.'
                
    if encontrado == False:
        texto = f'\nRestaurante {nome_restaurante} não encontrado. Tecle algo para continuar.'        
         
    chamar_menu(texto)

if __name__ == '__main__': 
    main()