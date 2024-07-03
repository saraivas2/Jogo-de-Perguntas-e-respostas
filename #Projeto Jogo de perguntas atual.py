#Projeto Jogo de perguntas Disciplina de Introdução a Programação I - UFRPE
import csv
import pandas as pd
from random import Random
from time import sleep
from csv import DictReader, DictWriter
from typing import SupportsAbs
contar = quant = 0

def jogadores(opcao): 
    with open('jogador.csv', 'r', encoding='latin-1') as f: #abre o arquivo .csv como a variável f
        reader = csv.DictReader(f) #a variável f através do componente csv.DictReader é carregado na variável reader
        df = pd.DataFrame(reader) # a variável reader carrega o DataFrame na variável df
    if opcao==0:
        df2 = df.sort_values(['STATUS','PONTOS'], ascending=[False, False]) #a variável df através do componente sort_values escalona as colulas Status e Pontos pelo maior valor
        print()
        print('=============================RANKING DE JOGADORES============================')
        print('=============================================================================')
        print('|     USUARIO       |              NOME           |   STATUS   |   PONTOS   |')
        print('=============================================================================')
        for index, row in df2.iterrows(): #ler linha por linha do df.
            sleep(0.3)
            A = row['USUARIO']
            B = row['NOME']
            C = row['PONTOS']
            D = int(row['STATUS'])
            if D==0:
                status_visto='Bronze'
            if D==1:
                status_visto='Prata'
            if D==2:
                status_visto='Ouro'
            if D>=3:
                status_visto='Platina'

            print('|{:<18} | {:^27} | {:^10} | {:^10} |'.format(A, B, status_visto, C))
        print('=============================================================================')
        print('\n')
        
    if opcao==1:
            print()
            print('================jOGADORES CADASTRADOS===============')
            print('====================================================')
            print('| ID  |    USUARIO           |      NOME            ')
            print('====================================================')
            
            for i, row in df.iterrows():
                sleep(0.3)
                B = row['USUARIO']
                C = row['NOME']
                
                print('| {:2}  | {:<18}   |    {:<2}'.format(i, B, C))
            print('====================================================')
            print('\n')

def alterar():
    
    perg=int(input('Digite o ID da pergunta: ')) # a variável perg recebe um número inteiro
    with open('perguntas.csv', 'r', encoding='latin-1') as f:
        reader = csv.DictReader(f)
        df = pd.DataFrame(reader)
        while True:
            print('=========================================================================================')
            print('Para corrigir pergunta (P), Letra (L+(A,B,C,D ou E)), Resposta (R), Nível (N) ou (0=Sair)?\n')
            print('=========================================================================================')
        
            escolha=str(input('Digite sua escolha (Sair=0): ')).strip().lower() #variável escolha assume os valores acima: P, LA, LB, LC, LD, LE, R, N e 0. 
                                                                                #strip retira espaços em branco e lower passa para minúsculas as letras.

            if escolha=='0':
                principal()
                continue
            if escolha=='p':
                dfperg=str(input('Digite a pergunta correta: ')) #variável dfperg recebe a pergunta (string)
                df.loc[perg, 'PERGUNTA'] = dfperg   #a variável perg pesquisa pelo index a posição da linha e substitui a célula com o valor de dfperg
            if escolha=='la':
                dfla=str(input('Digite a letra "a" correta: '))
                df.loc[perg, 'LETRAA'] = dfla
            if escolha=='lb':
                dflb=str(input('Digite a letra "b" correta: '))
                df.loc[perg, 'LETRAB'] = dflb
            if escolha=='lc':
                dflc=str(input('Digite a letra "c" correta: '))
                df.loc[perg, 'LETRAC'] = dflc
            if escolha=='ld':
                dfld=str(input('Digite a letra "c" correta: '))
                df.loc[perg, 'LETRAD'] = dfld
            if escolha=='le':
                dfle=str(input('Digite a letra "e" correta: '))
                df.loc[perg, 'LETRAE'] = dfle
            if escolha=='r':
                dfr=str(input('Digite a resposta correta: '))
                df.loc[perg, 'RESPOSTA'] = dfr
            if escolha=='n':
                dfn=str(input('Digite o nível da questão corret0: '))
                df.loc[perg, 'NIVEL'] = dfn
            df.to_csv('perguntas.csv', index=False) #salva as alterações no arquivo perguntas.csv, sem a inclusão de uma coluna do index.

