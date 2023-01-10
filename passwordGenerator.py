######################################################################################################
# Title: Password Generator For Brute Force Attack                                                   #
# Author: Tanvir Hossain Antu                                                                        #
# Github : https://github.com/Antu7      
# If you use the code give me the credit please                                                      #
######################################################################################################



import itertools

class PasswordGenerator:
    def __init__(self, possible_combination: int, combination_type: int):
        self.possible_combination = possible_combination
        self.combination_type = combination_type
        self.special = '!"#$%&\'()*+,-. /:;?@[]^_`{|}~'
        self.numeric = '0123456789'
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.get_carecter = ""
        
    def generate_get_carecter(self):
        if self.combination_type == 1:
            self.get_carecter = self.numeric + self.alphabet
        elif self.combination_type == 2:
            self.get_carecter = self.numeric
        elif self.combination_type == 3:
            self.get_carecter = self.alphabet
        elif self.combination_type == 4:
            self.get_carecter = self.special
        elif self.combination_type == 5:
            self.get_carecter = self.special + self.numeric
        elif self.combination_type == 6:
            self.get_carecter = self.special + self.numeric + self.alphabet
        else:
            raise ValueError("Invalid combination_type")

    def generate_password(self):
        for x in itertools.product(*([self.get_carecter] * self.possible_combination)):
            yield ''.join(x)

    def write_to_file(self):
        with open("password_list.txt", "w") as file:
            for i, password in enumerate(self.generate_password()):
                file.write(password + "\n")
                print(f"{i+1} possible combination: {password}")

possible_combination = int(input("How many password combinations do you want to create? Exp(3): "))
combination_type = int(input("Enter combination type (1-6): "))
generator = PasswordGenerator(possible_combination, combination_type)
generator.generate_get_carecter()
generator.write_to_file()
