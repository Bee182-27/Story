import time
import random
## Welcome
print("Welcome to Shadow Peak!")     
name = input("What is your name traveler? ")
print("Welcome " + name + "!" " my name is Quest-Master Ronin, I've been handeling quests since I was young man")
work = input("Are you looking for work" " "+ name + "? I'm always willing to help someone when they need it " "(yes/no) ")
if work == "yes":
  print("Great! The great world of Shadow Peak needs all the help it can get, especially with the forces of evil beginning to grow")
else:
  print("Oh I understand, I bid you farewll then, good luck on your journey")
  exit()

## Sub class
print("Please choose a class! ")
print("Choose wisely " + name + " we can't have you getting too powerful now!")
subclass = input("1) Paladin , 2) Ranger , 3) Storm-Walker ")
if subclass == "Paladin":
  print("Ah yes, the loyal Paladin, known for their courage and aggressive fighting style. The Paladin is a foe not to be taken lightly, Welcome aboard Paladin " + name)
  time.sleep(5)
elif subclass == "Ranger":
  print("Although small in stature, the Ranger is often known to be adaptive and verstaile, choosing stealth and tactics over recklessness, good hunting Ranger " + name)
  time.sleep(5)
elif subclass == "Storm-Walker":
  print("Masters at elemental magic, be wary of their shocking yet delicate touch, bring the balance between the elements Storm-Walker " + name)
  time.sleep(5)

## Subclass abilities
lis_t = Paladin = [" Warcry", "Revenge", "Berserker"]
lis_t = Ranger  = ["Wisp", "Stalk", "Pinpoint"]
lis_t = StormWalker  = ["Nurture", "Seasons", "Summon"]

## Subclass functions
def pldn():
  abl1 = input("Please enter your ability choice! ")
  if abl1 == "1":
    print("Paladin " + name + " used " + Paladin[0] + "!")
    print("Your first ability is Warcry, paralyze your eneimies with a deafening scream that could even make the elder gods shiver! ")
    time.sleep(4)
    print("Now onto your next ability!")
    time.sleep(5)
  elif abl1 == "2":
    print("Paladin " + name + " used " + Paladin[1] + "!")
    print("Revenge is your 2nd ability, the enemy can poke at you all they want, but they better be ready when you use all that stored power to strike 2X harder!")
    time.sleep(5)
    print("Now onto your next ability!")
    time.sleep(4)
  elif abl1 == "3":
    print("Paladin " + name + " used " + Paladin[2])
    print("Berserker is your 3rd ability and it's a fun one, boost yourself to max HP and damage is increased by 3x for one turn. Use the power boost wisely!")
    
def rngr():
  abl2 = input("Please enter your ability choice! ")
  if abl2 == "1":
    print("Ranger " + name + " used " + Ranger[0])
    print("Your first ability is Wisp, use this directional dash to get an edge on your enemies!")
    time.sleep(4)
    print("Now onto your next ability!")
    time.sleep(5)
  elif abl2 == "2":
    print("Ranger " + name + " used " + Ranger[1])
    print("Stalk is your 2nd ability, use Stalk to silence your footsteps, making it easier to sneak up on your enemies...or use it to find some precious loot, up to you!")
    time.sleep(5)
    print("Now onto your next ability!")
    time.sleep(5)
  elif abl2 == "3":
    print("Ranger " + name + " used " + Ranger[2])
    print("Pinpoint is your 3rd ability, now you wanna take an ogre or a goblin right in between the eyes, or maybe tryinng to hit a sick trickshot? Pinpoint increases your focus, giving you 100% accuracy guranteed!")
    
def strwlk():
  abl3 = input("Please enter your ability choice! ")
  if abl3 == "1":
    print("Storm-Walker " + name + " used " + StormWalker[0] + "!")
    print("Nurture is your 1st ability, it harnesses the elemental magic of water to heal you and your teammates by 30 HP")
    time.sleep(5)
    print("Now onto your next ability!")
    time.sleep(5)
  elif abl3 == "2":
    print("Storm-Walker " + name + " used " + StormWalker[1] + "!")
    print("Seasons is your 2nd ability, Seasons gives you the ability to shift through the 4 main types of elemental magic, Lightning, Fire, Water, and Air, to shoot a powerful blast of elmental magic. Keep this in mind Storm-Walker " + name + ", " " you can only use 1 form of elemental magic once per turn, choose carefully! ")
    time.sleep(7)
    print("Now onto your next ability!")
    time.sleep(5)
  elif abl3 == "3":
    print("Storm-Walker " + name + " used " + StormWalker[2] + "!")
    print("Summon is your 3rd ability, use elemental magic to summon a giant beast made up of the same elemental magic type type chosen in Seasons")

