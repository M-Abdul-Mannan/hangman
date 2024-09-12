import random

def main():

        HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")
        play_again = True
        while play_again: 
                words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                        "computer", "python", "program", "glasses", "sweatshirt",
                        "sweatpants", "mattress", "friends", "clocks", "biology",
                        "algebra", "suitcase", "knives", "ninjas", "shampoo"]

                chosen_word = random.choice(words).lower()
                player_guess = None
                guessed_letters = []
                word_guessed = [] #["-"] * len(chosen_word)
                for letter in chosen_word:
                       word_guessed.append("-")

                joined_word = None

                print(HANGMAN[0])
                
                play_again = False;

                attempts = len(HANGMAN) - 1

                while attempts > 0 and "-" in word_guessed:
                       print(f"You have {attempts} attempts left")
                       joined_word = "".join(word_guessed)
                       mistake = False
                       print(joined_word)

                       try : 
                                player_guess = str(input("Please select a letter between A-Z : ")).lower()
                                print(f"The letter you chose is : {player_guess}")
                       except :
                                print("This is an invalid input. Please try again")
                                continue
                       else :
                                if not player_guess.isalpha() : 
                                       print("That is not a letter, you illiterate fuck")
                                       mistake = True
                                elif len(player_guess) > 1:
                                        print("That is more than one letter, dumbass. Give it another shot")
                                        mistake = True
                                elif player_guess in guessed_letters:
                                        print("You have already guessed that letter dipshit. Try the fuck again")
                                        mistake = True
                                else : 
                                        pass
                        
                       guessed_letters.append(player_guess)
                       for letter in range(len(chosen_word)):
                               if player_guess == chosen_word[letter]:
                                       word_guessed[letter] = player_guess

                       if player_guess not in chosen_word or mistake:
                               attempts -= 1
                               print(HANGMAN[len(HANGMAN) - 1 - attempts])
                if "-" not in word_guessed:
                        print(f"You did it, you son of a bitch. The word was {chosen_word}.")
                else:
                        print(f"Haah you stupid fuck. The word was {chosen_word}.")

if __name__ == "__main__":
    main()