def excluir():

    pergunta=int(input('Digite o ID da pergunta: '))
    print()
    resp=int(input(f'Você confirma a exclusão da questão de ID << {pergunta} >>? Se Sim (0) - Não (1): '))
    print()
    with open('perguntas.csv', 'r', encoding='latin-1') as f:
        reader = csv.DictReader(f)
        df = pd.DataFrame(reader)
        df=df.drop(index=pergunta) #exclui a linha relativa ao index da variável pergunta
        if resp==0: #se a variável resp recebeu um valor inteiro 0, será excluída linha indicada pela variável pergunta, se um, não será excluída
            df.to_csv('perguntas.csv', index=False)
            print('Pergunta excluída com sucesso!')
        else:
            principal()

def buscar(): # Buscar pelo valor do index
    
    with open('perguntas.csv', 'r', encoding='latin-1') as f:
        reader = csv.DictReader(f)
        df = pd.DataFrame(reader)
        
        while True:
            print()
            busc=int(input('Pesquisa realizada por <<ID>> (Sair=-1): '))
            print()
            if busc==-1:
                principal()
                continue
            else:
                print(f"Pergunta: {busc}-{df.loc[busc, 'PERGUNTA']}") #buscar pelo index através da variável busc
                print(f"Letra a): {df.loc[busc, 'LETRAA']}")
                print(f"Letra b): {df.loc[busc, 'LETRAB']}")
                print(f"Letra c): {df.loc[busc, 'LETRAC']}")
                print(f"Letra d): {df.loc[busc, 'LETRAD']}")
                print(f"Letra e): {df.loc[busc, 'LETRAE']}")
                print(f"Resposta: {df.loc[busc, 'RESPOSTA']}")
                print(f"Nível: {df.loc[busc, 'NIVEL']}")

def lista_perguntas():
    print()
    with open('perguntas.csv', 'r', encoding='latin-1') as f:
        reader = csv.DictReader(f)
        df = pd.DataFrame(reader)
        
        print('=============================LISTA DE PERGUNTAS==============================')
        for i, row in df.iterrows():
            sleep(0.3)
            P = row['PERGUNTA']
            A = row['LETRAA']
            B = row['LETRAB']
            C = row['LETRAC']
            D = row['LETRAD']
            E = row['LETRAE']
            R = row['RESPOSTA']
            N = int(row['NIVEL'])
            print('ID: {} - Pergunta:{} '.format(i, P))
            print('Letra a)  {} '.format(A))
            print('Letra b)  {} '.format(B))
            print('Letra c)  {} '.format(C))
            print('Letra d)  {} '.format(D))
            print('Letra e)  {} '.format(E))
            print('Resposta: {} '.format(R))
            if N==0: #converte o valor encontrado no nível (0=Baixo, 1=Intermediário, 2=Alto, 3=Altíssimo)
                nivel_visto='0=Baixo'
            if N==1:
                nivel_visto='1=Intermediário'
            if N==2:
                nivel_visto='2=Alto'
            if N>=3:
                nivel_visto='3=Altíssimo'
            print('Nível:    {} '.format(nivel_visto))
            print('=============================================================================')
    
