# Do-You-Know-Your-Cat?

An very simple Expert System, to tell what type is your cat.


Rather than re-inventing the wheel, I'am going to use some readily available solution. There are several expert systems out there and I'll focus on those which are either in Python or can be used via Python.


#### CLIPS

    ```CLIPS``` is an expert system developed by NASA. 
    It's considered state of the art and used in university courses when teaching the basics of AI (idk why it's a sepreated Course though). 

    it's written in Lisp. The advantage of CLIPS is that is a solid C engine which can be fully integrated with any other Python system via its bindings:
    the older pyclips and the newer clipspy. The bindings allow to embed Python code within the CLIPS language making it very easy to extend.

    Rules can be loaded at runtime without the need of restarting the engine which should better suit your need.


#### PyKnow/Experta 

    Here we can express knowledge bases mostly in Python
    

### Main Idea


How to know your cat's type ?

##### Cat Generic Parts: 

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

##### Rules :

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

### Refs

[research gate](https://www.researchgate.net/publication/329401998_Expert_system_for_determining_the_type_of_cats_and_how_to_care_them#pf5)
