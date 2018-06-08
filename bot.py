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

client.run("NDU0NzUzOTg3MDUzNDg2MDkw.DfyPlA.Mveayqzgk_h6KU_goTxNJaCOeWQ");
