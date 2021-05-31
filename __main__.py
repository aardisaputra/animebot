import discord
import selenium
from discord.ext import commands
import io
import aiohttp
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
import sys
sys.path.append(".")
from webstuff import AnimeEntry
import webstuff

sys.path.append(".")
bot = commands.Bot(command_prefix='*', help_command=None)

#===========================EVENTS===============================
@bot.event
async def on_ready():

    #TODO fill in channel id
    anime_channel = bot.get_channel(________)

    await anime_channel.send("@everyone I'm online now!")

@bot.event
async def on_disconnect():

    #TODO fill in channel id
    anime_channel = bot.get_channel(________)

    await anime_channel.send("@everyone I'm went offline!")
#================================================================

#===========================COMMANDS=============================
@bot.command()
async def top(ctx, arg1):
    channel = ctx.channel
    type = "null"
    entryList = []
    embedList = []

    if(str.lower(arg1) == "air"):
        type = "Airing Now"
        entryList = webstuff.find_list("top_airing")

    elif(str.lower(arg1) == "upcoming"):
        type = "Upcoming"
        entryList = webstuff.find_list("top_upcoming")

    elif(str.lower(arg1) == "alltime"):
        type = "Alltime"
        entryList = webstuff.find_list("top_alltime")

    else:
        await channel.send("Only options are air (currently airing), upcoming, and alltime!")

    rank = 1
    for entry in entryList: 
        embedVar = discord.Embed(title=("Top " + type), 
                                description=entry.title, 
                                color=discord.Color.dark_orange())
        embedVar.set_image(url=entry.imageHTML)
        embedVar.add_field(name="Rank", value=rank)
        embedList.append(embedVar)
        rank += 1

    message = await channel.send(embed=embedList[0])

    await message.add_reaction('\u23ee')
    await message.add_reaction('\u25c0')
    await message.add_reaction('\u25b6')
    await message.add_reaction('\u23ed')

    i=0
    emote=''

    while True:
        if emote=='\u23ee':
            i=0
            await message.edit(embed=embedList[i])
        if emote=='\u25c0':
            if i>0:
                i-=1
                await message.edit(embed=embedList[i])
        if emote=='\u25b6':
            if i<(len(embedList)-1):
                i+=1
                await message.edit(embed=embedList[i])
        if emote=='\u23ed':
            i=(len(embedList) - 1)
            await message.edit(embed=embedList[i])

        reaction, user = await bot.wait_for('reaction_add', timeout=20)

        if reaction==None:
            break

        #TODO fill in bot name and id e.g. Anime Apostle#5688
        if user !=______:

            emote= reaction.emoji
            await message.remove_reaction(emote, ctx.author)

    await bot.clear_reactions(message)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def help(ctx):
    await ctx.channel.send("*top air - Top Anime Airing Now\n" +
                            "*top alltime - Top Anime Alltime\n" +
                            "*top upcoming - Top Upcoming Anime")
    
#================================================================

#TODO fill in bot token
bot.run(__________)

