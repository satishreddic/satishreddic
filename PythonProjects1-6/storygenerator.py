# Importing random module
import random
  
# Defining list of phrases which will help to build a story
  
Sentence_starter = ['Last year', ' In the second century', 'Once upon a time']
character = [' there lived a soldier.',' there was a man named Daniel Errico.',
             ' there lived a socialist.']
time = [' One fine day', ' One full-moon night','at midnight']
story_plot = [' she was passing by',' she was going for a trip to ']
place = [' the mountains', ' the garden','the river side','to beach side']
second_character = [' she saw a man', ' she saw a young handsome boy']
age = [' who seemed to be hurry', ' who seemed very old and feeble','who seemed to be busy','who seemed to be so sad']
work = [' searching something.', ' digging a well on roadside.']

# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
      random.choice(time)+random.choice(story_plot) +
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work))