"""
How to know if your cat type ?

Body :
    Big
    Medium
Hair :
    Long
    Short
    Unavailable
Eye :
    Sharp
    Round
Earlobe :
    Wide
    Small
    Medium
Neck :
    Meduim
    Short
Leg : 
    Short 
    Meduim
Nose:
    Flat
    Pointed


Rule 1 : 

    Body Big and Hair Long and Eye Sharp and Neck Medium and Earlobe Wide and Leg Medium and Nose Pointed THEN : Maine Coon    

Rule 2 : 

    Body Big and Hair Long and Eye Sharp and Neck Short and Earlobe small and Leg Short and Nose Flat THEN : Persia Himalaya    


Rule 3 : 

    Body Big and Hair Long and Eye Round and Neck Short and Earlobe Small and Leg Short and Nose Flat THEN : Persia Peaknose 


Rule 4 : 

    Body Meduim and Hair Short and Eye Round and Neck Short and Earlobe Small and Leg Short and Nose Flat THEN : Exotic Shorthair 


Rule 5 : 

    Body Meduim and Hair Short and Eye Sharp and Neck Medium and Earlobe Medium and Leg Medium and Nose Pointed THEN : Russian Blue 


Rule 6 : 

    Body Medium and Hair Long and Eye Sharp and Neck Medium and Earlobe Wide and Leg Medium and Nose Pointed THEN : Anggora   


Rule 7 : 

    Body Medium and Hair Short and Eye Sharp and Neck Medium and Earlobe Meduim and Leg Medium and Nose Pointed THEN : Siamese   


Rule 8 : 

    Body Meduim and Hair Short and Eye Round and Neck Short and Earlobe Small and Leg Medium and Nose Flat THEN : Scotishfold   


Rule 9 : 

    Body Medium and Hair Unavailable and Eye Sharp and Neck Medium and Earlobe Wide and Leg Medium and Nose Pointed THEN : Sphynx   


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
         



def main_loop():
    """Taking Input from User"""
    
    print("Descibe Your Cat ...")

       
    body = input("Big or Meduim body ? ").strip().lower()
    hair = input("Long or Short or no hair ? ").strip().lower()
    eye = input("Sharp or Round eyes ? ").strip().lower()
    neck = input("Short or Meduim neck ? ").strip().lower()
    earlobe = input("Wide or Meduim or Small earlobe ? ").strip().lower()
    leg = input("Short or Meduim legs ? ").strip().lower()
    nose = input("Pointed or Flat nose ? ").strip().lower()

    return body, hair, eye, earlobe, neck, nose, leg    


if __name__ == "__main__":

    engine = CatEngine()

    engine.reset()

    # getting input from user
    body, hair, eye, earlobe, neck, nose, leg = main_loop() 


    engine.declare(Cat(body=(body)), Cat(hair=hair),   Cat(eye=eye),   Cat(neck=neck),  Cat(earlobe=earlobe),  Cat(leg=leg),  Cat(nose=nose)) 

    print("Your Cat type is : ")
    engine.run()

