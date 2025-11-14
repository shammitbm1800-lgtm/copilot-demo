from helpers import send_message

def greet_user(name):
    send_message("Hello", name)

def farewell_user(name):
    send_message("Goodbye", name)

def congratulate_user(name):
    send_message("Congratulations", name)   
