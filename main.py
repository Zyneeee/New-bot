from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return '''<body style="margin: 0; padding: 0;">
    <iframe width="100%" height="100%" src="https://bot-status-phi.vercel.app/" frameborder="0" allowfullscreen></iframe>
  </body>'''

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()

keep_alive()
print("Server Running Because of Zcy")
import discord
from requests import get
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Rizz You Up"))
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'rizz' in message.content.lower():
        pickup_line = fetch_pickup_line()
        if pickup_line:
            await message.channel.send(pickup_line)
        else:
            await message.channel.send("I'm sorry, I couldn't fetch a pickup line at the moment. Can you try again later?")

def fetch_pickup_line():
    try:
        pickup = get("https://vinuxd.vercel.app/api/pickup").json()["pickup"]
        return pickup
    except Exception as e:
        print(f"An error occurred while fetching pickup line: {e}")
        return None

client.run(os.getenv('BOT_TOKEN'))
