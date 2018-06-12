import discord
import asyncio

description = "Monika-Bot"
bot_prefix = "m!"

client = discord.Client()

@client.event
async def on_ready():
	print("Logged in");
	print("Name: " + client.user.name);
	print("ID: " + client.user.id);
	print("\n\n");

@client.event
async def on_message(message):
	if message.content.startswith('bing'):
		await client.send_message(message.channel, "bong")
	if message.content.startswith('morning'):
		await client.send_message(message.channel, "Good morning <3")
	if message.content.startswith('afternoon'):
		await client.send_message(message.channel, "Good afternoon :white_sun_cloud:")
	if message.content.startswith('evening'):
		await client.send_message(message.channel, "Good evening :city_sunset:")
	if message.content.startswith('night'):
		await client.send_message(message.channel, "Good night :full_moon:")
	if message.content.startswith('m!triggers'):
		await client.send_message(message.channel, """This bot is still in the makings, 
... 								Currently availlable 'trigger words': 
...								bing, morning, afternoon, evening, night""")
		
client.run("NDU0NzUzOTg3MDUzNDg2MDkw.DfyPlA.Mveayqzgk_h6KU_goTxNJaCOeWQ");
