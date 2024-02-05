import discord
import keys
from json import load
from random import choice

with open("respostas.json") as f:
    respostas = load(f)

class bot(discord.Client):
    async def on_ready(self):
        print(f"{self.user} tá on")

        status = (discord.Status.online, discord.Status.do_not_disturb, discord.Status.idle)
        await self.change_presence(status=choice(status))
    
    async def on_message(self, msg):
        if msg.author == self.user or msg.author.bot:
            return
        
        print(f"{msg.author} em {msg.channel}:\n   {msg.content}")

        resposta = respostas.get(msg.content.lower())
        if resposta:
            await msg.channel.send(resposta)

ints = discord.Intents.default()
ints.message_content = True

eugenio = bot(intents=ints)
eugenio.run(keys.token)