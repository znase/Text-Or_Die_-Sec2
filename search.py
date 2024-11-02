import pandas as pd
from rapidfuzz import process
import random
import pygame
import main

df = pd.read_excel(r'data\dictionary.xlsx', sheet_name='dictionary')
letters = "abcdefghijklmnopqrstuvwxyz"

class problemBox() :
    def __init__() :



    def random_problem(self):
        selected_letters = random.sample(letters, 2)
        #print(f"input the word that is include {selected_letters[0]} and {selected_letters[1]}")
        
        BLACK = (0, 0, 0)

        self.text_surface = main.self.font.render(f"input the word that is include {selected_letters[0]} and {selected_letters[1]}", True, BLACK)
            
        self.text_rect = self.text_surface.get_rect(center=(main.width // 2, main.height // 2))

        main.window.blit(self.text_surface, self.text_rect)

        main.pg.display.update()

        return selected_letters 

def check_text(problem,text) :
    text = text.lower()
    check_text = process.extractOne( text , df.key)
    #print(check_text)

    if check_text[1] == 100.00 and problem[0] in text and problem[1] in text:
        print("Correct")

    else :
        print("Incorrect")

def start() :
    problem = random_problem()

    text = input()

    check_text(problem,text)

start()