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
	if message.content.startswith('m!help'):
		await client.send_message(message.channel, "HELP")

client.run("NDU0NzUzOTg3MDUzNDg2MDkw.DfyCLQ.smx6ng_f3_C4PM9tHrxeCFoFrHY");
