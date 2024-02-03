import discord
import keys

respostas = {
    "**EUGENIOOOOO**": "eae",
    "eita bixo": "sexo"
}

class bot(discord.Client):
    async def on_ready(self):
        print(f"{self.user} tá on")
        
        await self.change_presence(status=discord.Status.online)
        print(self.status)
    
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