import os
import discord
import time
import random

my_secret = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
token = os.getenv("DISCORD_BOT_TOKEN")

print("I am ONLAYN")
global duelistDatabase
duelistDatabase= [0]* 100
global scoreDatabase
scoreDatabase= [0]* 100
duelist1= "None"
duelist2= "None"


def changeDuelistScore(duelist, k): 
  n= 0
  while n<100:
    if duelistDatabase[n]== duelist:
      break
    if n== 99:
      n=0
      while n<100:
        if duelistDatabase[n]==0:
          duelistDatabase[n]= duelist ; break
        n= n+1
      break  
    n= n+1
  scoreDatabase[n]= scoreDatabase[n]+ k
  return n

def setduelist1(duelist):
  global duelist1
  duelist1= duelist
  return duelist1

def setduelist2(duelist):
  global duelist2
  duelist2= duelist
  return duelist2
  



@client.event
      
async def on_message(message):
    if message.content.startswith("Help"): #Duel me function
      await message.channel.send("The commands are: \n Duel me; Accepted; Total Score\nBen ezik bir botum")

    if message.content.startswith("Duel me"): #Duel me function
      global duelBit, duelist1 #duelBit defines if duel is active
      if duelist1 == "None":
        setduelist1(message.author)
        duelBit= True
        await message.channel.send("Rakip Bekleniyor")
      else:
       await message.channel.send("Baska Duello Aktif") 
      
      
    if message.content.startswith("Accepted") and duelBit== True and duelist1 != message.author: #Duel accepted function
      global duelist2
      if duelist2 == "None":
        setduelist2(message.author)
        await message.channel.send(str(duelist1)+" vs "+str(duelist2))
        roll1= random.randint(0,6) #roll1
        roll2= random.randint(0,6) #roll2
        time.sleep(2)
        await message.channel.send(str(duelist1)+" rolls "+str(roll1))
        time.sleep(2)
        await message.channel.send(str(duelist2)+" rolls "+str(roll2))
        time.sleep(1)
        if roll1>roll2:#duelist1 won
          await message.channel.send("Winner is:"+str(duelist1))
          changeDuelistScore(duelist1, +1)
          changeDuelistScore(duelist2, -1)
        if roll2>roll1:#duelist2 won
          await message.channel.send("Winner is: "+str(duelist2))
          changeDuelistScore(duelist2, +1)
          changeDuelistScore(duelist1, -1)
        if roll1==roll2:
          await message.channel.send("Draw ")
        duelBit= False
        duelist1= "None" #clear duelists
        duelist2= "None" #clear duelists
        return duelist1,duelist2
      else:
        await message.channel.send("Duello onceden kabul edildi")
      
    if message.content.startswith("Total Score"):
      x= message.author
      n= 0
      while n<100:
        if duelistDatabase[n]== x:
          await message.channel.send("Score is: "+str(scoreDatabase[n]))
          break
        if n== 99:
          await message.channel.send("Score is: 0")
          break
        n= n+1


client.run(token)