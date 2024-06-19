import time, os
os.system("cls")
os.system("color 3")
print(""" Bem-vindo à 
 ▄█   ▄█          ▄█    █▄       ▄████████        ▄▄▄▄███▄▄▄▄      ▄████████  ▄█       ███    █▄   ▄████████    ▄████████ 
███  ███         ███    ███     ███    ███      ▄██▀▀▀███▀▀▀██▄   ███    ███ ███       ███    ███ ███    ███   ███    ███ 
███▌ ███         ███    ███     ███    ███      ███   ███   ███   ███    ███ ███       ███    ███ ███    █▀    ███    ███ 
███▌ ███        ▄███▄▄▄▄███▄▄   ███    ███      ███   ███   ███   ███    ███ ███       ███    ███ ███          ███    ███ 
███▌ ███       ▀▀███▀▀▀▀███▀  ▀███████████      ███   ███   ███ ▀███████████ ███       ███    ███ ███        ▀███████████ 
███  ███         ███    ███     ███    ███      ███   ███   ███   ███    ███ ███       ███    ███ ███    █▄    ███    ███ 
███  ███▌    ▄   ███    ███     ███    ███      ███   ███   ███   ███    ███ ███▌    ▄ ███    ███ ███    ███   ███    ███ 
█▀   █████▄▄██   ███    █▀      ███    █▀        ▀█   ███   █▀    ███    █▀  █████▄▄██ ████████▀  ████████▀    ███    █▀  
                                                       """)
print('''Você é um explorador corajoso em busca de tesouros lendários na 
misteriosa Ilha Maluca.
     Rumores dizem que um grande tesouro está 
escondido em algum lugar na ilha, mas para encontrá-lo, você 
precisa decifrar uma série de enigmas.
Ao chegar na ilha, você se depara com uma placa estranha com 
inscrições antigas.
       As inscrições dizem o seguinte:
"Para desbloquear o tesouro escondido, você deve provar sua destreza. Resolva os 
desafios a seguir e siga as instruções para encontrar o caminho certo.''')
time.sleep(10)
os.system("cls")
os.system("color 2")
print('''Desafio 1#################################### O Guardião da Porta
                                                                               
                                                                                         
                   █                                                  █                  
                     █████████████████████████████████████████████████                   
                                                                                         
                       █       █         ██     ██         █                             
                       █         █ █  █             █  █ ██        █                     
                       █ █   ██   █                █    █ █ ██     █                     
                       █       █      ██████████  ████    █ █      █                     
                       █  █   █    ████ ███████████      █  █ ██   █                     
                       █         ██  █████           ██        ███ █                     
                       █   █   ███ ███   ██████████             ██                       
                       █       █ ██  ████████ █ ██████   █   █   ███                     
                       █  █   █ ██ █████  █ █ █ █      █  █      ███                     
                             ████ ████████████████      █ █       ██                     
                   █         ███ ██ ██████       █       █ █ █  █ █  ███                 
                    ██ █       ███ ██ ██           █     █ █       ███                   
                       █  █ █  █   ████             █      █  █ █  ███                   
                     ███  █ █  ████████                 ████    █ ████                   
                        █    ███  █████             █  █ █  █    ███ █                   
                     ████████████ ██ ██             █  █ █████████████                   
                             ██████████                  █       █████                   
                             ███ ██████                  █       █████                   
                              ██ ██████                  █       █████                   
                              █████████                  █       █████                   
               █    █   █     ██  █████                  █        ██████████             
             █     ██         █████████                  █        ███████████            
           █      ███         ██ ██████                  █       ███████████████         
           █ ████████         ████████                   █       ███████████████         
             ████             █████████                  █        ████    ████           
                             ███ ██████            █     █  █    █████ █ █               
                   █    █     █████████  █          █    █  █     ████ █                 
                    █   ████████████████                 █  ██████████     ██            
                   ██  █       ██  ████████       ██     ███      ████   ███             
                   ██           █  ███████         █ █              ██   ███             
             █     ██           ██               █      ██           ██  ████            
          █         █████████████                        █ ███████████████  █████        
                                █                        █            ███████████        
       ██████████████  █  █████ █                    ██  ████████ ██████     ███████     
                             ███                       █ ██                              
    
Você se depara com uma porta enorme guardada por um gigante adormecido. Para passar 
pela porta e continuar sua jornada, você precisa responder a seguinte questão:''')
time.sleep(5)
os.system("cls")
print(''' "Quantos cocos o macaco tem se eu pegar metade dos cocos que ele tem, mais dois cocos, 
e depois subtrair três cocos? ''')
desafio1 = float(input("Insira quantos cocos o macaco tinha: "))#ou int
d1 = float(input("Insira quantos cocos o macaco tem/ficou: "))
d2 = ((desafio1/2)-1)
if d1 == d2:
    print("Aeeh,parabéns! Passagem permitida!")
else:
    print("Você não conseguiu e foi atacado pelo gigante ...")
    quit()
