class Computer:
    def __init__(self, cpu, ram, os, manu):
        self.cpu = cpu
        self.ram = ram
        self.os = os
        self.manu = manu

    def show_config(self):
        print('CPU : {}, \nRAM : {}, \nOS : {}, \nManufacturer : {}'.format(self.cpu, self.ram, self.os, self.manu))

    def compare_manu(self, other_computer):
        if self.manu == other_computer.manu:
            print('Both machines are manufactured by same company')
        else:
            print('Both machines are manufactured by diff company')

computer1 = Computer('i5 8th Gen', '8 GB', 'Windows 10 Enterprise Edition', 'Lenovo')

# Computer.show_config(computer1)
computer1.show_config()

computer2 = Computer('i7 9th Gen', '16 GB', 'Windows 10 Pro', 'Lenovo')
computer2.show_config()

computer1.compare_manu(computer2)