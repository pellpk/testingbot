import discord
from discord.ext import commands
from discord.utils import get

# just to let you know my code is fucking ass and this is from an old ass template

TOKEN = 'no <3'  # the account token of your bot

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}!')  # prints a message that shows the bot is online.
#  above code logs the bot online

@bot.listen()
async def on_raw_reaction_add(payload):
    if payload.emoji.name == "<YOUR EMOJI HERE>":
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
        if reaction and reaction.count > 15:
            guild = bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(message.author.id)
            await member.ban(reason="Voted Out")
            
            # voted out.
            await channel.send(f"{member.mention} has been voted out.")

# basic functions, allows to read chat from console, and inside joke 
@bot.listen()
async def on_message(message):
    hoontee = {71372475925008384}

    username = str(message.author)  # username variable
    user_message = str(message.content)  # user message variable
    channel = str(message.channel.name)  # channel variable
    guild = str(message.guild.name)  # server variable (guild = server)
    user_ids_print = str(message.author.id)
    
    print(f'{username} ({user_ids_print}): {user_message}  (posted in "#{channel}" in "{guild}")')  # when a message is sent, it enters this in the terminal.
    #  i.e "noradrenalines: Hello. (posted in #fortnite in Fortnite Official)

    if message.author == bot.user:
        return  # ignores below code if message author is the bot
    
    if message.author.id in hoontee: # said inside joke
        await message.add_reaction('🫃')
    

bot.run(TOKEN)
