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
    ###cadstro no sistema 
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
        
        url = 'http://localhost:8000/scheduling/create/'
        response = requests.post(url=url,json=dados)

        if response.status_code >= 200 and response.status_code <=299:
            #sucesso em cadastrar usuario!
            #print('Status Code', response.status_code)
            print('########################################')
            print('#SEU CADASTRO FOI REALIZADO COM SUCESSO#')
            print('#    CONTINUE A USAR O SISTEMA!!!      #')
            print('########################################')
            option = 7
            
        
        #caso nao tenha dado certo fazer o cadastro
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
        
    ###Login
    if option == 0:
        request = requests.get('http://localhost:8000/scheduling/')
        dados = request.json()
        print('Bem vindo ao SISCOVID')
        consultaNome = input('digite seu nome:  ')
        consultaSenha = getpass.getpass(prompt='Digite sua Senha: ', stream=None)
        i= 0
        for d  in dados:
            if dados[i]['name'] == consultaNome:
                if dados[i]['password'] == consultaSenha:
                    if dados[i]['categoryUser'] == 'paciente':
                        option = 8
                    elif dados[i]['categoryUser'] == 'medico':
                        option = 9
            else:
                i+=1
        

    
    if option == 4:
        request = requests.get('http://localhost:8000/scheduling/')
        dados = request.json()
        i = 0
        print('Dados dos pacientes com consultas realizadas\n')
        
        for i in range(len(dados)):
            print('Nome: {}'.format(dados[i]['name']) )
            print('CPF: {}'.format(dados[i]['cpf']) )
            print('Data da consulta: {}'.format(dados[i]['date']) )
            print('Status Exames: {}'.format(dados[i]['exam']) )
            print('\n') 
        print('\n')    
        option = 7

    if option == 8:
        print('Ola paciente\n')
    
    if option == 9:
        print('Ola medico\n')
        
       
        



    if option == 7:
        main()


if __name__ == '__main__':
    main()


