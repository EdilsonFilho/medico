import requests
import json

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
        dados = {
            "name": "Joao Claudio",
            "cpf": "001548745899",
            "date": "02/02/2020",
            "description": ""
        }
        url = 'http://localhost:8000/scheduling/create/'

        response = requests.post(url=url,json=dados)
        
        if response.status_code >= 200 and response.status_code <=299:
            #sucesso em cadastrar usuario
            print('Status Code', response.status_code)
            print('Reason', response.reason)
            print('Texto',response.text)
            print('Json',response.json())
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