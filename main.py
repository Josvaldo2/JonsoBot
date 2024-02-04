import discord
import json
import keys

with open("respostas.json") as f:
    respostas = json.load(f)

class bot(discord.Client):
    async def on_ready(self):
        print(f"{self.user} tá on")
        print(respostas)
        
        await self.change_presence(status=discord.Status.online)
    
    async def on_message(self, msg):
        if msg.author == self.user:
            return
        
        print(f"{msg.author} em {msg.channel}:\n   {msg.content}")

        if msg.content in respostas:
            await msg.channel.send(respostas[msg.content])

ints = discord.Intents.default()
ints.message_content = True

eugenio = bot(intents=ints)
eugenio.run(keys.token)