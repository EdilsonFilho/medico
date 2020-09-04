# -*- coding: utf-8 -*-
import requests
import json
import getpass 


print('########################################')
print('#   PAINEL DE CONTROLE PARA O MEDICO   #')
print('#    VISAO GERAL SISTEMA COVID         #')
print('# -----------------------------------  #')
print('#                                      #')
print('########################################')

def main():

    option = int(input('Ola medico, o que desejas fazer?\n 1.Listar completa dos pacientes\n 2.Sair\n 3.consultar resultado por CPF\n 4.Cadastrar resposta de exame\n'))
    #Inicio do Menu
    if option == 1:
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

    
    if option == 2:
        print('saindo')
        print('-------------------')
        

    if option == 3:
        request = requests.get('http://localhost:8000/scheduling/')
        dados = request.json()
        i = 0
        print('inciando consulta de resultado por CPF')
        print('-------------------')
        consultaCpf = int(input('digite o CPF para consulta:  '))
        
        for consultaCpf in dados:
            print(dados.value()) 
    
    if option == 4:
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
            #sucesso em cadastrar usuario
            print('Status Code', response.status_code)
            print('Cadastro criado com sucesso!')
            #print('Reason', response.reason)
            #print('Texto',response.text)
            #print('Json',response.json())
        else:
            #Erros
            print('Status Code', response.status_code)
            print('Reason', response.reason)
            print('Texto',response.text)
        
        option = 7



    if option == 7:
        main()


if __name__ == '__main__':
    main()