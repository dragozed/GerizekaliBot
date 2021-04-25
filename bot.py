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
@client.event

async def on_message(message):
  
    if message.content.startswith("Duel me"): #Duel me function
      global duelBit #duelBit defines if duel is active
      global duelist1 #duel participant 1
      duelist1= message.author
      duelBit= True
      await message.channel.send("Rakip Bekleniyor")
      
      
    if message.content.startswith("Accepted") and duelBit== True and duelist1 != message.author: #Duel accepted function
      duelist2= message.author #duel participant 2
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
        n= 0
        while n<100:
          if duelistDatabase[n]== duelist1:
            break
          if n== 99:
            n=0
            while n<100:
              if duelistDatabase[n]==0:
                duelistDatabase[n]= duelist1 ; break
              n= n+1
            break  
          n= n+1
        scoreDatabase[n]= scoreDatabase[n]+1
      if roll2>roll1:#duelist2 won
        await message.channel.send("Winner is: "+str(duelist2))
        n= 0
        while n<100:
          if duelistDatabase[n]== duelist2:
            break
          if n== 99:
            n=0
            while n<100:
              if duelistDatabase[n]==0:
                duelistDatabase[n]= duelist2 ; break
              n= n+1
            break  
          n= n+1
        scoreDatabase[n]= scoreDatabase[n]+1
      if roll1==roll2:
        await message.channel.send("Draw ")

      f = open("data.txt", "a+") #open txt file append only, meaning: Open the file for writing. The data being written will be inserted at the end, after the existing data. 
      f.write("Winner is:"+str(duelist1)+"; ")
      print(f.read())
      f.close()
      duelBit= False
      
    if message.content.startswith("Total Score"):
      x= message.author
      
      n= 0
      while n<100:
        if duelistDatabase[n]== x:
          await message.channel.send("Total wins are: "+str(scoreDatabase[n]))
          break
        if n== 99:
          await message.channel.send("Total wins are: 0")
          n=0; break
        n= n+1
        print(duelistDatabase[n])
      
      
    
    
    
    if message.content.startswith("helikopter"):
        await message.channel.send(user.id)



    
client.run(token)
