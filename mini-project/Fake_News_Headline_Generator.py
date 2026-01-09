#1 step: import random module
import random

#step 2: create list of subject, object ,action
subjects =[
  "Shahrukh Khan",
  "Virat Kohli",
  "Nirmala Sitarman",
  "A Mumbai Cat",
  "A Group of Monkeys",
  "Prime Minister Modi",
  "Auto Rickshaw Driver from Delhi"
]
actions=[
  "Launches",
  "Cancels",
  "Declares War on",
  "orders","eats",
  "dance with",
  "celebrates"
]
places_or_things=[
  "at red fort",
  "mumbai local train",
  "plate of samosa",
  "inside parliament",
  "near ganga ghat",
  "india gate",
  "visit maheswar on 30th February "
]

#step3 : start the headline generation loop
while True:
  subject =random.choice(subjects)
  action =random.choice(actions)
  place_or_thing= random.choice(places_or_things)

  headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
  print("\n" + headline)

  user_input = input("\n Do you want another headline? (yes/no)").strip().lower() # strip use to remove extra spaces its two types left strip /right strip
  if user_input=="no":
    break

# step 4 : print goodbye message
print("\n Thanks for using the Fake News Headline Generator. Have a fun day")
