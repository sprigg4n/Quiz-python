'''
Class: Is like an object constructor, or a "blueprint" for creating objects.
an instance of that blueprint. (In this case we use "Question")

self: as arguments.

Def: is a class methods.

__init __ () 
Internal function. Assigns values ​​to object properties or other operations.

\n break line.

For:  loop is used for iterating over a sequence.

If:  logical conditions.

Assignment Operators:
= equal
+= add +1 number
 Comparison Operators:
== equals/
'''

class Question:  
     def __init__(self, prompt, answer): 
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What is my favorite color?\n(a) lightred\n(b)black\n(c) Glitter\n",
     "\nWhat I want with you now?\n(a) lovesex with u\n(b)Nothing\n(c) sleep\n",
     "\nWhat I prefer watch?\n(a) Dramas\n(b) Anime\n(c) Movies\n",
     "\nMy favorite Musics:\n(a) Rock/Metal\n(b) Asiatic Instrumental\n(c) a&b love two options..\n",
     "\nP, love me?\n(a) N\n(b) Y\n(c) Null\n"

]
questions = [
     Question(question_prompts[0], "c"),
     Question(question_prompts[1], "a"),
     Question(question_prompts[2], "b"),
     Question(question_prompts[3], "c"),
     Question(question_prompts[4], "b")
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)