import discord
import openai
import keys

intents = discord.Intents.default()
intents.message_content = True

# Keys
DISCORD_TOKEN = keys.discord_token
openai.api_key = keys.openai_key

# Initialize a client object for Discord bot
client = discord.Client(intents=intents)

# Function that sends message to OpenAI API and gets response
async def ask_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message.content}
        ]
    )
    answer = response.choices[0].message.content
    return answer

# Listener that checks for messages in Discord
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response = await ask_gpt(message)
    await message.channel.send(response)

client.run(DISCORD_TOKEN)