#########################################################################
time.sleep(5)
os.system("cls")
print('''Desafio 2:
╔═╗  ╦  ┌─┐┌┐ ┌─┐┬─┐┬┌┐┌┌┬┐┌─┐         
║ ║  ║  ├─┤├┴┐├┤ ├┬┘││││ │ │ │         
╚═╝  ╩═╝┴ ┴└─┘└─┘┴└─┴┘└┘ ┴ └─┘         
┌┬┐┌─┐┌─┐  ╔═╗┬─┐┌─┐┌─┐┌─┐┌┬┐┬┬  ┌─┐┌─┐
 │││ │└─┐  ║  ├┬┘│ ││  │ │ ││││  │ │└─┐
─┴┘└─┘└─┘  ╚═╝┴└─└─┘└─┘└─┘─┴┘┴┴─┘└─┘└─┘
      

                                                                                   
                           ░▓▓███▓▓▒                                                                
                       ░▓██████▓▒▒▒▒▓▓▓░                                                            
                     ██████▒                                                                        
                  ▒▒██████                                                                          
                   ███████                                                                          
                   ████████                                                                         
                  ▒██████████▒                                                                      
                    ████████████▓░                                                                  
                    ▒█████████████████▒░                                                            
                      ▒████████████████████████████▓▒░                                              
                        ▒██████████████████████████████████▓░                                       
                          ▒█████████████████████████████████████▓░                                  
                              ▒▓████████████████████████████████████▒                               
                                  ▒████████████████████████████████████▒                            
                                     ▒███████████████████████████████████▒                          
                                       ░▓██████████████████████████████████░                        
                                         ▒██████████████████████████████████░                       
                                          ▒██████████████████████████████████░                      
                                          ▓██████████████████████████████████▓                      
                                  ▒███████████████▒▒██████████████████████████░                     
                                 ▓████████████████▓ ▓█████████████████████████▒                     
                                █████████████████▓ ░███████████████████████████                     
                               ▓███████████░       ████████████████████████████                     
                              ▒█████████████░    ░████████████████████████████▓                     
                              ░  ░██▒▒████▒▓▓   ▓█████████████████████████████▒                     
                                  ▒     █▒  ░  ▓██████████████████████████████░                     
                                               ███████████████████████████████                      
             ░▓███▓░                           ███████▓▒█████████████████████▒                      
           ▓██████████▓░      ░░▒▒▒░   ░▓▓███▓▒░░▒▒░░░▓█████████████████████▓                       
           ▒██████████████████████████████████████▓▓████████████████████▓▒░░                        
              ▒████████████████████████████████████████████████████████████▓░                       
                 ░████████████████████████████████████████████████████████████                      
                  ░░  ▒░  █▒▒█████████████████████████████████████████████████▓                     
                             ▒▒▒█████████████████████████████████ ▒████████████░                    
                                            ▓██████████████████▓       ▓███████░                    
                          ░                   ▒██████████████▓         ░███████▒                    
                       ▒█░             ▒██████████████████▓            ▓████████░                   
                    ░██▒           █░▓██████████████▓░              ▒████████████▓                  
                  ▓███░     ▒█▒███████████████▓▒                   ██████████████████               
                ░████▒ ░▓█▓█████████████▓░                         ░  █████████▓  ░█▓               
                 ████████████████▓▒░                                  ▓▒     ░▒                     
                  ░▓▓██▓▓▓▒░                                                                
       
Após passar pela porta, você entra em um labirinto infestado de 
crocodilos famintos. Para escapar deles, você precisa resolver o seguinte 
problema:''')
time.sleep(5)
desafio2 = int(input(''' "Se eu tenho uma corda de 12 metros e preciso atravessar um rio de 7 metros de largura, 
quantos metros de corda a mais eu tenho para amarrar nas árvores e atravessar com 
segurança?''')) #usar print vazio
d3 =int(5) # ou 12-7
if desafio2 == 5:
    print('Você conseguiu passar pelos crocodilos e não perdeu sua mochila. Parabéns!')
else:
    print('E morreu... Caiu no rio com a mochila.')
    quit()
time.sleep(5)
os.system("cls")
print('''

╔═╗  ╔═╗┌┐┌┬┌─┐┌┬┐┌─┐  ╔═╗┬┌┐┌┌─┐┬  
║ ║  ║╣ │││││ ┬│││├─┤  ╠╣ ││││├─┤│  
╚═╝  ╚═╝┘└┘┴└─┘┴ ┴┴ ┴  ╚  ┴┘└┘┴ ┴┴─┘
                                                                                      
                                                            ████                      
                                                            ██████                    
                                                            ███████                   
                                                            ███████                   
                                                            ███████                   
                   ██████████████  █████████████████████████████ ██                   
                ██                                               ██                   
               ██                                                ██                   
               ██                                      ███ ██    ██                   
               ██             █████                      ███     ██                   
               ████                 ████████           ██  ███   ██                   
               ███████                                           ██                   
               ███████      ██                                   ██                   
               ███████     ████                         ██       ██                   
               ███████    ██  ██  ██                             ██                   
               ███████   ██    ███ ██             ██             ██                   
               ███████   ████████   ██  █  ██  ██                ██                   
               ███████        █████████                          ██                   
               ███████                                     ████████                   
               ███████                                          ██                    
               ███████████████████████████████  ████████████████                      
               ███████                                                                
               ███████                                                                
               ███████                                                                
                ██████                                                                
                 █████                                                                
                                                                                      
                                                                                   
Finalmente, você chega à câmara do tesouro, mas para abri-la, você precisa resolver um 
enigma final:
''')
time.sleep(5)
os.system("cls")
tesouros = int(input('''
DESAFIO 3 #########
Se o número de tesouros enterrados na ilha é igual ao dobro do número de palmeiras, 
e o número de palmeiras é igual a três vezes o número de periquitos na ilha, e o número 
total de periquitos é 42, quantos tesouros tem na ilha?'''))
if tesouros == 252: # ou palmeiras = 42*3 , tesouros = palmeiras*2 ou 252
    print('''Parabéns! Você resolveu o enigma e conseguiu encontrar o tesouro
    ___________  
   '._==_==_=_.' 
   .-\:      /-. 
  | (|:.     |) |
   '-|:.     |-' 
     \::.    /   
      '::. .'    
        ) (      
      _.' '._    
     `"""""""`''')
else: 
    print('Não conseguiu. Você ficou preso do lado de fora da câmara :( ' )
    quit()