def jogo():
    respostascertas=pfeitas = nivelperg = pontosperg = cont=0
    lista=data=[] 

    usuario=int(input('Digite o número "ID" do jogador: '))
            
    while True:
                
        file='perguntas.csv'
        d = DictReader(open(file, encoding='latin-1'))
        
        for row in d:
            data.append(row)

        r = Random() 
        conta=len(data)
        for cont in range(conta):
            ask = data[r.randrange(0, conta,1)] #randomização das perguntas
            if not (ask['PERGUNTA']) in lista: #Consulta a lista se já tem a pergunta, para evitar repetição das perguntas selecionadas pela randomização
                print('Pergunta:', ask['PERGUNTA'])
                sleep(0.2)
                print('a) ', ask['LETRAA'])
                print('b) ', ask['LETRAB'])
                print('c) ', ask['LETRAC'])
                print('d) ', ask['LETRAD'])
                print('e) ', ask['LETRAE'])
                sleep(0.3)
                nivelperg=int(ask['NIVEL']) 
                cont+=1
                resposta=input('Digite a letra da resposta: ').strip().lower()
                sleep(0.3)
                pfeitas+=1
                    
                if resposta==ask['RESPOSTA']: #Consulta se a resposta é correta 
                    print()
                    print('{:-^34}'.format('\033[32mVocê acertou!!!!!!!!!!!\033[m'))
                    print()
                    respostascertas+=1
                        
                    if nivelperg == 0: #sendo correta a resposta, verifica o nível da questão
                        pontosperg+=10 # atribui 10 pontos, se nível é igual a zero
                    if nivelperg == 1:
                        pontosperg+=20
                    if nivelperg==2:
                        pontosperg+=50
                    if nivelperg==3:
                        pontosperg+=100

                    print()
                    lista.append(ask['PERGUNTA']) # coloca a pergunta selecionada pela randomização na lista                  
                else:
                    print('{:-^34}'.format('\033[32mAhhhhh, você errou!\033[m'))
                    print()
        df = pd.read_csv('jogador.csv', encoding='latin-1') #abre o arquivo .csv e armazena na variável df
        df.head() #traz as primeiras linhas no DataFrame 
        df.loc[usuario, 'PONTOS'] += pontosperg #pesquisa pelo index, e soma o valor de pontosperg ao valor de 'PONTOS'
            
        a=int(df.loc[usuario, 'PONTOS']) #armazena o valor inteiro de 'PONTOS' na variável 'a'
        
        if a <=1000: 
            df.loc[usuario,'STATUS']=0 # sendo a menor que 1000 pontos, atribui o valor 0 para 'STATUS'.
        if a>1000 and a<=5000:
            df.loc[usuario,'STATUS']=1
        if a>5000 and a<=10000:
            df.loc[usuario,'STATUS']=2
        if a>10000:
            df.loc[usuario,'STATUS']=3
        df.to_csv('jogador.csv', index=False)

        porcentagemacertos= format(respostascertas/pfeitas * 100, '0.02f')
        print(f' Das {pfeitas} perguntas, você acertou {porcentagemacertos}% - fez {pontosperg} pontos')
        print()
        condition = str(input('Você gostaria de jogar novamente? [S / N]: ')).strip().lower()
        print()
                
        if condition!='s':
            break
        else:
            continue

def cadastro_jogador():
    print('=============================================')    
    print('{:-^34}'.format('\033[32m==============Cadastrar jogador==============\033[m'))
    print('=============================================')    
    print()
    file1 = 'jogador.csv' 
    usuario=str(input('Crie o nome do usuário (Sair): ')).strip().lower()
    print()
    
    if usuario=='sair': 
        principal()
    else:
        file1_name = file1
        try:
            with open(file1_name, encoding='latin-1') as doc: #abre o arquivo .csv e armazena na variável doc
                reading=DictReader(doc)
                       
                for line in reading:
                    if usuario==str(line['USUARIO']): #se já existe o usuário cadastrado, solicita criar outro usuário
                        print('{:-^34}'.format('\033[32mNome de Usuário já utilizado!\033[m'))
                        print()
                        cadastro_jogador()
                    else:
                        
                        parameter = 'a' #adicionar novos

        except FileNotFoundError:
                parameter = 'w' #escrever

        with open(file1_name, parameter) as doc:
            header1 = ['USUARIO', 'NOME', 'IDADE', 'PONTOS', 'STATUS'] #cabeçalho colocado na primeira linha do arquivo.csv

            writing2 = DictWriter(doc, fieldnames=header1) #conteúdo do .csv

            if parameter == 'w':
                writing2.writeheader() #escreve uma linha com os nomes dos campos
            nome1=str(input(f'Digite o Nome Completo de {usuario}: ')) #adiciona os novos dados nas variáveis
            idade1= str(input(f'Digite a idade de {usuario}: '))
            pontos1= 0
            status1 = 0
            print()                       
            print('{:-^34}'.format('\033[32mCadastro incluido com sucesso!\033[m\n'))

            writing2.writerow({ 
                'USUARIO': usuario, #incorpora os dados no .csv
                'NOME': nome1,
                'IDADE': idade1,
                'PONTOS': pontos1,
                'STATUS': status1, 
            })
            print('{:-^34}'.format('\033[32mArquivo Salvo!\033[m'))

