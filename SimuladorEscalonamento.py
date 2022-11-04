arquivo = open('processos.in', 'r')

# Vetor para ler cada liha do arquivo
aux = []  

# Lê linha por linha do arquivo e armazena no vetor aux
while True:
    line = arquivo.readline()
    if not line:
        break
    aux.append(line)
arquivo.close()

#Vetor de processos para armazenar as informações dos processos
processos = [] 

#Método para separar cada processo
for x in aux:
    processos.append(x.split())
    
    
def SJF()->list(processos):
    print("SJF with preemption")
    
def Priority()->list(processos):
    print("Priority without preemption")
    
    Ut = 0
    copiaProcessos = processos
    queueProntos = []
    queueEspera = []
    while Ut < 5:#len(processos) != 0:
        print("Tempo corrente: {0}".format(Ut))
        for x in copiaProcessos:
            if Ut == int(x[0]):
                queueProntos.append(x)
        Ut += 1
    print(queueProntos)
    print(copiaProcessos)
    
                
                
    
    
    
print("="*35+"\nSIMULADOR DE ESCALONAMENTO\n\n"
      +"(1) -> SJF with preemption\n(2) -> Priority without preemption\n"+"="*35)
response = int(input("Digite sua opção: "))
print("="*35+"\n")


if response == 1:
    SJF()
elif response == 2:
    Priority()
else:
    print('Opção Inválida!')