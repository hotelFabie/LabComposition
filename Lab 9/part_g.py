#Part G

#1
class CPU:
    def __init__(self, model : str):
        self.model = model

#2
class Computer:
    def __init__(self, brand : str, cpu : CPU):
        self.brand = brand
        self.cpu = cpu 

#3
cpu = CPU("AMD Ryzen Threadripper 9980X")
computer = Computer("Dell", cpu)

#4
print(computer.brand)
print(computer.cpu.model)

#5
#A computer is not only a CPU, but rather, literally and contextually appropriate, a composition of many things.
#While a CPU is the brain of the computer, it highly rarely exists alone. So, a computer HAS A CPU, like how it HAS A GPU, RAM, etc.

#6

