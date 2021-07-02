"""
This Expert System can tell your cat's type based on some rules, the system takes user's requests
and then perform some magic/matching to find out.

engine.run() : runs the engine in real time.
engine.declare() : passes requests to the engine aka adds a fact to the engine.
engine.reset() : resets the engine.

more info : https://experta.readthedocs.io/en/latest/thebasics.html

"""
from experta import *


class Cat(Fact):
    """Meow"""
    pass


cat_types = [
    "Maine Coon" ,
    "Persia Himalya" ,
    "Persia Peaknose",
    "Exotic Shorthair",
    "Russian Blue",
    "Anggora" ,
    "Siamese" ,
    "Scotishfold",
    "Sphynx" 
]

class CatEngine(KnowledgeEngine):

    @Rule(AND( Cat(body=("big")), Cat(hair="long"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="wide"),  Cat(leg="medium"),  Cat(nose="pointed") ))  
    def maine_coon(self):
        print(cat_types[0])
         


    @Rule(AND( Cat(body=("big")), Cat(hair="long"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="wide"),  Cat(leg="medium"),  Cat(nose="flat") ))  
    def persia_himalya(self):
        print(cat_types[1])
         

    @Rule(AND( Cat(body=("big")), Cat(hair="long"),   Cat(eye="sharp"),   Cat(neck="short"),  Cat(earlobe="small"),  Cat(leg="short"),  Cat(nose="flat") ))  
    def persia_peaknose(self):
        print(cat_types[2])
         


    @Rule(AND( Cat(body=("big")), Cat(hair="long"),   Cat(eye="round"),   Cat(neck="short"),  Cat(earlobe="small"),  Cat(leg="short"),  Cat(nose="flat") ))  
    def exotic_shorthair(self):
        print(cat_types[3])
         

    @Rule(AND( Cat(body=("medium")), Cat(hair="short"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="medium"),  Cat(leg="medium"),  Cat(nose="flat") ))  
    def russian_blue(self):
        print(cat_types[4])
         

    @Rule(AND( Cat(body=("medium")), Cat(hair="long"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="wide"),  Cat(leg="medium"),  Cat(nose="pointed") ))  
    def anggora(self):
        print(cat_types[5])
         

    @Rule(AND( Cat(body=("medium")), Cat(hair="short"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="medium"),  Cat(leg="medium"),  Cat(nose="pointed") ))  
    def siamese(self):
        print(cat_types[6])
         

    @Rule(AND( Cat(body=("medium")), Cat(hair="short"),   Cat(eye="round"),   Cat(neck="short"),  Cat(earlobe="small"),  Cat(leg="medium"),  Cat(nose="flat") ))  
    def scotishfold(self):
        print(cat_types[7])
         

    @Rule(AND( Cat(body=("medium")), Cat(hair="unavailable"),   Cat(eye="sharp"),   Cat(neck="medium"),  Cat(earlobe="wide"),  Cat(leg="medium"),  Cat(nose="pointed") ))  
    def sphynx(self):
        print(cat_types[8])
         


def get_user_input(req):
    """Avoid dups by taking user's requests in a sep function"""
    
    return input(req).strip().lower()


def main_loop():
    """Taking Input from User"""
    
    print("Descibe Your Cat ...")

    body = get_user_input("Big or Meduim body ? ")
    hair = get_user_input("Long or Short or no hair ? ")
    eye = get_user_input("Sharp or Round eyes ? ")
    neck = get_user_input("Short or Meduim neck ? ")
    earlobe = get_user_input("Wide or Meduim or Small earlobe ? ")
    leg = get_user_input("Short or Meduim legs ? ")
    nose = get_user_input("Pointed or Flat nose ? ")

    return body, hair, eye, earlobe, neck, nose, leg    


if __name__ == "__main__":

    engine = CatEngine()

    engine.reset()

    # getting input from user
    body, hair, eye, earlobe, neck, nose, leg = main_loop() 


    engine.declare(Cat(body=(body)), Cat(hair=hair),   Cat(eye=eye),   Cat(neck=neck),  Cat(earlobe=earlobe),  Cat(leg=leg),  Cat(nose=nose)) 

    print("Your Cat type is : ")
    engine.run()

