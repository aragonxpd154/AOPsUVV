class Fila:
    def __init__(self):
        self.itens = []
    
    # Função para adicionar um novo item a fila
    
    def enqueue(self, item):
        self.itens.append(item)
    
    def dequeue(self):
        return self.intens.pop(0)
    
    def inEmpty(self):
        return self.itens == []
    
    def size(self):
        return len(self.itens)
    
    # Instanciandno um objeto estacionamento que recebe a clasee Fila()
    
# Verificando se a fila está vazia ou não
print("\n")
    
estacionamento = Fila()
    
if Fila.inEmpty:
    print("Não há elementos na fila!!")
else:
    print("Há elementos na fila!!")
    
print("\n")

# Inserindo carros na fila do estacionamento

estacionamento.enqueue("Carro Azul")
estacionamento.enqueue("Carro Verde")
estacionamento.enqueue("Carro Vermelho")

print("Esses são os carros que estão na fila do estacionamento: \n" , estacionamento.itens)
print("\n")
