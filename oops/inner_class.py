class Computer:
    def __init__(self):
        self.name = "PC1"
        self.cpu = self.CPU()
        self.os = self.OS()
    class CPU:
        def __init__(self):
            self.cpu = "Intel i7"
    class OS:
        def __init__(self):
            self.os = "Windows"

comp = Computer()
print(f"Computer's name is {comp.name}, cpu is {comp.cpu.cpu} and operating system is {comp.os.os}")