import discord
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace with your bot token and channel ID from environment variables
TOKEN = os.getenv('TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)

    if channel is None:
        print(f"Channel with ID {CHANNEL_ID} not found. Please check the ID and bot permissions.")
        await client.close()
        return

    messages = []

    async for message in channel.history(limit=None):
        for reaction in message.reactions:
            async for user in reaction.users():
                messages.append({
                    'Message ID': message.id,
                    'Author': message.author.name,
                    'Content': message.content,
                    'Timestamp': message.created_at,
                    'Reaction': reaction.emoji,
                    'Reacted by': user.name
                })

        if not message.reactions:
            messages.append({
                'Message ID': message.id,
                'Author': message.author.name,
                'Content': message.content,
                'Timestamp': message.created_at,
                'Reaction': None,
                'Reacted by': None
            })

    # Save to CSV
    df = pd.DataFrame(messages)
    df.to_csv('discord_messages.csv', index=False)
    print('Messages saved to discord_messages.csv')
    await client.close()

client.run(TOKEN)