## number generator
def rannum():
  random.randint(0, 10)
def ranDefend():
  random.randint(0, 5)

## enemy generator
lis_t = skullKnight = ["Slash," "Thrust," "Nullify"]
lis_t = Minatuar = ["Slam," "Axe-Throw," "Rage"]
lis_t = Corpse = ["Bite", "Poison", "Catacomb"]
lis_t = Dragon = ["Blast", "Swipe", "Super-Heat"]

## attack effectivness
attack = rannum()
##if attack >= 5:
  ##print("Your attack was effective!")
##else:
  ##print("Miss! Try to dodge")

## Dodge effectivness
dodge = ranDefend()
##if dodge <= 3:
  ##print("Dodged!")
##else:
  ##print("You were hit!")

## Enemy ability random select
def enmabl1():
  print("Skull Knight used" + random.choice(skullKnight))


# Location setup    
if subclass == "Paladin":
  print("Head to Diburh, the City of Gates " + subclass  + " " + name + "," " the Paladin guild will teach you your abilites and how to use them ")
  time.sleep(8)
elif subclass == "Ranger":
  print("Ranger " + name + ", " "head for Bariande, the City Beneath the Spire " )
  print("The Ranger guild stays on the move, it's best if you hurry before they disappear ")
  time.sleep(8)
elif subclass == "Storm-Walker":
  print(subclass + " " + name + "! "" Mamoor, City of the Old Ones is where you must venture")
  time.sleep(8)
  print("The Storm-Walker guild are few, but they will be willing to help you")

## Story print("Here " + subclass  + " " + name  + " take this map to find your way")
print("Now " + subclass  + " "  + name  + " your training must begin at once, use this rune stone to teleport you to your destination")
print("Opening rune stone menu...")
time.sleep(8)
print("Where would you like to travel" " " + subclass + " " + name + "? " )
location = input("Please enter a location! ")

## Diburh / ability display
if location == "Diburh":
  print("Traveling to Diburh, the City of Gates...")
  time.sleep(8)
  print("Welcome to Diburh " + subclass + " " + name)
  print("My name is Shane, Questmaster Ronin told me about you, I'll be your trainer and brother in arms ")
  ans1 = input("Are you ready to get started on your abilities? ")
  if ans1 == "yes":
    print("Loading abilities...")
    time.sleep(8)
    print(*Paladin, sep = " , ")
    print("When you want to use an ability simply enter the value the ability is associated with (i.e: 1, 2, 3) ")
    for i in range(3):
      pldn()

## Bariande    
elif location == "Bariande":
    print("Traveling to Bariande, the City beneath the Spire...")
    time.sleep(8)
    print("Hey you the one Ronin won't stop talking about? Names Holden, I'll be helping you along to make you a full fledge Ranger, who needs swords and giant hunks of armor when you've got the shadows am I right?")
    ans2 = input("Ready yourself Ranger " + name + " wanna know your abilities? ")
    if ans2 == "yes":
     print("Loading abilities...")
    time.sleep(8)
    print(*Ranger, sep = " , ")
    print("When you want to use an ability simply enter the value the ability is associated with (i.e: 1, 2, 3)")
    for i in range(3):
      rngr()

## Mamoor
if location == "Mamoor":
  print("Traveling to Mamoor...the City of the Old Ones")
  time.sleep(8)
  print("Welcome " + subclass + " " + name + ", "" Quest-master Ronin has informed me of your arrival ")
  print("I am Meritoc, I will teach you the ways of our people, as well as how to master your abilities")
  ans3 = input("Now then, with the forces of darkness growing, shall we beign your training? ")
  if ans3 == "yes":
    print("Excellent! This potion shall display your abilties, every Storm-Walker's abilities are different so this indeed shall be interesting")
    print("Loading abilities...")
    time.sleep(8)
    print(*StormWalker, sep = " , ")
    print("When you want to use an ability simply enter the value the ability is associated with (i.e 1, 2, 3) ")
    for i in range(3):
      strwlk()
      break


  


