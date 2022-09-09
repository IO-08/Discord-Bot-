import discord
import random
import requests
import json

intents = discord.Intents.default()
intents.message_content = True
sad_words= ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"] #making of list sad words that can be typed in to get encourage words
starter_encouragements= ["Cheer up!", "Hang in there", "You are a great person/bot"] #makinf a lsit of feesback

#function that gets the quote from an API
def get_quote():
    response = requests.get ("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

#function that enables the discord bot to run.
def run_discord_bot():
    TOKEN = ''
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        print ( 'We have logged in as {0.user}'.format ( client ) )

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hey there!')
        if message.content.startswith('inspire'):
            quote = get_quote()
            await message.channel.send ( quote)
        if any(word in message.content for word in sad_words):
            await message.channel.send (random.choice(starter_encouragements))
        if message.content.startswith('roll' ):
            await message.channel.send( random.randint ( 1, 6 ) )
        if message.content.startswith('Sad') or message.content.startswith('sad') :
            await message.channel.send ( 'Smile')

    client.run ( TOKEN )

