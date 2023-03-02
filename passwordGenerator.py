import itertools
import threading

class PasswordGenerator:
    def __init__(self, possible_combination: int, combination_type: int, num_threads: int):
        self.possible_combination = possible_combination
        self.combination_type = combination_type
        self.special = '!"#$%&\'()*+,-. /:;?@[]^_`{|}~'
        self.numeric = '0123456789'
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.get_carecter = ""
        self.num_threads = num_threads
        
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

    def generate_password(self, start: int, end: int, output):
        for x in itertools.product(*([self.get_carecter] * self.possible_combination))[start:end]:
            output.append(''.join(x))

    def write_to_file(self):
        with open("password_list.txt", "w") as file:
            for password in self.generate_password():
                file.write(password + "\n")
                print(f"Possible combination: {password}")

    def generate_password_thread(self, thread_id, output):
        start = thread_id * self.possible_combination // self.num_threads
        end = (thread_id + 1) * self.possible_combination // self.num_threads
        passwords = []
        self.generate_password(start, end, passwords)
        output += passwords

    def generate_passwords(self):
        self.generate_get_carecter()
        threads = []
        output = []
        for i in range(self.num_threads):
            threads.append(threading.Thread(target=self.generate_password_thread, args=(i, output)))
            threads[i].start()

        for i in range(self.num_threads):
            threads[i].join()

        with open("password_list.txt", "w") as file:
            for password in output:
                file.write(password + "\n")
                print(f"Possible combination: {password}")

possible_combination = int(input("How many password combinations do you want to create? Exp(3): "))
combination_type = int(input("Enter combination type (1-6): "))
num_threads = int(input("How many threads to use? "))
generator = PasswordGenerator(possible_combination, combination_type, num_threads)
generator.generate_passwords()
