from words import word_list
import random

def getRandom():
  word = random.choice(word_list)
  return word.upper()

def play(word):
  word_completion = '_' * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print('Lets Play Hangman!')
  print(displayHangman(tries))
  print(word_completion)
    
    while not guessed and tries > 0:
      guess = input('Enter your guess: ').upper()
      if len(guess) == 1 and guess.isalpha():
          if guess in guessed_letters:
              print("You already guessed the letter")
          elif guess not in word:
              print(guess, "is not in the word")
              tries -= 1
              guessed_letters.append(guess)
          else:
              print("Good Job,", guess , "is in the word")
              guessed_letters.append(guess)
              word_as_list = list(word_completion)
              indices = [i for i, letter in enumerate(word) if letter == i]
              for index in indices:
                word_as_list[index] = guess
              word_completion = "".join(word_as_list)
              if "_" not in word_completion:
                guessed = True
        elif len(guess) == len(word) and guess.isalpha():
          if guess in guessed_words:
            print("You already guessed the word", guess)
          
          
          
          
          
          
          
          
          
          
          
          elif guess != word:
            print(guess, "is not the word")
            tries -= 1
            guessed_words.append(guess)
          else:
            guessed = True
            word_completion = word 
        else:
          print('Not a valid guess')

        print(word_completion)                                   
        if guessed:
          print("Congrats , you guessed the word")
        else:
          print("Sorry , you ran out of tries")              
    
    def displayHangman(tries):
      stages = [  
            """
               --------
               |    |
               |    o
               |   \\|/
               |    |
               |   / \\
               -
            """
    
            """
               --------
               |    |
               |    o
               |   \\|/
               |    |
               |   /
               -
            """

            """
               --------
               |    |
               |    o
               |   \\|/
               |    |
               |
               -
            """

            """
               --------
               |    |
               |    o
               |   \\|
               |    |
               |
               -
            """

            """
               --------
               |    |
               |    o
               |    |
               |    |
               |
               -     
            """

            """
               --------
               |    |
               |
               |
               |
               |
               -
            """



      ]
      return stages[tries]                  
    
    def main():
      word = getRandom()
      print(word)
      play(word)

      again = input('Do you want to play again(Y/N): ').upper()
      while again == 'Y':
        play(word)  

    
    main()    

