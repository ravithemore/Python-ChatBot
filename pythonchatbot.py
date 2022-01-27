
 

   
# Pocket Pen Pal 

# Username Input 
print ("Welcome to My World Pal! Let's get fired up!")
username = input(str("What's your name buddy? "))
print (f"Well... Hey there, {username}!")

# Have user choose city
city = input(str("Where would you like your AIBOT Pal to be from? (Choose from either Paris, Tokyo,Los Angeles, or Ahemadabad) "))

if city.lower() == "paris":
    print ("Bonjour! I am from Paris, the most romantic city in the world!")
elif city.lower() == "tokyo":
    print ("Kon'nichiwa! I am from Tokyo, the jungle of electric lights and colors at night!")
elif city.lower() == "los angeles":
    print ("Hey! I am from Hollywood, the land of glamour, palm trees, and sunny skies!")
elif city.lower() == "Ahemadabad":
    print ("Namaste! I am from Ahemdabad, the land of textiles and food, speices and culture and tradition. It's an awesome India😊!")  
else:
    print ("You need to select from Paris, Tokyo, Los Angeles or Ahemadabad. :)")

# Ask user for their city
user_city = input (str("What city are you in? :) "))
print (f"So you're from {user_city}! Sweet! I've heard nice things about your city. The people there are really awesome cool and always sweet😊 :)")

# Import your choice module
from random import choice

# Create function for user's mood
def get_bot_response(user_response):
  bot_response_happy = ["That's so good to hear!", "That makes ME happy to hear!", "There is nothing more then that,  makes me happier!"]
  bot_response_sad = ["Don't worry. You're not alone!", "I wish there was something I could do to help you feel better!", "Well I'm sorry, but hey, I'm sending you only the best of vibes!"]
  if user_response.lower() == "happy":
    return choice(bot_response_happy)
  elif user_response.lower() == "sad":
    return choice(bot_response_sad)
  else:
      return "You do you! :)"

# Get user mood
while True:
  user_response = input("How are you feeling today? (Happy or sad? Type 'done' for next question.) ")
  if user_response == 'done':
    break
  bot_response = get_bot_response(user_response)
  print(bot_response)

# Ask user what awesome activity they did today
activity = input (str("Can you tell me one cool thing you did today? "))
print ("That sounds pretty interesting and fascinating!")

# Ask user if they want to hear what you did today
bot_activity = input (str("Do you want to hear what I did today? (Yes or No?) "))
if bot_activity.lower() == "yes":
  print ("I actually was a tourist in my own city today! I visited all the popular travel destinations in my area!. Had burgers fries ,drank booze ,danced like hell and a lot more")
elif bot_activity.lower() == "no":
  print ("That's alright. :)")
else:
  print (f"Well, no worries! It seems as if you are no longer interested in chatting, so I hope you have a great rest of your day, {username}!")

# Get user's favorite book
book = input (str("After a long day, there is nothing like unwinding with a good book. So... I'm curious. What is your favorite book? :) "))
print (f"So yours is {book}! Mine is probably... 'Harry Potter' by J.K. Rowling and Atomic Habits by James Clear.")

# Get user's favorite game
game = input (str("Let's move on to something way more fun! What is your favorite video game?" ))
print (f"OMG! Your favorite game is {game}! I too love that one. I personally love TOM CLANCY ,GTA 5 and RDR-2.")

# Create function for user's favorite food
def get_user_food(user_food):
  user_food_sushi = ["I love California rolls!", "Sign me up for a nice bento box!", "OMG, tempura with ANY sushi and then add miso soup... Yuuuums."]
  user_food_burritos = ["A steak burrito can hit the spot!", "I'm such a huge fan of any burrito bowl known to man AND woman!", "Burritos without chips and salsa? Whaaaat?! AM I RIGHT OR AM I RIGHT?"]
  user_food_burgers = ["In N Out is my favorite burger joint!", "I can't blame you... a burger and fries is classic. Oh, can't forget the milkshake... strawberry for me, please!", "Yes! Just don't forget to pair it with a nice side of fries and a shake! :)"]
  if user_food.lower() == "sushi":
    return choice(user_food_sushi)
  elif user_food.lower() == "burritos":
    return choice(user_food_burritos)
  elif user_food.lower() == "burgers":
    return choice(user_food_burgers)
  else:
      return "I am always open to trying out new dishes! :)"

# Get user's favorite food
while True:
  user_food = input("Geez... all this talk about gaming is making me hungry. I usually love to top off a great gaming session with a savory meal! Hmm... Which food is your favorite: sushi, burritos, or burgers? (Type 'done' for next interaction.) ")
  if user_food == 'done':
    break
  user_food = get_user_food(user_food)
  print(user_food)

# Say goodbye to user 
print ("I think it is time for me to go ahead and make a meal! All that talk about food... Hehe, but it was so wonderful chatting with you! I truly hope you can visit my city sometime soon! Ciao")
