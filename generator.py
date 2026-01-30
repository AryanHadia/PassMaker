# we generate password hear
import random

class Generator():
    def generate_hard(): # generate hard password
        hard = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ1234567890!@#$%^&*()" # exclude I, l, 1, 0
        password = "".join(random.choice(hard) for i in range(22)) # generate 12 character password
        return password

    def generate_medium(): # generate medium password
        medium = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()" # exclude I, l, 1, 0
        password = "".join(random.choice(medium) for i in range(12)) # generate 8 character password
        return password

    def generate_weak(): # generate weak password
        weak = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" # exclude I, l, 1, 0
        password = "".join(random.choice(weak) for i in range(6)) # generate 6 character password
        return password   

class advance_generatior(): # generate advance password
    def generate_advance(self , length , special_characters , numbers , uppercase_letters): # generate advance password
        advance = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()" # exclude I, l, 1, 0
        password = ""
        if special_characters: # if special characters is True
            password += random.choice("!@#$%^&*()")
        if numbers: # if numbers is True
            password += random.choice("1234567890")
        if uppercase_letters: # if uppercase letters is True
            password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        password += "".join(random.choice(advance) for i in range(length - len(password))) # generate remaining characters
        return password
    
    def improve_password(self , password , options): # improve password
        if options == "special_characters": # if special characters is True
            password += random.choice("!@#$%^&*()")
        if options == "numbers": # if numbers is True
            password += random.choice("1234567890")
        if options == "uppercase_letters": # if uppercase letters is True
            password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return password