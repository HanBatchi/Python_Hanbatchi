
def print_upper_words(word_list, start_letter):

  """Print any word you want in upper case. Add special starts letters."""

  #we pass the words to lower case to look for the desired leeter. Then we also pass the desire letter to lower case, in case that the user type the letter in upper case

  for words in word_list:
    if any(words.lower().startswith(letter.lower())for letter in start_letter):
        print(words.upper())
  
words_to_print = ["apple", "orange", "strawberry", "Electric", "Enamorado"]
letter_to_check = ["e", "o"]
print_upper_words(words_to_print,letter_to_check)