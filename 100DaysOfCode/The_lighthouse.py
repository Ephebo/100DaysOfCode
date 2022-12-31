print("""
                   .
             \ _ /     .-='-. _db_      .--==-,
           -= (_) =-  (_  (  _IIII_   _(    )  `.
             /   \      (    |" " |-.(  ` ,_  `  )
               '         '-._HHHHHH  `)---' `'--'    =.=
                             |.   |--`                    =.=
                             |    |      =.=
                   _H___,=====;___|           =.=
                n_/____/____/``\__|
               /__|:: :|. .|:::|::|                  =.=
            _%&|__&%_"_|_"_|_ H|__|__
           jgs`";;;;`";;;;'";;'"';;;;``;;-.
           .  ' `";;'  `;;;  `;'   `;  .`' `|
           . '  .  `' .  `';.    '   .   .  |^-`^~_^^~``-^^_~^^-`^~
             
""")

print("""
                    Welcome to Mysterious place...
                    
      noise....A hard noise and....asleeping, you wake up in a dark room.      
   ...HAAAAAGH, You hear something! 
      There is a staircase nearby.   
         
      """)

choice1 = input(
    "choose to get out or stay? ")
if choice1 == "get out":
    print("""
        
          You get out of that room...
          In the outside, you notice that you are in a lighthouse.
          The place looks strange.
           
        """)
    choice2 = input(
        "Choose to walk around the lighthouse? ")
    if choice2 == "walk" or choice2 == "walk around" or choice2 == "yes":
        print("""
              you found blood everywhere, and hear something inside that lighthouse.
              Next to the blood, there's a knife!
                    
              """)
        choice3 = input("Take the knife or return? ")

        if choice3 == "take the knife":
            print("""
                  You take the knife, when a man comes to you...
                  sunddlyn, he tried to hurt you...
                  """)
            final = input("kill him or die? ")
            if final == "kill him" or final == "kill":
                print("""
                      
                      You killed him and has survived. 
                       
                      """)
            else:
                print("You are dead. Game Over.")
        else:
            print("""
                  Try to go back to the lighthouse but the doors is closed!
                  """)
    else:
        print("""
              Try to go back to the lighthouse but the doors is closed!
              """)
else:
    print("""
          all of a sudden...\n DEAD! Someone appears and attack you with a knife!
          """)
