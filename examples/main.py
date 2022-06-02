from jewerly import Client
from discord_api import Intents


client = Client(intents=Intents(guilds=True).value)

@client.slash_command(name="ping", description="Ping command")
async def ping(interaction):
    await interaction.send("Pong!")
    
    
@client.slash_command(name="say", description="Send message", options={"text": "Text content"})
async def say(interaction, text):
    await interaction.send(text)
    
    
client.run("token")
