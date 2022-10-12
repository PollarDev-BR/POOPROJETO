import random
import time
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.__idade = idade
        self.__profissao = "Pedreiro"
        self.__dinheiro = 0
        self.__energia = 20
        self.__saude = 100

    def getIdade(self):
        return self.__idade
        
    def getDinheiro(self):
        return self.__dinheiro

    def getProfissao(self):
        return self.__profissao
        
    def getEnergia(self):
        return self.__energia
        
    def setIdade(self,value):
        self.__idade += value
        
    def setProfissao(self,value):
        self.__profissao = value
    
    def setEnergia(self,value):
         self.__energia += value

    def setDinheiro(self,value):
        self.__dinheiro += value
    
    def demitir(self):
        self.setProfissao = "Desempregado"
    def procurarEmprego(self,horasProcurando):
        energia = self.getEnergia()
        for i in range(horasProcurando):
            self.setIdade(0.1)
            if(energia > 0):
                self.setEnergia(-1)
                prob = random.randint(0, 9)
                if(prob == 5):
                    prob1 = random.randint(1, 6)
                    if(prob1 == 1):
                        self.setProfissao("Lixeiro") #salário de R$12,00
                    elif(prob1 == 2):
                        self.setProfissao("Mendigo") #salário de R$2,00
                    elif (prob==3):
                        self.setProfissao("Pedreiro") #salário de R$20,00 
                    elif (prob==4):
                        self.setProfissao("Motoboy") #salário de R$100,00
                    elif (prob==5):
                        self.setProfissao("Catador de latinhas") #salário de R$40,00
                    elif (prob==6):
                        self.setProfissao("Uber") #Criar probalidade de ele ser roubado - Salário de 200,00 
                
                    print(self.getProfissao())
                    break
                else:
                    print("Procurando...")
        else:
            print("Sua energia acabou, vai dormir fi.")
    def dormir(self,horasDormindo):
        for i in range(horasDormindo):
            self.setEnergia(1)
            self.setIdade(0.1)
            print("Dormindo e envelhecendo...")
            energia = self.getEnergia()
            idade = self.getIdade()
            print(f"Sua energia: {energia}")
            print(f"Sua idade: %.2f" % (idade))
    def trabalhar(self,horasTrabalhadas):
        trabalho = self.getProfissao()
        energia = self.getEnergia()
        if(trabalho == "Lixeiro"):
            if(energia > 10):
                for i in range(horasTrabalhadas):
                    self.setIdade(0.1)
                    self.setEnergia(-2)
                    prob = random.randint(0, 9)
                    prob1 = random.randint(0, 50)
                    if(prob1 > 45):
                        self.demitir()
                    if(prob > 5):
                        self.setDinheiro(100)
                        print("Trabalhando")
            else:
                print("Você está cansado, va recuperar energia.")

                        
        if(trabalho=="Mendigo"):
            if(energia > 10):
                for i in range(horasTrabalhadas):
                    time.sleep(1)
                    print("Mendigando...")
                    time.sleep(3)
                    self.setIdade(0.1)
                    self.setEnergia(-2)
                    prob = random.randint(0, 9)
                    if(prob > 5):
                        self.setDinheiro(2)
                        dinheiro = self.getDinheiro()
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
                    atEnergia = self.getEnergia()
                    print(f"\nEnergia: {atEnergia}")
                    print("Construindo...")
                    time.sleep(5)
                    self.setIdade(0.1)
                    self.setEnergia(-4)
                    prob = random.randint(0, 9)
                    if(prob > 3):
                        self.setDinheiro(40)
                        dinheiro = self.getDinheiro()
                        print("O patrão curtiu a construção +40R$")
                        time.sleep(1)
                        print(f"Dinheiro atual: {dinheiro} ")
                        
                    else:
                        time.sleep(1)
                        print("A construção ficou ruim \n-10R$ Pelo material desperdicado.\n")
                        self.setDinheiro(-10)
                        dinheiro = self.getDinheiro()
                        time.sleep(1)
                        print(f"Dinheiro atual: {dinheiro} ")

                else:
                    print("Você está cansado, va recuperar energia.")

        if(trabalho == "Motoboy"):
            if(energia > 10):
                for i in range(horasTrabalhadas):
                    self.setIdade(0.1)
                    self.setEnergia(-2)
                    prob = random.randint(0, 9)
                    prob1 = random.randint(0, 50)
                    if(prob1 > 45):
                        self.demitir()
                    if(prob > 5):
                        self.setDinheiro(100)
                        print("Trabalhando")
            else:
                print("Você está cansado, va recuperar energia.")


        if(trabalho == "Catador de latinhas"):
            if(energia > 10):
                for i in range(horasTrabalhadas):
                    time.sleep(1)
                    print("Catando latinhas...")
                    time.sleep(8)
                    self.setIdade(0.1)
                    self.setEnergia(-4)
                    prob = random.randint(0, 50)
                    prob1 = random.rand(0.3,0.8)
                    print(f"Você achou {prob} latinhas")
                        self.setDinheiro(2)
                        dinheiro = self.getDinheiro()
                        print("Achei uma moeda +2Reais")
                        time.sleep(1)
                        print(f"Dinheiro atual: {dinheiro} ")
                        
                    else:
                        time.sleep(1)
                        print("Nada encontrado")
            else:
                print("Você está cansado, va recuperar energia.")


        if(trabalho == "Uber"):
            if(energia > 10):
                for i in range(horasTrabalhadas):
                    self.setIdade(0.1)
                    self.setEnergia(-2)
                    prob = random.randint(0, 9)
                    prob1 = random.randint(0, 50)
                    if(prob1 > 45):
                        self.demitir()
                    if(prob > 5):
                        self.setDinheiro(100)
                        print("Trabalhando")
            else:
                print("Você está cansado, va recuperar energia.")

                    
               
                
    
joao = Pessoa("Joao",18)
joao.trabalhar(5)
