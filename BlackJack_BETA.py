import random
import time
import sys

class Blackjack_Karten ():
    
    def __init__(self):
        self.karten = {"2er Karte":2,
                  "3er Karte":3,
                  "4er Karte":4,
                  "5er Karte":5,
                  "6er Karte":6,
                  "7ner Karte":7,
                  "8er Karte":8,
                  "9er Karte":9,
                  "Bube":10,
                  "Dame":10,
                  "König":10,
                  "Ass":11}
        
        self.kartenliste = list(self.karten)
        self.cards_user = []
        self.cards_bank = []
        self.bank_points = 0
        self.user_points = 0
        self.welcome()
    
    def reset (self):
        self.user_points = 0
        self.cards_user = []
        self.bank_points = 0
        self.bank_cards = []
        print("Das Spiel wird beendet...")
        time.sleep(3)
        sys.exit()    
    
    def proof_winner (self,user_points,bank_points):
        if self.user_points > self.bank_points:
            print("Du hast gewonnennach Punkten!")
            self.reset()
        elif self.user_points < self.bank_points:
            print("Die Bank hat gewonnen nacht Punkten!")
            self.reset()
        elif self.user_points == self.bank_points:
            print("Es ist unentschieden!")
            self.reset()
        
    def proof_user (self,user_points):
        
        if self.user_points == 21:
            print("Du hast Gewonnen!")
            self.reset()
        elif self.user_points > 21:
            print ("Du hast verloren!")
            self.reset()
        elif self.user_points < 21:
            print("Deine Punkte sind " + str(self.user_points))
            
    def xtra_card (self):
        
        user_card = random.choice(self.kartenliste)
        self.cards_user.append(user_card)
        self.user_points += self.karten[user_card]
        
        time.sleep(1)
        print("Dein Karten sind " + str(self.cards_user)
              + " und deine Punktzahl ist "
              + str(self.user_points))
        time.sleep(1)
        
        self.proof_user(self.user_points)
        
        print("Willst du eine Karte oder möchtest du dein")
        print("Blatt behalten? Drücke 'weiter' für eine extra Karte")
        time.sleep(1)
        print("oder 'halten' um das Blatt zu halten!")
        
        user_input = input("Deine Eingabe :")
        
        if user_input.lower() == "weiter":
            self.proof_user(self.user_points)
            self.xtra_card()
        elif user_input.lower() == "halten":
            self.proof_user(self.user_points)
            self.give_bank()
        
    def give_bank (self):
        time.sleep(1)
        
        bank_cards = random.choices (self.kartenliste,k=2)
        
        self.cards_bank.append(bank_cards)
        
        for card in bank_cards:
            self.bank_points += self.karten[card]
        
        while self.bank_points <= 17:
            xtra_card = random.choice(self.kartenliste)
            self.bank_points += self.karten[xtra_card]
        if self.bank_points == 21:
            print("Die Bank hat gewonnen!")
            self.reset()
        elif self.bank_points > 21:
            print("Die Bank hat verloren! Mit " + str(self.bank_points)
                  + " Punkten!")
            self.reset()
        elif self.bank_points < 21:
            print("Die Bank bleibt stehen bei "
                  + str(self.bank_points) + " Punkten!")
            self.proof_winner(self.user_points,self.bank_points)   
        
    def give_cards (self):
        user_cards = random.choices(self.kartenliste,k=2)
        self.cards_user.extend(user_cards)
        
        for card in user_cards:
            self.user_points += self.karten[card]
            
        time.sleep(1)
        while self.user_points < 17:
            print("Deine Karten sind " + str(user_cards) 
                  + " mit einer Punktzahl von "
                  + str(self.user_points))
            print("Willst du noch eine Karte oder möchtest du dein")
            print("Blatt behalten? Drücke 'weiter' für eine extra Karte")
            time.sleep(1)
            print("oder 'halten' um das Blatt zu halten!")
            time.sleep(1)
            
            user_input = input("Deine Eingabe : ")
            
            time.sleep(1)
            
            if user_input.lower() == "weiter":
                self.xtra_card()
                break                
            elif user_input.lower() == "halten":
                self.give_bank ()
            else:
                print("Falsche Eingabe !")
                continue
                
 
    def welcome (self):
                
            print("Willkommen bei deinem Blackjack-Spiel!")
            time.sleep(1)
            print("Tippe 'spielen' um mit dem Spiel anzufangen!")
            print("oder Tippe 'beenden' um das Spiel zu beenden.")
            time.sleep(1)
        
            user_input = input("Ihre Eingabe : ")
            
            time.sleep(1)
            
            if user_input.lower() == "spielen":
                self.give_cards()
                
            elif user_input.lower() == "beenden":
                self.reset()
            
            else:
                print("Falsche Eingabe!")
                time.sleep(1)
                print("Das Spiel startet neu...")
                time.sleep(1)
                self.welcome ()
                                    
 
    
bj_cards = Blackjack_Karten()   



              
        
        
        










    