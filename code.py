import random
import time
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.__idade = idade
        self.__profissao = "Desempregado"
        self.__dinheiro = 0
        self.__energia = 20
        self.__saude = 100

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self,value):
        self.__idade = value


    @property
    def dinheiro(self):
        return self.__dinheiro
    @dinheiro.setter
    def dinheiro(self,value):
        self.__dinheiro = value  
    
    
    @property
    def profissao(self):
        return self.__profissao
    
    @profissao.setter
    def profissao(self,value):
        self.__profissao = value
    

    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self,value):
         self.__energia = value

    
    
    def demitir(self):
        self.profissao = "Desempregado"
    def procurarEmprego(self,horasProcurando):
        energia = self.energia
        for i in range(horasProcurando):
            self.idade += 0.1
            if(energia > 0):
                self.energia -= 1
                prob = random.randint(0, 9)
                if(prob == 5):
                    prob1 = random.randint(1, 6)
                    if(prob1 == 1):
                        self.profissao = "Lixeiro" #salário de R$12,00
                    elif(prob1 == 2):
                        self.profissao = "Mendigo"#salário de R$2,00
                    elif (prob==3):
                        self.profissao = "Pedreiro" #salário de R$20,00 
                    elif (prob==4):
                        self.profissao = "Motoboy" #salário de R$100,00
                    elif (prob==5):
                        self.profissao = "Catador de latinhas" #salário de R$40,00
                    elif (prob==6):
                        self.profissao = "Uber" #Criar probalidade de ele ser roubado - Salário de 200,00 
                
                    print(self.profissao)
                    break
                else:
                    print("Procurando...")
                    time.sleep(2)
        else:
            print("Sua energia acabou, vai dormir fi.")
    def dormir(self,horasDormindo):
        for i in range(horasDormindo):
            self.energia += 1
            self.idade += 0.1
            print("Dormindo e envelhecendo...")
            energia = self.energia
            idade = self.idade
            print(f"Sua energia: {energia}")
            print(f"Sua idade: %.2f" % (idade))
            time.sleep(2)
    def trabalhar(self,horasTrabalhadas):
        trabalho = self.profissao
        energia = self.energia
        if(trabalho == "Lixeiro"):
            if(energia > 10):
                for i in range(horasTrabalhadas):
                    time.sleep += 1
                    print("Correndo e colocando lixo no caminhão!")
                    time.sleep += 5
                    self.idade += 0.8
                    self.energia -= 5

                    prob = random.randint(0, 9)
                    if(prob > 5):
                        self.dinheiro += 30

                        print("Voce achou um item valioso no lixo +30R$")
                        time.sleep(5)
                        self.dinheiro += 20
                        print("+20R$ pela hora trabalhada")
                        time.sleep(1)
                        dinheiro = self.dinheiro
                        print(f"Dinheiro atual: {dinheiro} ")
                    else:
                        self.dinheiro += 20
                        print("+20R$ pela hora trabalhada")
                        dinheiro = self.dinheiro
                        print(f"Dinheiro atual: {dinheiro} ")
                        
            else:
                print("Você está cansado, va recuperar energia.")

                        
        if(trabalho=="Mendigo"):
            if(energia > 10):
                for i in range(horasTrabalhadas):
                    time.sleep(1)
                    print("Mendigando...")
                    time.sleep(4)
                    self.idade += 0.1
                    self.energia -= 1
                    prob = random.randint(0, 9)
                    if(prob > 5):
                        self.dinheiro += 2
                        dinheiro = self.dinheiro
                        print("Achei uma moeda +2Reais")
                        time.sleep(1)
                        print(f"Dinheiro atual: {dinheiro} ")
                        
                    else:
                        time.sleep(1)
                        print("Nada encontrado")
            else:
                print("Você está cansado, va recuperar energia.")
        

        if(trabalho == "Pedreiro"):
           if(energia > 10):
                for i in range(horasTrabalhadas):
                    time.sleep(1)
                    atEnergia = self.energia
                    print(f"\nEnergia: {atEnergia}")
                    print("Construindo...")
                    time.sleep(5)
                    self.idade += 0.1
                    self.energia -= 4
                    prob = random.randint(0, 9)
                    if(prob > 3):
                        self.dinheiro += 40
                        dinheiro = self.dinheiro
                        print("O patrão curtiu a construção +40R$")
                        time.sleep(1)
                        print(f"Dinheiro atual: {dinheiro} ")
                        
                    else:
                        time.sleep(1)
                        print("A construção ficou ruim \n-10R$ Pelo material desperdicado.\n")
                        self.dinheiro -= 10
                        dinheiro = self.dinheiro
                        time.sleep(1)
                        print(f"Dinheiro atual: {dinheiro} ")

                else:
                    print("Você está cansado, va recuperar energia.")

        if(trabalho == "Motoboy"):
            if(energia > 10):
                for i in range(horasTrabalhadas):
                    self.idade += 0.1
                    self.energia -= 2
                    prob = random.randint(0, 9)
                    prob1 = random.randint(0, 50)
                    if(prob1 > 45):
                        self.demitir()
                    if(prob > 5):
                        self.dinheiro += 100
                        print("Trabalhando")
            else:
                print("Você está cansado, va recuperar energia.")


        if(trabalho == "Catador de latinhas"):
            if(energia > 10):
                for i in range(horasTrabalhadas):
                    time.sleep(1)
                    print("Catando latinhas...")
                    time.sleep(8)
                    self.idade += 0.1
                    self.energia -= 4
                    prob = random.randint(0, 50)
                    prob1 = random.uniform(0.30, 0.60)
                    print(f"Você achou {prob} latinhas e conseguiu vendelas por {round(prob1,2)}")
                    rendDinheiro = prob*prob1
                    self.dinheiro += rendDinheiro
                    dinheiro = self.dinheiro
                    time.sleep(1)
                    print(f"Dinheiro atual: {round(dinheiro,2)} ")
                        
                else:
                    time.sleep(1)
                    print("Nada encontrado")
            else:
                print("Você está cansado, va recuperar energia.")


        if(trabalho == "Uber"):
           if(energia > 10):
                for i in range(horasTrabalhadas):
                    time.sleep(1)
                    print("Fazendo corrida...")
                    time.sleep(8)
                    self.idade += 0.4
                    self.energia -= 1
                    prob = random.randint(0, 9)
                    if(prob > 8):
                        self.dinheiro -= (random.randint(20, 30))
                        dinheiro = self.dinheiro
                        print("Voce foi assaltado, levaram sua carteira.")
                        time.sleep(1)
                        print(f"Dinheiro atual: {dinheiro} ")
                        
                    else:
                        
                        time.sleep(1)
                        money = random.randint(5, 30)
                        self.dinheiro += money
                        dinheiro = self.dinheiro
                        print(f"Corrida finalizada!, +{money}R$")
                        print(f'Dinheiro atual: {dinheiro} ')
                        
                else:
                    print("Você está cansado, va recuperar energia.")

                    
               
                
    
#https://colab.research.google.com/drive/1KxXxKX1OjdV9QPWNToyBWqFQXIFVyYjj?usp=sharing