def cadastro_perguntas():
    
    file = 'perguntas.csv'
    file_name = file
        
    try:
        with open(file_name, encoding='latin-1') as doc:
        
            parameter = 'a'

    except FileNotFoundError:
        parameter = 'w'

    quant = int(input('Quantos? ')) # Quantas perguntas quer cadastrar?
    print()

    with open(file_name, parameter) as doc:
        header = ['PERGUNTA', 'LETRAA', 'LETRAB', 'LETRAC', 'LETRAD', 'LETRAE', 'RESPOSTA', 'NIVEL']

        writing = DictWriter(doc, fieldnames=header)

        if parameter == 'w':
            writing.writeheader()
    
        while contar < quant: #dependendo do valor da variável quant, contar será quant-1.
            for contar in range (quant):
                print('\n', '{:-^34}'.format(f'{contar+1})Pergunta'))

                perguntafeita = input('Digite a Pergunta ou Sair=0: ').strip()

                if perguntafeita != '0': #adicona novas perguntas
                    leta = str(input('Letra a): '))
                    letb=str(input('Letra b): '))
                    letc  = str(input('Letra c): '))
                    letd = str(input('Letra d): '))
                    lete = str(input('Letra e): '))
                    respostacorreta=str(input('Digite a letra correta: ')).strip().lower()
                    nivelesc=int(input('Qual o nível (baixo=0, intermediário=1, alto=2, altíssimo=3)?: '))

                    print('{:-^34}'.format('\033[32mCadastro incluido com sucesso!\033[m\n'))

                    writing.writerow({
                        'PERGUNTA': perguntafeita,
                        'LETRAA': leta,
                        'LETRAB': letb,
                        'LETRAC': letc,
                        'LETRAD': letd, 
                        'LETRAE': lete, 
                        'RESPOSTA': respostacorreta,
                        'NIVEL': nivelesc
                    })
                else:
                    principal()
                contar+=1

                print('{:-^34}'.format('\033[32mArquivo Salvo!\033[m'))
    
def principal():

    while True:
        print()
        print('===========================================')
        print('      JOGO DE PERGUNTAS E RESPOSTAS')
        print('===========================================')
        print('1 - Iniciar jogo')
        print('2 - Cadastrar Jogador')
        print('3 - Cadastrar novas perguntas')
        print('4 - Buscar perguntas')
        print('5 - Alterar perguntas')
        print('6 - Excluir perguntas')
        print('7 - Listar de Perguntas')
        print('8 - Ver Ranking dos jogadores')
        print('9 - Sair')
        print('===========================================')
        
        iniciar=str(input('Escolha uma opção: '))
        
        if iniciar == '1':
            print()
            sleep(0.2)
            jogadores(1)
            jogo()
        
        elif iniciar=='2':
            cadastro_jogador()
        
        elif iniciar == '3':
            print()
            sleep(0.2)
            cadastro_perguntas()

        elif iniciar=='4':
            print()
            sleep(0.2)
            print('{:-^34}'.format('\033[32mAlterar perguntas!\033[m'))
            buscar()   
        
        elif iniciar=='5':
            print()
            sleep(0.2)
            print('{:-^34}'.format('\033[32mAlterar perguntas!\033[m'))    
            alterar()

        elif iniciar=='6':
            print()
            sleep(0.2)
            print('{:-^34}'.format('\033[32mExcluir perguntas\033[m'))
            excluir()
        
        elif iniciar=='7':
            print()
            sleep(0.2)
            lista_perguntas()

        elif iniciar=='8':
            print()
            sleep(0.2)
            jogadores(0)
        
        elif iniciar=='9':
            print()
            sleep(0.2)
            print('{:-^34}'.format('\033[32mVocê saiu do jogo!\033[m'))
            break

        else:
            print()
            print('{:-^34}'.format('\033[32mOpção não disponível, tente novamente!\033[m\n'))

principal()
