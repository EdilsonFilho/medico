# -*- coding: utf-8 -*-
import requests
import json
import getpass 


print('########################################')
print('# -----------------------------------  #')
print('#       PAINEL DE CONTROLE GERAL       #')
print('#      VISAO GERAL SISTEMA COVID       #')
print('# -----------------------------------  #')
print('########################################')

def main():

    option = int(input('Ola, o que desejas fazer?\n 0.Login\n 1.Cadastrar-se\n 2.Sair\n'))
    ###Cadastrando-se no sistema
    if option == 1:
        inputNameUser = input('Digite seu nome completo: \n')
        inputCategoryUser = int(input('Digite o número correspondente à sua categoria:\n 11.paciente\n 22.medico\n'))
        inputpasswordUser = getpass.getpass(prompt='Digite sua Senha: ', stream=None)
        inputCpfUser = int(input('Digite seu cpf, só os numeros: \n'))
        print(inputCategoryUser)
        if  inputCategoryUser == 11:
            inputDateUser = input('Digite a data para a consulta no formato dd/mm/aaaa: \n')
            inputCategoryUser ='paciente'
        else:
            inputDateUser ='00/00/0000'
            inputCategoryUser ='medico'
        
        dados = {
            "name": inputNameUser,
            "categoryUser": inputCategoryUser,
            "password": inputpasswordUser,
            "cpf": inputCpfUser,
            "date":inputDateUser ,
            "description": ""
        }
        
        url = 'http://localhost:8000/scheduling//'
        response = requests.post(url=url,json=dados)

        if response.status_code >= 200 and response.status_code <=299:
            #sucesso em cadastrar usuario!
            #print('Status Code', response.status_code)
            print('########################################')
            print('#SEU CADASTRO FOI REALIZADO COM SUCESSO#')
            print('#    CONTINUE A USAR O SISTEMA!!!      #')
            print('########################################')
            option = 7
            
        
        #caso nao tenha dado certo fazer o cadastro essas mensagens pode m ser consumidas 
        else:
            #Erros
            print('Status Code', response.status_code)
            print('Reason', response.reason)
            print('Texto',response.text)
            option = 7
        
    
    
    ###sair do sistema
    if option == 2:
        print('saindo')
        print('-------------------')
        
    ###Logando 
    if option == 0:
        request = requests.get('http://localhost:8000/scheduling//')
        dados = request.json()
        print('Bem vindo ao SISCOVID')
        consultaNome = input('digite seu nome:  ')
        consultaSenha = getpass.getpass(prompt='Digite sua Senha: ', stream=None)
        i= 0
        for d  in dados:
            if dados[i]['name'] == consultaNome:
                if dados[i]['password'] == consultaSenha:
                    if dados[i]['categoryUser'] == 'paciente': #no caso de ser pacinte o usuario logado
                        print('\nSeja Bem vindo, {}'.format(consultaNome))
                        if dados[i]['exam'] == 'Sem resultados de exames':
                            print('Mensagem: {}'.format(dados[i]['exam']))
                            print('em breve voce podera fazer nova consulta\n')
                            option = 2
                        else:
                            print('Mensagem: {}\n'.format(dados[i]['exam']))
                            print('O resultado eh: {}'.format(dados[i]['description']))
                            print('Obrigado por usar o sistema!')
                            option = 2    
                    elif dados[i]['categoryUser'] == 'medico':#caso o usuario logado seja medico
                        option = 4
            else:
                i+=1
    ##caso o usuario logado seja medico, tera poderes de consultar cpfs e cadastras laudo do exame
    if option == 4:
        print('\nSeja Bem vindo, {}'.format(consultaNome))
        option = int(input('Ola, o que desejas fazer?\n 5.Ver todos os pacientes sem exame\n 6.Pesquisar CPF\n 8.Laudar um exame\n 2.Sair\n'))
        
        
    if option == 5:# ver paciente sem exames
        request = requests.get('http://localhost:8000/scheduling//')
        dados = request.json()
        i = 0
        count =0
        print('Dados dos pacientes SEM resultados em seus exames\n')
        
        for i in range(len(dados)):
            if dados[i]['exam'] == 'Sem resultados de exames': 
                count+=1
                #print('Id: {}'.format(dados[i]['id']) )
                print('Nome: {}'.format(dados[i]['name']) )
                print('CPF: {}'.format(dados[i]['cpf']) )
                print('Data da consulta: {}'.format(dados[i]['date']) )
                print('Status Exames: {}'.format(dados[i]['exam']) )
                print('\n') 
            
        print('\n') 
        print('O numero de resultados SEM  exames laudados eh: {}'.format(count))   
        option = 7

    if option == 6: #pequisar por cpf
        request = requests.get('http://localhost:8000/scheduling//')
        dados = request.json()
        i = 0
        inputCpfSearch = int(input('Digite o cpf para pesquisa, só os numeros: \n'))
        
        for d  in dados:
            if dados[i]['cpf'] == inputCpfSearch:
                print('Segue as informacoes do registro com o cpf digitado: \n' )
                print('Nome: {}'.format(dados[i]['name']) )
                print('CPF: {}'.format(dados[i]['cpf']) )
                print('Data da consulta: {}'.format(dados[i]['date']) )
                print('Status Exames: {}'.format(dados[i]['exam']) )
                print('\n')
                if dados[i]['exam'] == 'Sem resultados de exames':
                    print('Esse paciente ainda nao possui laudo do exame cadastrado. \n' )
                else:
                    print('Esse paciente possui resultado do exame feito:\n' )
                    print('Resultado: {}'.format(dados[i]['description']) )
                    
            elif dados[i]['cpf'] != inputCpfSearch:
                i+=1
    
    if option == 8: #Laudar exame
        request = requests.get('http://localhost:8000/scheduling//')
        dados = request.json()
        i = 0
        inputCpfSearch = int(input('Digite o cpf para o qual voce vai laudar o exame dele: \n'))   
        
        for d  in dados:
            if dados[i]['cpf'] == inputCpfSearch:
                print('Segue as informacoes do registro com o cpf digitado: \n' )
                print('Nome: {}'.format(dados[i]['name']) )
                print('CPF: {}'.format(dados[i]['cpf']) )
                print('Data da consulta: {}'.format(dados[i]['date']) ) 
                inputDescription = input('Escreva o resultado do teste de COVID: \n')
                dadosExame = {
                    
                    "description": inputDescription
                }
            
                url = 'http://localhost:8000/scheduling//{}/'.format(dados[i]['id'])
                response = requests.patch(url=url,json=dadosExame)

                if response.status_code >= 200 and response.status_code <=299:
                    #sucesso em cadastrar usuario!
                    #print('Status Code', response.status_code)
                    print('########################################')
                    print('#SEU LAUDO FOI REALIZADO COM SUCESSO   #')
                    print('#                                      #')
                    print('########################################')
                    break
            
            else:
                i+=1

                    
        
       
        
       
        



    if option == 7:
        main()


if __name__ == '__main__':
    main()


