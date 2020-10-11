import os
import discord
import math
import asyncio
import random
import json
from discord.ext import commands
client = commands.Bot(command_prefix='!', help_command=None)

with open("data.txt") as json_file:
    datadic = json.load(json_file)

channel1available = True
channel2available = True
channel3available = True

def keys_exists(element, *keys):
    if not isinstance(element, dict):
        raise AttributeError('keys_exists() expects dict as first argument.')
    if len(keys) == 0:
        raise AttributeError('keys_exists() expects at least two arguments, one given.')
    _element = element
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return True
    
embedhelp = discord.Embed(title='Help Menu')
embedhelp.add_field(name='!roles', value="Lists out all roles avaialable.", inline=False)
embedhelp.add_field(name="!role <action> <name>", value ="""Adds/Removes a role.
**Parameters**
action: "add" or "remove"
name: Role's name. Must be on the list (!roles)""", inline=False)

embedtimeout = discord.Embed(title='Process Failed')
embedtimeout.add_field(name='Reason', value='Timeout', inline=False)

embedvalueerror = discord.Embed(title='Process Failed')
embedvalueerror.add_field(name='Reason', value='Value Error', inline=False)

# Dice Roll
@client.command(name='roll')
async def roll(ctx, arg1):
    userid = ctx.author.id
    user = client.get_user(userid)
    try:
        if arg1 == "0":
            await ctx.send("Please enter a number greater than 0.")
        else:
            max = int(arg1)
            randno = random.randint(1, max)
            embedrandom = discord.Embed(title="{}".format(user.name))
            embedrandom.add_field(name='Roll', value = "{}".format(randno), inline=True)
            await ctx.send(embed=embedrandom)
    except ValueError:
        await ctx.send(embed=embedvalueerror)

# Add/Remove Roles
embedrole = discord.Embed(title='Available roles')
embedrole.add_field(name='Do !role <add/remove> <rolename> to receive the role', value="""Dead, but hidden
map editor
#Anime
SHB
Nova Aeterna
norrpakten
GL
Eternal Cosmos""")

@client.command(name='roles')
async def roles(ctx):
    await ctx.send(embed=embedrole)

@client.command(name='role')
async def role(ctx, arg1, arg2):
    user = ctx.message.author
    if arg1 == "add":
        if arg2 == "dead":
            await user.add_roles(discord.utils.get(user.guild.roles, name='Dead, but hidden'))
            await ctx.send("Role given!")
        elif arg2 == "map":
            await user.add_roles(discord.utils.get(user.guild.roles, name='map editor'))
            await ctx.send("Role given!")
        elif arg2 == "anime":
            await user.add_roles(discord.utils.get(user.guild.roles, name='#Anime'))
            await ctx.send("Role given!")
        elif arg2 == "shb":
            await user.add_roles(discord.utils.get(user.guild.roles, name='SHB'))
            await ctx.send("Role given!")
        elif arg2 == "na":
            await user.add_roles(discord.utils.get(user.guild.roles, name='Nova Aeterna'))
            await ctx.send("Role given!")
        elif arg2 == "nrp":
            await user.add_roles(discord.utils.get(user.guild.roles, name='norrpakten'))
            await ctx.send("Role given!")
        elif arg2 == "gl":
            await user.add_roles(discord.utils.get(user.guild.roles, name='GL'))
            await ctx.send("Role given!")
        elif arg2 == "ec":
            await user.add_roles(discord.utils.get(user.guild.roles, name='Eternal Cosmos'))
            await ctx.send("Role given!")
        else:
            await ctx.send("Invalid role.")
    elif arg1 == "remove":
        if arg2 == "dead":
            await user.remove_roles(discord.utils.get(user.guild.roles, name='Dead, but hidden'))
            await ctx.send("Role removed!")
        elif arg2 == "map":
            await user.remove_roles(discord.utils.get(user.guild.roles, name='map editor'))
            await ctx.send("Role removed!")
        elif arg2 == "anime":
            await user.remove_roles(discord.utils.get(user.guild.roles, name='#Anime'))
            await ctx.send("Role removed!")
        elif arg2 == "shb":
            await user.remove_roles(discord.utils.get(user.guild.roles, name='SHB'))
            await ctx.send("Role removed!")
        elif arg2 == "na":
            await user.remove_roles(discord.utils.get(user.guild.roles, name='Nova Aeterna'))
            await ctx.send("Role removed!")
        elif arg2 == "nrp":
            await user.remove_roles(discord.utils.get(user.guild.roles, name='norrpakten'))
            await ctx.send("Role removed!")
        elif arg2 == "gl":
            await user.remove_roles(discord.utils.get(user.guild.roles, name='GL'))
            await ctx.send("Role removed!")
        elif arg2 == "ec":
            await user.remove_roles(discord.utils.get(user.guild.roles, name='Eternal Cosmos'))
            await ctx.send("Role removed!")
        else:
            await ctx.send("Invalid role.")
    else:
        await ctx.send("Invalid action.")

# Suggest
@client.command(name='suggest')
async def suggest(ctx):
    channel = client.get_channel(664615244236062727)
    user = ctx.message.author
    userid = ctx.author.id
    await channel.send("Please give a brief description of the problem.")
    try:
        await client.wait_for('message', timeout=60)
    except asyncio.TimeoutError:
        await channel.send(embed=embedtimeout)
    else:
        async for message in channel.history(limit=1):
            if message.author == user:
                problem = message.content
                await channel.send("Please provide details regarding the problem.")
                try:
                    await client.wait_for('message', timeout=60)
                except asyncio.TimeoutError:
                    await channel.send(embed=embedtimeout)
                else:
                    async for message in channel.history(limit=1):
                        if message.author == user:
                            details = message.content
                            await channel.send("Please propose a solution.")
                            try:
                                await client.wait_for('message', timeout=60)
                            except asyncio.TimeoutError:
                                await channel.send(embed=embedtimeout)
                            else:
                                async for message in channel.history(limit=1):
                                    if message.author == user:
                                        solution = message.content
                                        await channel.send("Process complete.")
                                        embedsuggest = discord.Embed(title='Suggestion', description="Author: <@{}>".format(userid))
                                        embedsuggest.add_field(name="Problem", value="{}".format(problem), inline=False)
                                        embedsuggest.add_field(name="Details", value="{}".format(details), inline=False)
                                        embedsuggest.add_field(name="Solution", value="{}".format(solution), inline=False)
                                        channel = client.get_channel(666213834675060749)
                                        await channel.send(embed=embedsuggest)

# Ships and Fleets

@client.command(name='create')
async def create(ctx):
    global channel1available
    global channel2available
    global channel3available
    global datadic
    user = ctx.message.author
    userid = ctx.author.id
    canrun = None
    if channel1available == True:
        channel1available = False
        channel = client.get_channel(764017189279236096)
        role1 = 'ships and fleets 1' #role to add
        await user.add_roles(discord.utils.get(user.guild.roles, name=role1))
        canrun = True
    elif channel2available == True:
        channel2available = False
        channel = client.get_channel(764017265125228544)
        role2 = 'ships and fleets 2' #role to add
        await user.add_roles(discord.utils.get(user.guild.roles, name=role2))
        canrun = True
    elif channel3available == True:
        channel3available = False
        channel = client.get_channel(764017300424622100)
        role3 = 'ships and fleets 3' #role to add
        await user.add_roles(discord.utils.get(user.guild.roles, name=role3))
        canrun = True
    else:
        await ctx.send("All channels are currently unavailable. Please try again later.")
    while canrun == True:
        await channel.send("<@{}>, please move here.".format(userid))
        await channel.send("What would you like to create? (nation/ship/fleet)")
        try:
            await client.wait_for('message', timeout=60)
        except asyncio.TimeoutError:
            await channel.send(embed=embedtimeout)
            canrun = False
        else:
            async for message in channel.history(limit=1):
                if message.content == "nation" and message.author == user:
                    await channel.send("What is the name of the nation?")
                    try:
                        await client.wait_for('message', timeout=60)
                    except asyncio.TimeoutError:
                        await channel.send(embed=embedtimeout)
                        canrun = False
                    else:
                        async for message in channel.history(limit=1):
                            if message.author == user:
                                nationname = message.content
                                # check if nation exists: if false, proceed
                                if keys_exists(datadic, nationname) == False:
                                    datadic.update({
                                        nationname:
                                            {"userid":userid, 
                                            'ships':{},  
                                            'fleets':{}, 
                                            'location':{}
                                            }
                                            }
                                        )
                                    with open("data.txt", "w") as outfile:
                                        json.dump(datadic, outfile)
                                    await channel.send("{} has been created.".format(nationname))
                                    canrun = False
                                else:
                                    await channel.send("A nation with this name already exists.")
                                    canrun = False
                if message.content == "ship" and message.author == user:
                    with open("data.txt") as json_file:
                        datadic = json.load(json_file)
                    await channel.send("Please enter the name of the nation that you want to create the ship in.")
                    try:
                        await client.wait_for('message', timeout=60)
                    except asyncio.TimeoutError:
                        await channel.send(embed=embedtimeout)
                        canrun = False
                    else:
                        async for message in channel.history(limit=1):
                            nationnamecheck = message.content
                            # if nation exists: true, proceed
                            if keys_exists(datadic, nationnamecheck) == True and message.author == user and datadic[nationnamecheck]["userid"] == userid:
                                await channel.send("Please enter the name of the ship.")
                                try:
                                    await client.wait_for('message', timeout=60)
                                except asyncio.TimeoutError:
                                    await channel.send(embed=embedtimeout)
                                    canrun = False
                                else:
                                    async for message in channel.history(limit=1):
                                        shipname = message.content
                                        # if ship exists, false: proceed
                                        if keys_exists(datadic, nationnamecheck, "ships", shipname) == False and message.author == user:
                                            await channel.send("Ship's name has been set to {}".format(shipname))
                                            await channel.send("Please choose a class.")
                                            embedclasslist = discord.Embed(title='List of Ship Classes', description='Please enter the number next to the class of your choice.')
                                            embedclasslist.add_field(name="Classifications", value="""1: Striker
2: Corvette
3: Frigate
4: Destroyer
5: Cruiser
6: Battlecruiser
7: Battleship
8: Light Carrier
9: Dreadnaught
10: Carrier
11: Battlesphere
12: Battleglobe""", inline=False)
                                            await channel.send(embed=embedclasslist)
                                            try:
                                                await client.wait_for('message', timeout=60)
                                            except asyncio.TimeoutError:
                                                await channel.send(embed=embedtimeout)
                                                canrun = False
                                            else:
                                                async for message in channel.history(limit=1):
                                                    classchoice = message.content
                                                    if message.author == user:
                                                        if classchoice == "1": 
                                                            shipclass = 'Striker'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"striker", 
                                                                            'maxpoints':30, 
                                                                            'healthmod':0.4, 
                                                                            'speedmod':(((- (1/30) * math.log(30) + 2000 * (5 / 30)) - 100) / 100) + 1, 
                                                                            'defencemod':0.5, 
                                                                            'closemod':2, 
                                                                            'mediummod':0, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to striker.".format(shipname))
                                                        if classchoice == "2": 
                                                            shipclass = 'Corvette'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"corvette", 
                                                                            'maxpoints':60, 
                                                                            'healthmod':0.5, 
                                                                            'speedmod':(((- (1/60) * math.log(60) + 2000 * (5 / 60)) - 100) / 100) + 1, 
                                                                            'defencemod':0.7, 
                                                                            'closemod':1.8, 
                                                                            'mediummod':0, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to corvette.".format(shipname))
                                                        if classchoice == "3": 
                                                            shipclass = 'Frigate'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"frgiate", 
                                                                            'maxpoints':80, 
                                                                            'healthmod':0.7, 
                                                                            'speedmod':(((- (1/80) * math.log(80) + 2000 * (5 / 80)) - 100) / 100) + 1, 
                                                                            'defencemod':0.9, 
                                                                            'closemod':1.7, 
                                                                            'mediummod':0, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to frigate.".format(shipname))
                                                        if classchoice == "4": 
                                                            shipclass = 'Destroyer'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"destroyer", 
                                                                            'maxpoints':140, 
                                                                            'healthmod':0.8, 
                                                                            'speedmod':(((- (1/140) * math.log(140) + 2000 * (5 / 140)) - 100) / 100) + 1, 
                                                                            'defencemod':1, 
                                                                            'closemod':1.6, 
                                                                            'mediummod':0.7, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to destroyer.".format(shipname))
                                                        if classchoice == "5":
                                                            shipclass = 'Cruiser'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"cruiser", 
                                                                            'maxpoints':310, 
                                                                            'healthmod':1, 
                                                                            'speedmod':(((- (1/310) * math.log(310) + 2000 * (5 / 310)) - 100) / 100) + 1, 
                                                                            'defencemod':1.2, 
                                                                            'closemod':1.4, 
                                                                            'mediummod':1, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to cruiser.".format(shipname))
                                                        if classchoice == "6": 
                                                            shipclass = 'Battlecruiser'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"battlecruiser", 
                                                                            'maxpoints':970, 
                                                                            'healthmod':1.1, 
                                                                            'speedmod':(((- (1/970) * math.log(970) + 2000 * (5 / 970)) - 100) / 100) + 1, 
                                                                            'defencemod':1.4, 
                                                                            'closemod':1.3, 
                                                                            'mediummod':1.3, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to battlecruiser.".format(shipname))
                                                        if classchoice == "7": 
                                                            shipclass = 'Battleship'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"battleship", 
                                                                            'maxpoints':3760, 
                                                                            'healthmod':1.15, 
                                                                            'speedmod':(((- (1/3760) * math.log(3760) + 2000 * (5 / 3760)) - 100) / 100) + 1, 
                                                                            'defencemod':1.5, 
                                                                            'closemod':1.2,  
                                                                            'mediummod':1.4, 
                                                                            'longmod':0.9, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to battleship.".format(shipname))
                                                        if classchoice == "8": 
                                                            shipclass = 'Lightcarrier'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"lightcarrier", 
                                                                            'maxpoints':9380, 
                                                                            'healthmod':1.2, 
                                                                            'speedmod':(((- (1/9380) * math.log(9380) + 2000 * (5 / 9380)) - 100) / 100) + 1, 
                                                                            'defencemod':2, 
                                                                            'closemod':0.6, 
                                                                            'mediummod':0.6, 
                                                                            'longmod':0.6, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to lightcarrier.".format(shipname))
                                                        if classchoice == "9": 
                                                            shipclass = 'Dreadnaught'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"dreadnaught", 
                                                                            'maxpoints':11250, 
                                                                            'healthmod':0.5, 
                                                                            'speedmod':(((- (1/11250) * math.log(11250) + 2000 * (5 / 11250)) - 100) / 100) + 1, 
                                                                            'defencemod':1.7, 
                                                                            'closemod':1, 
                                                                            'mediummod':1.3, 
                                                                            'longmod':1.3, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to dreadnaught.".format(shipname))
                                                        if classchoice == "10": 
                                                            shipclass = 'Carrier'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"carrier", 
                                                                            'maxpoints':11880, 
                                                                            'healthmod':1.35, 
                                                                            'speedmod':(((- (1/11880) * math.log(11880) + 2000 * (5 / 11880)) - 100) / 100) + 1, 
                                                                            'defencemod':2,  
                                                                            'closemod':0.6, 
                                                                            'mediummod':0.6, 
                                                                            'longmod':0.6, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to carrier.".format(shipname))
                                                        if classchoice == "11": 
                                                            shipclass = 'Battlesphere'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"battlesphere", 
                                                                            'maxpoints':175000, 
                                                                            'healthmod':1.4, 
                                                                            'speedmod':(((- (1/175000) * math.log(175000) + 2000 * (5 / 175000)) - 100) / 100) + 1, 
                                                                            'defencemod':1.9, 
                                                                            'closemod':1.8, 
                                                                            'mediummod':1.5, 
                                                                            'longmod':1., 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to battlesphere.".format(shipname))
                                                        if classchoice == "12":
                                                            shipclass = 'Battleglobe'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':'battleglobe', 
                                                                            'maxpoints':9000000000, 
                                                                            'healthmod':1.5, 
                                                                            'speedmod':(((- (1/9000000000) * math.log(9000000000) + 2000 * (5 / 9000000000)) - 100) / 100) + 1, 
                                                                            'defencemod':2, 
                                                                            'closemod':1, 
                                                                            'mediummod':1.7, 
                                                                            'longmod':2, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to battleglobe.".format(shipname))
                                                        if int(classchoice) > 12:
                                                            await channel.send("That is not a valid option.")
                                                            canrun = False
                                                    with open("data.txt", "w") as outfile:
                                                        json.dump(datadic, outfile)
                                                    with open("data.txt") as json_file:
                                                        datadic = json.load(json_file)
                                                    maxpoints = datadic[nationnamecheck]['ships'][shipname]['maxpoints']
                                                    spent = 0
                                                    remain = int(maxpoints)
                                                    await channel.send("You have {} points left.".format(remain))
                                                    await channel.send("Please enter the amount of points you wish to spend on health")
                                                    embedhealthallo = discord.Embed(title='Health', description='Points must not exceed remaining points.')
                                                    embedhealthallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: -
Defense Points: -
Speed Points: -
Close Attack Points: -
Medium Attack Points: -
Long Attack Points: -""".format(remain, maxpoints), inline=False)
                                                    await channel.send(embed=embedhealthallo)
                                                    try:
                                                        await client.wait_for('message', timeout=60)
                                                    except asyncio.TimeoutError:
                                                        await channel.send(embed=embedtimeout)
                                                        canrun = False
                                                    else:
                                                        async for message in channel.history(limit=1):
                                                            if message.author == user:
                                                                health = int(message.content)
                                                                if health > remain:
                                                                    await channel.send("You do not have that many points.")
                                                                else:
                                                                    spent = health
                                                                    remain = int(maxpoints) - spent
                                                                    await channel.send("You have spent {} points on health. You have {} points left.".format(health, remain))
                                                                    await channel.send("Please enter the amount of points you wish to spend on defense.")
                                                                    embeddefenseallo = discord.Embed(title='Defense', description='Points must not exceed remaining points.')
                                                                    embeddefenseallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: {}
Defense Points: -
Speed Points: -
Close Attack Points: -
Medium Attack Points: -
Long Attack Points: -""".format(remain, maxpoints, health), inline=False)
                                                                    await channel.send(embed=embeddefenseallo)
                                                                    try:
                                                                        await client.wait_for('message', timeout=60)
                                                                    except asyncio.TimeoutError:
                                                                        await channel.send(embed=embedtimeout)
                                                                        canrun = False
                                                                    else:
                                                                        async for message in channel.history(limit=1):
                                                                            if message.author == user:
                                                                                defense = int(message.content)
                                                                                if defense > remain:
                                                                                    await channel.send("You do not have that many ponts.")
                                                                                else:
                                                                                    spent = health + defense
                                                                                    remain = int(maxpoints) - spent
                                                                                    await channel.send("You have spent {} points on defense. You have {} points left.".format(defense, remain))
                                                                                    await channel.send("Please enter the amount of points you wish to spend on speed.")
                                                                                    embedspeedallo = discord.Embed(title='Speed', description='Points must not exceed remaining points.')
                                                                                    embedspeedallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: {}
Defense Points: {}
Speed Points: -
Close Attack Points: -
Medium Attack Points: -
Long Attack Points: -""".format(remain, maxpoints, health, defense), inline=False)
                                                                                    await channel.send(embed=embedspeedallo)
                                                                                    try:
                                                                                        await client.wait_for('message', timeout=60)
                                                                                    except asyncio.TimeoutError:
                                                                                        await channel.send(embed=embedtimeout)
                                                                                        canrun = False
                                                                                    else:
                                                                                        async for message in channel.history(limit=1):
                                                                                            if message.author == user:
                                                                                                speed = int(message.content)
                                                                                                if speed > remain:
                                                                                                    await channel.send("You do not have that many ponts.")
                                                                                                else:
                                                                                                    spent = health + defense + speed
                                                                                                    remain = int(maxpoints) - spent
                                                                                                    await channel.send("You have spent {} points on speed. You have {} points left.".format(speed, remain))
                                                                                                    await channel.send("Please enter the amount of points you wish to spend on close attack.")
                                                                                                    embedcloseallo = discord.Embed(title='Close Attack', description='Points must not exceed remaining points.')
                                                                                                    embedcloseallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: {}
Defense Points: {}
Speed Points: {}
Close Attack Points: -
Medium Attack Points: -
Long Attack Points: -""".format(remain, maxpoints, health, defense, speed), inline=False)
                                                                                                    await channel.send(embed=embedcloseallo)
                                                                                                    try:
                                                                                                        await client.wait_for('message', timeout=60)
                                                                                                    except asyncio.TimeoutError:
                                                                                                        await channel.send(embed=embedtimeout)
                                                                                                        canrun = False
                                                                                                    else:
                                                                                                        async for message in channel.history(limit=1):
                                                                                                            if message.author == user:
                                                                                                                closeatt = int(message.content)
                                                                                                                if closeatt > remain:
                                                                                                                    await channel.send("You do not have that many ponts.")
                                                                                                                else:
                                                                                                                    spent = health + defense + speed + closeatt
                                                                                                                    remain = int(maxpoints) - spent
                                                                                                                    await channel.send("You have spent {} points on close attack. You have {} points left.".format(closeatt, remain))
                                                                                                                    await channel.send("Please enter the amount of points you wish to spend on medium attack.")
                                                                                                                    embedmediumallo = discord.Embed(title='Medium Attack', description='Points must not exceed remaining points.')
                                                                                                                    embedmediumallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: {}
Defense Points: {}
Speed Points: {}
Close Attack Points: {}
Medium Attack Points: -
Long Attack Points: -""".format(remain, maxpoints, health, defense, speed, closeatt), inline=False)
                                                                                                                    await channel.send(embed=embedmediumallo)
                                                                                                                    try:
                                                                                                                        await client.wait_for('message', timeout=60)
                                                                                                                    except asyncio.TimeoutError:
                                                                                                                        await channel.send(embed=embedtimeout)
                                                                                                                        canrun = False
                                                                                                                    else:
                                                                                                                        async for message in channel.history(limit=1):
                                                                                                                            if message.author == user:
                                                                                                                                medatt = int(message.content)
                                                                                                                                if medatt > remain:
                                                                                                                                    await channel.send("You do not have that many ponts.")
                                                                                                                                else:
                                                                                                                                    spent = health + defense + speed + closeatt + medatt
                                                                                                                                    remain = int(maxpoints) - spent
                                                                                                                                    await channel.send("You have spent {} points on medium attack. You have {} points left.".format(medatt, remain))
                                                                                                                                    await channel.send("Please enter the amount of points you wish to spend on long attack.")
                                                                                                                                    embedlongallo = discord.Embed(title='Medium Attack', description='Points must not exceed remaining points.')
                                                                                                                                    embedlongallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: {}
Defense Points: {}
Speed Points: {}
Close Attack Points: {}
Medium Attack Points: {}
Long Attack Points: -""".format(remain, maxpoints, health, defense, speed, closeatt, medatt), inline=False)
                                                                                                                                    await channel.send(embed=embedlongallo)
                                                                                                                                    try:
                                                                                                                                        await client.wait_for('message', timeout=60)
                                                                                                                                    except asyncio.TimeoutError:
                                                                                                                                        await channel.send(embed=embedtimeout)
                                                                                                                                        canrun = False
                                                                                                                                    else:
                                                                                                                                        async for message in channel.history(limit=1):
                                                                                                                                            if message.author == user:
                                                                                                                                                longatt = int(message.content)
                                                                                                                                                if longatt > remain:
                                                                                                                                                    await channel.send("You do not have that many ponts.")
                                                                                                                                                else:
                                                                                                                                                    spent = health + defense + speed + closeatt + medatt + longatt
                                                                                                                                                    remain = int(maxpoints) - spent
                                                                                                                                                    await channel.send("You have spent {} points on long attack.".format(longatt))
                                                                                                                                                    healthmod = datadic[nationnamecheck]['ships'][shipname]['healthmod']
                                                                                                                                                    defencemod = datadic[nationnamecheck]['ships'][shipname]['defencemod']
                                                                                                                                                    speedmod = datadic[nationnamecheck]['ships'][shipname]['speedmod']
                                                                                                                                                    closemod = datadic[nationnamecheck]['ships'][shipname]['closemod']
                                                                                                                                                    medmod = datadic[nationnamecheck]['ships'][shipname]['mediummod']
                                                                                                                                                    longmod = datadic[nationnamecheck]['ships'][shipname]['longmod']
                                                                                                                                                    datadic.update({
                                                                                                                                                        userid:
                                                                                                                                                            {nationnamecheck:
                                                                                                                                                                {'ships':
                                                                                                                                                                    {
                                                                                                                                                                    shipname:
                                                                                                                                                                        {
                                                                                                                                                                        "shipclass":shipclass, 
                                                                                                                                                                        'maxpoints':maxpoints, 
                                                                                                                                                                        'healthmod':healthmod, 
                                                                                                                                                                        'speedmod':speedmod, 
                                                                                                                                                                        'defencemod':defencemod, 
                                                                                                                                                                        'closemod':closemod, 
                                                                                                                                                                        'mediummod':medmod, 
                                                                                                                                                                        'longmod':longmod, 
                                                                                                                                                                        "health":(health+1)*healthmod, 
                                                                                                                                                                        "defense":(defense+1)*defencemod, 
                                                                                                                                                                        "speed":(speed+1)*speedmod, 
                                                                                                                                                                        "close":(closeatt+1)*closemod, 
                                                                                                                                                                        "med":(medatt+1)*medmod, 
                                                                                                                                                                        "long":(longatt+1)*longmod, 
                                                                                                                                                                        }
                                                                                                                                                                    }
                                                                                                                                                                }
                                                                                                                                                            }
                                                                                                                                                        })
                                                                                                                                                    with open("data.txt", "w") as outfile:
                                                                                                                                                        json.dump(datadic, outfile)
                                                                                                                                                    await channel.send("Ship successfuly created.")
                                                                                                                                                    embedsummary = discord.Embed(title='Summary', description='{}'.format(shipname))
                                                                                                                                                    embedsummary.add_field(name='Properties', value="""Nation: {}
Class: {}
Name: {}""".format(nationnamecheck, shipclass, shipname), inline=False)
                                                                                                                                                    healthscore = datadic[nationnamecheck]['ships'][shipname]['health']
                                                                                                                                                    defensescore = datadic[nationnamecheck]['ships'][shipname]['defense']
                                                                                                                                                    speedscore = datadic[nationnamecheck]['ships'][shipname]['speed']
                                                                                                                                                    closescore = datadic[nationnamecheck]['ships'][shipname]['close']
                                                                                                                                                    medscore = datadic[nationnamecheck]['ships'][shipname]['med']
                                                                                                                                                    longscore = datadic[nationnamecheck]['ships'][shipname]['long']

                                                                                                                                                    embedsummary.add_field(name='Stats', value="""Health: {}
Defense: {}
Speed: {}
Close Attack: {}
Medium Attack: {}
Long Attack: {}""".format(healthscore, defensescore, speedscore, closescore, medscore, longscore), inline=False)
                                                                                                                                                    await channel.send(embed=embedsummary)
                                                                                                                                                    canrun = False
                                        else:
                                            await channel.send("You have already created a ship with the same name.")
                                            canrun = False
                            else:
                                await channel.send("You do not own that nation.")
                                canrun = False

                if message.content == "fleet" and message.author == user:
                    return # do this
                else:
                    if message.author == user:
                        canrun = False
    if canrun == False:
        if channel == client.get_channel(764017189279236096):
            channel1available = True
            role4 = 'ships and fleets 1' #role to add
            await user.remove_roles(discord.utils.get(user.guild.roles, name=role4))
        elif channel == client.get_channel(764017265125228544):
            channel2available = True
            role5 = 'ships and fleets 2' #role to add
            await user.remove_roles(discord.utils.get(user.guild.roles, name=role5))
        elif channel == client.get_channel(764017300424622100):
            channel3available = True
            role6 = 'ships and fleets 3' #role to add
            await user.remove_roles(discord.utils.get(user.guild.roles, name=role6))

@client.command(name='edit')
async def edit(ctx):
    global channel1available
    global channel2available
    global channel3available
    user = ctx.message.author
    userid = ctx.author.id
    if channel1available == True:
        channel1available = False
        channel = client.get_channel(764017189279236096)
        role1 = 'ships and fleets 1' #role to add
        await user.add_roles(discord.utils.get(user.guild.roles, name=role1))
        canrun = True
    elif channel2available == True:
        channel2available = False
        channel = client.get_channel(764017265125228544)
        role2 = 'ships and fleets 2' #role to add
        await user.add_roles(discord.utils.get(user.guild.roles, name=role2))
        canrun = True
    elif channel3available == True:
        channel3available = False
        channel = client.get_channel(764017300424622100)
        role3 = 'ships and fleets 3' #role to add
        await user.add_roles(discord.utils.get(user.guild.roles, name=role3))
        canrun = True
    else:
        await ctx.send("All channels are currently unavailable. Please try again later.")
    if canrun == True:
        await channel.send("<@{}>, please move here.".format(userid))
        await channel.send("What do you want to edit? (ship/fleet)")
        try:
            await client.wait_for('message', timeout=60)
        except asyncio.TimeoutError:
            await channel.send(embed=embedtimeout)
            canrun = False
        else:
            async for message in channel.history(limit=1):
                if message.author == user and message.content=="ship":
                    await channel.send("Please enter the name of the nation that has the ship you want to edit.")
                    try:
                        await client.wait_for('message', timeout=60)
                    except asyncio.TimeoutError:
                        await channel.send(embed=embedtimeout)
                        canrun = False
                    else:
                        async for message in channel.history(limit=1):
                            nationnamecheck = message.content
                            # if nation exists: true, proceed
                            if keys_exists(datadic, nationnamecheck) == True and message.author == user and datadic[nationnamecheck]["userid"] == userid:
                                await channel.send("Please enter the name of the ship.")
                                try:
                                    await client.wait_for('message', timeout=60)
                                except asyncio.TimeoutError:
                                    await channel.send(embed=embedtimeout)
                                    canrun = False
                                else:
                                    async for message in channel.history(limit=1):
                                        shipname = message.content
                                        # if ship exists, true: proceed
                                        if keys_exists(datadic, nationnamecheck, 'ships', shipname) == True and message.author == user:
                                            currentclass = datadic[nationnamecheck]['ships'][shipname]['shipclass']
                                            await channel.send("Your current class is {}".format(currentclass))
                                            await channel.send("Please choose a class.")
                                            embedclasslist = discord.Embed(title='List of Ship Classes', description='Please enter the number next to the class of your choice.')
                                            embedclasslist.add_field(name="Classifications", value="""1: Striker
2: Corvette
3: Frigate
4: Destroyer
5: Cruiser
6: Battlecruiser
7: Battleship
8: Light Carrier
9: Dreadnaught
10: Carrier
11: Battlesphere
12: Battleglobe""", inline=False)
                                            await channel.send(embed=embedclasslist)
                                            try:
                                                await client.wait_for('message', timeout=60)
                                            except asyncio.TimeoutError:
                                                await channel.send(embed=embedtimeout)
                                                canrun = False
                                            else:
                                                async for message in channel.history(limit=1):
                                                    classchoice = message.content
                                                    if message.author == user:
                                                        if classchoice == "1": 
                                                            shipclass = 'Striker'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"striker", 
                                                                            'maxpoints':30, 
                                                                            'healthmod':0.4, 
                                                                            'speedmod':(((- (1/30) * math.log(30) + 2000 * (5 / 30)) - 100) / 100) + 1, 
                                                                            'defencemod':0.5, 
                                                                            'closemod':2, 
                                                                            'mediummod':0, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to striker.".format(shipname))
                                                        if classchoice == "2": 
                                                            shipclass = 'Corvette'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"corvette", 
                                                                            'maxpoints':60, 
                                                                            'healthmod':0.5, 
                                                                            'speedmod':(((- (1/60) * math.log(60) + 2000 * (5 / 60)) - 100) / 100) + 1, 
                                                                            'defencemod':0.7, 
                                                                            'closemod':1.8, 
                                                                            'mediummod':0, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to corvette.".format(shipname))
                                                        if classchoice == "3": 
                                                            shipclass = 'Frigate'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"frgiate", 
                                                                            'maxpoints':80, 
                                                                            'healthmod':0.7, 
                                                                            'speedmod':(((- (1/80) * math.log(80) + 2000 * (5 / 80)) - 100) / 100) + 1, 
                                                                            'defencemod':0.9, 
                                                                            'closemod':1.7, 
                                                                            'mediummod':0, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to frigate.".format(shipname))
                                                        if classchoice == "4": 
                                                            shipclass = 'Destroyer'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"destroyer", 
                                                                            'maxpoints':140, 
                                                                            'healthmod':0.8, 
                                                                            'speedmod':(((- (1/140) * math.log(140) + 2000 * (5 / 140)) - 100) / 100) + 1, 
                                                                            'defencemod':1, 
                                                                            'closemod':1.6, 
                                                                            'mediummod':0.7, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to destroyer.".format(shipname))
                                                        if classchoice == "5":
                                                            shipclass = 'Cruiser'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"cruiser", 
                                                                            'maxpoints':310, 
                                                                            'healthmod':1, 
                                                                            'speedmod':(((- (1/310) * math.log(310) + 2000 * (5 / 310)) - 100) / 100) + 1, 
                                                                            'defencemod':1.2, 
                                                                            'closemod':1.4, 
                                                                            'mediummod':1, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to cruiser.".format(shipname))
                                                        if classchoice == "6": 
                                                            shipclass = 'Battlecruiser'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"battlecruiser", 
                                                                            'maxpoints':970, 
                                                                            'healthmod':1.1, 
                                                                            'speedmod':(((- (1/970) * math.log(970) + 2000 * (5 / 970)) - 100) / 100) + 1, 
                                                                            'defencemod':1.4, 
                                                                            'closemod':1.3, 
                                                                            'mediummod':1.3, 
                                                                            'longmod':0, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to battlecruiser.".format(shipname))
                                                        if classchoice == "7": 
                                                            shipclass = 'Battleship'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"battleship", 
                                                                            'maxpoints':3760, 
                                                                            'healthmod':1.15, 
                                                                            'speedmod':(((- (1/3760) * math.log(3760) + 2000 * (5 / 3760)) - 100) / 100) + 1, 
                                                                            'defencemod':1.5, 
                                                                            'closemod':1.2,  
                                                                            'mediummod':1.4, 
                                                                            'longmod':0.9, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to battleship.".format(shipname))
                                                        if classchoice == "8": 
                                                            shipclass = 'Lightcarrier'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"lightcarrier", 
                                                                            'maxpoints':9380, 
                                                                            'healthmod':1.2, 
                                                                            'speedmod':(((- (1/9380) * math.log(9380) + 2000 * (5 / 9380)) - 100) / 100) + 1, 
                                                                            'defencemod':2, 
                                                                            'closemod':0.6, 
                                                                            'mediummod':0.6, 
                                                                            'longmod':0.6, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to lightcarrier.".format(shipname))
                                                        if classchoice == "9": 
                                                            shipclass = 'Dreadnaught'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"dreadnaught", 
                                                                            'maxpoints':11250, 
                                                                            'healthmod':0.5, 
                                                                            'speedmod':(((- (1/11250) * math.log(11250) + 2000 * (5 / 11250)) - 100) / 100) + 1, 
                                                                            'defencemod':1.7, 
                                                                            'closemod':1, 
                                                                            'mediummod':1.3, 
                                                                            'longmod':1.3, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to dreadnaught.".format(shipname))
                                                        if classchoice == "10": 
                                                            shipclass = 'Carrier'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"carrier", 
                                                                            'maxpoints':11880, 
                                                                            'healthmod':1.35, 
                                                                            'speedmod':(((- (1/11880) * math.log(11880) + 2000 * (5 / 11880)) - 100) / 100) + 1, 
                                                                            'defencemod':2,  
                                                                            'closemod':0.6, 
                                                                            'mediummod':0.6, 
                                                                            'longmod':0.6, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to carrier.".format(shipname))
                                                        if classchoice == "11": 
                                                            shipclass = 'Battlesphere'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':"battlesphere", 
                                                                            'maxpoints':175000, 
                                                                            'healthmod':1.4, 
                                                                            'speedmod':(((- (1/175000) * math.log(175000) + 2000 * (5 / 175000)) - 100) / 100) + 1, 
                                                                            'defencemod':1.9, 
                                                                            'closemod':1.8, 
                                                                            'mediummod':1.5, 
                                                                            'longmod':1.5, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to battlesphere.".format(shipname))
                                                        if classchoice == "12":
                                                            shipclass = 'Battleglobe'
                                                            datadic.update({
                                                                nationnamecheck:
                                                                    {'ships':
                                                                        {
                                                                        shipname:
                                                                            { 
                                                                            'shipclass':'battleglobe', 
                                                                            'maxpoints':9000000000, 
                                                                            'healthmod':1.5, 
                                                                            'speedmod':(((- (1/9000000000) * math.log(9000000000) + 2000 * (5 / 9000000000)) - 100) / 100) + 1, 
                                                                            'defencemod':2, 
                                                                            'closemod':1, 
                                                                            'mediummod':1.7, 
                                                                            'longmod':2, 
                                                                            'health':0, 
                                                                            'defense':0, 
                                                                            'speed':0, 
                                                                            'close':0, 
                                                                            'med':0, 
                                                                            'long':0, 
                                                                            }
                                                                        }
                                                                        }
                                                                    }
                                                                )
                                                            await channel.send("{}'s class has been set to battleglobe.".format(shipname))

                                                        if int(classchoice) > 12:
                                                            await channel.send("That is not a valid option.")
                                                            canrun = False
                                                    with open("data.txt", "w") as outfile:
                                                        json.dump(datadic, outfile)
                                                    with open("data.txt") as json_file:
                                                        datadic = json.load(json_file)
                                                    maxpoints = datadic[nationnamecheck]['ships'][shipname]['maxpoints']
                                                    spent = 0
                                                    remain = int(maxpoints)
                                                    healthmodc = datadic[nationnamecheck]['ships'][shipname]['healthmod']
                                                    defencemodc = datadic[nationnamecheck]['ships'][shipname]['defencemod']
                                                    speedmodc = datadic[nationnamecheck]['ships'][shipname]['speedmod']
                                                    closemodc = datadic[nationnamecheck]['ships'][shipname]['closemod']
                                                    medmodc = datadic[nationnamecheck]['ships'][shipname]['mediummod']
                                                    longmodc = datadic[nationnamecheck]['ships'][shipname]['longmod']

                                                    healthscorec = datadic[nationnamecheck]['ships'][shipname]['health']
                                                    defensescorec = datadic[nationnamecheck]['ships'][shipname]['defense']
                                                    speedscorec = datadic[nationnamecheck]['ships'][shipname]['speed']
                                                    closescorec = datadic[nationnamecheck]['ships'][shipname]['close']
                                                    medscorec = datadic[nationnamecheck]['ships'][shipname]['med']
                                                    longscorec = datadic[nationnamecheck]['ships'][shipname]['long']

                                                    healthpoint = (int(healthscorec) / int(healthmodc)) - 1
                                                    defensepoint = (int(defensescorec) / int(defencemodc)) - 1
                                                    speedpoint = (int(speedscorec) / int(speedmodc)) - 1
                                                    closepoint = (int(closescorec) / int(closemodc)) - 1
                                                    medpoint = (int(medscorec) / int(medmodc)) - 1
                                                    longpoint = (int(longscorec) / int(longmodc)) - 1

                                                    embedcurrentpoints = discord.Embed(title = 'Current Points')
                                                    embedcurrentpoints.add_field(name='Stats', value = """Health: {}
Defense: {}
Speed: {}
Close Attack: {}
Medium Attack: {}
Long Attack: {}""".format(healthpoint, defensepoint, speedpoint, closepoint, medpoint, longpoint), inline=False)
                                                    await channel.send(embed=embedcurrentpoints)
                                                    await channel.send("You have {} points left.".format(remain))
                                                    await channel.send("Please enter the amount of points you wish to spend on health")
                                                    embedhealthallo = discord.Embed(title='Health', description='Points must not exceed remaining points.')
                                                    embedhealthallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: -
Defense Points: -
Speed Points: -
Close Attack Points: -
Medium Attack Points: -
Long Attack Points: -""".format(remain, maxpoints), inline=False)
                                                    await channel.send(embed=embedcurrentpoints)
                                                    try:
                                                        await client.wait_for('message', timeout=60)
                                                    except asyncio.TimeoutError:
                                                        await channel.send(embed=embedtimeout)
                                                        canrun = False
                                                    else:
                                                        async for message in channel.history(limit=1):
                                                            if message.author == user:
                                                                health = int(message.content)
                                                                if health > remain:
                                                                    await channel.send("You do not have that many points.")
                                                                else:
                                                                    spent = health
                                                                    remain = int(maxpoints) - spent
                                                                    await channel.send("You have spent {} points on health. You have {} points left.".format(health, remain))
                                                                    await channel.send("Please enter the amount of points you wish to spend on defense.")
                                                                    embeddefenseallo = discord.Embed(title='Defense', description='Points must not exceed remaining points.')
                                                                    embeddefenseallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: {}
Defense Points: -
Speed Points: -
Close Attack Points: -
Medium Attack Points: -
Long Attack Points: -""".format(remain, maxpoints, health), inline=False)
                                                                    await channel.send(embed=embeddefenseallo)
                                                                    try:
                                                                        await client.wait_for('message', timeout=60)
                                                                    except asyncio.TimeoutError:
                                                                        await channel.send(embed=embedtimeout)
                                                                        canrun = False
                                                                    else:
                                                                        async for message in channel.history(limit=1):
                                                                            if message.author == user:
                                                                                defense = int(message.content)
                                                                                if defense > remain:
                                                                                    await channel.send("You do not have that many ponts.")
                                                                                else:
                                                                                    spent = health + defense
                                                                                    remain = int(maxpoints) - spent
                                                                                    await channel.send("You have spent {} points on defense. You have {} points left.".format(defense, remain))
                                                                                    await channel.send("Please enter the amount of points you wish to spend on speed.")
                                                                                    embedspeedallo = discord.Embed(title='Speed', description='Points must not exceed remaining points.')
                                                                                    embedspeedallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: {}
Defense Points: {}
Speed Points: -
Close Attack Points: -
Medium Attack Points: -
Long Attack Points: -""".format(remain, maxpoints, health, defense), inline=False)
                                                                                    await channel.send(embed=embedspeedallo)
                                                                                    try:
                                                                                        await client.wait_for('message', timeout=60)
                                                                                    except asyncio.TimeoutError:
                                                                                        await channel.send(embed=embedtimeout)
                                                                                        canrun = False
                                                                                    else:
                                                                                        async for message in channel.history(limit=1):
                                                                                            if message.author == user:
                                                                                                speed = int(message.content)
                                                                                                if speed > remain:
                                                                                                    await channel.send("You do not have that many ponts.")
                                                                                                else:
                                                                                                    spent = health + defense + speed
                                                                                                    remain = int(maxpoints) - spent
                                                                                                    await channel.send("You have spent {} points on speed. You have {} points left.".format(speed, remain))
                                                                                                    await channel.send("Please enter the amount of points you wish to spend on close attack.")
                                                                                                    embedcloseallo = discord.Embed(title='Close Attack', description='Points must not exceed remaining points.')
                                                                                                    embedcloseallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: {}
Defense Points: {}
Speed Points: {}
Close Attack Points: -
Medium Attack Points: -
Long Attack Points: -""".format(remain, maxpoints, health, defense, speed), inline=False)
                                                                                                    await channel.send(embed=embedcloseallo)
                                                                                                    try:
                                                                                                        await client.wait_for('message', timeout=60)
                                                                                                    except asyncio.TimeoutError:
                                                                                                        await channel.send(embed=embedtimeout)
                                                                                                        canrun = False
                                                                                                    else:
                                                                                                        async for message in channel.history(limit=1):
                                                                                                            if message.author == user:
                                                                                                                closeatt = int(message.content)
                                                                                                                if closeatt > remain:
                                                                                                                    await channel.send("You do not have that many ponts.")
                                                                                                                else:
                                                                                                                    spent = health + defense + speed + closeatt
                                                                                                                    remain = int(maxpoints) - spent
                                                                                                                    await channel.send("You have spent {} points on close attack. You have {} points left.".format(closeatt, remain))
                                                                                                                    await channel.send("Please enter the amount of points you wish to spend on medium attack.")
                                                                                                                    embedmediumallo = discord.Embed(title='Medium Attack', description='Points must not exceed remaining points.')
                                                                                                                    embedmediumallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: {}
Defense Points: {}
Speed Points: {}
Close Attack Points: {}
Medium Attack Points: -
Long Attack Points: -""".format(remain, maxpoints, health, defense, speed, closeatt), inline=False)
                                                                                                                    await channel.send(embed=embedmediumallo)
                                                                                                                    try:
                                                                                                                        await client.wait_for('message', timeout=60)
                                                                                                                    except asyncio.TimeoutError:
                                                                                                                        await channel.send(embed=embedtimeout)
                                                                                                                        canrun = False
                                                                                                                    else:
                                                                                                                        async for message in channel.history(limit=1):
                                                                                                                            if message.author == user:
                                                                                                                                medatt = int(message.content)
                                                                                                                                if medatt > remain:
                                                                                                                                    await channel.send("You do not have that many ponts.")
                                                                                                                                else:
                                                                                                                                    spent = health + defense + speed + closeatt + medatt
                                                                                                                                    remain = int(maxpoints) - spent
                                                                                                                                    await channel.send("You have spent {} points on medium attack. You have {} points left.".format(medatt, remain))
                                                                                                                                    await channel.send("Please enter the amount of points you wish to spend on long attack.")
                                                                                                                                    embedlongallo = discord.Embed(title='Medium Attack', description='Points must not exceed remaining points.')
                                                                                                                                    embedlongallo.add_field(name="Stats", value="""Remaining Points: {}
Max Points: {}
Health Points: {}
Defense Points: {}
Speed Points: {}
Close Attack Points: {}
Medium Attack Points: {}
Long Attack Points: -""".format(remain, maxpoints, health, defense, speed, closeatt, medatt), inline=False)
                                                                                                                                    await channel.send(embed=embedlongallo)
                                                                                                                                    try:
                                                                                                                                        await client.wait_for('message', timeout=60)
                                                                                                                                    except asyncio.TimeoutError:
                                                                                                                                        await channel.send(embed=embedtimeout)
                                                                                                                                        canrun = False
                                                                                                                                    else:
                                                                                                                                        async for message in channel.history(limit=1):
                                                                                                                                            if message.author == user:
                                                                                                                                                longatt = int(message.content)
                                                                                                                                                if longatt > remain:
                                                                                                                                                    await channel.send("You do not have that many ponts.")
                                                                                                                                                else:
                                                                                                                                                    spent = health + defense + speed + closeatt + medatt + longatt
                                                                                                                                                    remain = int(maxpoints) - spent
                                                                                                                                                    await channel.send("You have spent {} points on long attack.".format(longatt))
                                                                                                                                                    healthmod = datadic[nationnamecheck]['ships'][shipname]['healthmod']
                                                                                                                                                    defencemod = datadic[nationnamecheck]['ships'][shipname]['defencemod']
                                                                                                                                                    speedmod = datadic[nationnamecheck]['ships'][shipname]['speedmod']
                                                                                                                                                    closemod = datadic[nationnamecheck]['ships'][shipname]['closemod']
                                                                                                                                                    medmod = datadic[nationnamecheck]['ships'][shipname]['mediummod']
                                                                                                                                                    longmod = datadic[nationnamecheck]['ships'][shipname]['longmod']
                                                                                                                                                    datadic.update({
                                                                                                                                                        userid:
                                                                                                                                                            {nationnamecheck:
                                                                                                                                                                {'ships':
                                                                                                                                                                    {
                                                                                                                                                                    shipname:
                                                                                                                                                                        {
                                                                                                                                                                        "shipclass":shipclass, 
                                                                                                                                                                        'maxpoints':maxpoints, 
                                                                                                                                                                        'healthmod':healthmod, 
                                                                                                                                                                        'speedmod':speedmod, 
                                                                                                                                                                        'defencemod':defencemod, 
                                                                                                                                                                        'closemod':closemod, 
                                                                                                                                                                        'mediummod':medmod, 
                                                                                                                                                                        'longmod':longmod, 
                                                                                                                                                                        "health":(health+1)*healthmod, 
                                                                                                                                                                        "defense":(defense+1)*defencemod, 
                                                                                                                                                                        "speed":(speed+1)*speedmod, 
                                                                                                                                                                        "close":(closeatt+1)*closemod, 
                                                                                                                                                                        "med":(medatt+1)*medmod, 
                                                                                                                                                                        "long":(longatt+1)*longmod, 
                                                                                                                                                                        }
                                                                                                                                                                    }
                                                                                                                                                                }
                                                                                                                                                            }
                                                                                                                                                        })
                                                                                                                                                    with open("data.txt", "w") as outfile:
                                                                                                                                                        json.dump(datadic, outfile)

                                                                                                                                                    await channel.send("Ship successfully edited.")
                                                                                                                                                    embedsummary = discord.Embed(title='Summary', description='{}'.format(shipname))
                                                                                                                                                    embedsummary.add_field(name='Properties', value="""Nation: {}
Class: {}
Name: {}""".format(nationnamecheck, shipclass, shipname), inline=False)
                                                                                                                                                    healthscore = datadic[nationnamecheck]['ships'][shipname]['health']
                                                                                                                                                    defensescore = datadic[nationnamecheck]['ships'][shipname]['defense']
                                                                                                                                                    speedscore = datadic[nationnamecheck]['ships'][shipname]['speed']
                                                                                                                                                    closescore = datadic[nationnamecheck]['ships'][shipname]['close']
                                                                                                                                                    medscore = datadic[nationnamecheck]['ships'][shipname]['med']
                                                                                                                                                    longscore = datadic[nationnamecheck]['ships'][shipname]['long']
                                                                                                                                                    embedsummary.add_field(name='Stats', value="""Health: {}
Defense: {}
Speed: {}
Close Attack: {}
Medium Attack: {}
Long Attack: {}""".format(healthscore, defensescore, speedscore, closescore, medscore, longscore), inline=False)
                                                                                                                                                    await channel.send(embed=embedsummary)

                                        else:
                                            await channel.send("Ship does not exist.")
                                            canrun = False


                            else:
                                await channel.send("You do not own that nation.")
                                canrun = False
                elif message.content == "fleet" and message.author == user:
                    return # do this
                else:
                    canrun = False
    if canrun == False:
        if channel == client.get_channel(764017189279236096):
            channel1available = True
            role4 = 'ships and fleets 1' #role to add
            await user.remove_roles(discord.utils.get(user.guild.roles, name=role4))
        elif channel == client.get_channel(764017265125228544):
            channel2available = True
            role5 = 'ships and fleets 2' #role to add
            await user.remove_roles(discord.utils.get(user.guild.roles, name=role5))
        elif channel == client.get_channel(764017300424622100):
            channel3available = True
            role6 = 'ships and fleets 3' #role to add
            await user.remove_roles(discord.utils.get(user.guild.roles, name=role6))

@client.command(name='delete')
async def delete(ctx):
    return

@client.command(name='view')
async def view(ctx):
    global channel1available
    global channel2available
    global channel3available
    user = ctx.message.author
    userid = ctx.author.id
    if channel1available == True:
        channel1available = False
        channel = client.get_channel(764017189279236096)
        role1 = 'ships and fleets 1' #role to add
        await user.add_roles(discord.utils.get(user.guild.roles, name=role1))
        canrun = True
    elif channel2available == True:
        channel2available = False
        channel = client.get_channel(764017265125228544)
        role2 = 'ships and fleets 2' #role to add
        await user.add_roles(discord.utils.get(user.guild.roles, name=role2))
        canrun = True
    elif channel3available == True:
        channel3available = False
        channel = client.get_channel(764017300424622100)
        role3 = 'ships and fleets 3' #role to add
        await user.add_roles(discord.utils.get(user.guild.roles, name=role3))
        canrun = True
    else:
        await ctx.send("All channels are currently unavailable. Please try again later.")
    if canrun == True:
        await channel.send("<@{}>, please move here.".format(userid))
        await channel.send("What would you like to view? (ship/fleet)")
        try:
            await client.wait_for('message', timeout=60)
        except asyncio.TimeoutError:
            await channel.send(embed=embedtimeout)
            canrun = False
        else:
            async for message in channel.history(limit=1):
                if message.content == "ship":
                    await channel.send("What is the name of the nation who owns the ship?")
                    try:
                        await client.wait_for('message', timeout=60)
                    except asyncio.TimeoutError:
                        await channel.send(embed=embedtimeout)
                        canrun = False
                    else:
                        async for message in channel.history(limit=1):
                            if message.author == user:
                                nationnamecheck = message.content
                                if keys_exists(datadic, nationnamecheck) == True:
                                    await channel.send("What is the name of the ship?")
                                    try:
                                        await client.wait_for('message', timeout=60)
                                    except asyncio.TimeoutError:
                                        await channel.send(embed=embedtimeout)
                                        canrun = False
                                    else:
                                        shipname = message.content
                                        if keys_exists(datadic, nationnamecheck, 'ships', shipname) == True:
                                            shipclass = datadic[nationnamecheck]['ships'][shipname]['shipclass']
                                            embedsummary = discord.Embed(title='Summary', description='{}'.format(shipname))
                                            embedsummary.add_field(name='Properties', value="""Nation: {}
Class: {}
Name: {}""".format(nationnamecheck, shipclass, shipname), inline=False)
                                            healthscore = datadic[nationnamecheck]['ships'][shipname]['health']
                                            defensescore = datadic[nationnamecheck]['ships'][shipname]['defense']
                                            speedscore = datadic[nationnamecheck]['ships'][shipname]['speed']
                                            closescore = datadic[nationnamecheck]['ships'][shipname]['closeatt']
                                            medscore = datadic[nationnamecheck]['ships'][shipname]['medatt']
                                            longscore = datadic[nationnamecheck]['ships'][shipname]['longatt']
                                            embedsummary.add_field(name='Stats', value="""Health: {}
Defense: {}
Speed: {}
Close Attack: {}
Medium Attack: {}
Long Attack: {}""".format(healthscore, defensescore, speedscore, closescore, medscore, longscore), inline=False)

                                            await channel.send(embedsummary)
                                        else:
                                            await channel.send("Ship does not exist.")
                                            canrun = False
                                else:
                                    await channel.send("Nation does not exist.")
                                    canrun = False
                if message.content == "fleet":
                    return
    if canrun == False:
        if channel == client.get_channel(764017189279236096):
            channel1available = True
            role4 = 'ships and fleets 1' #role to add
            await user.remove_roles(discord.utils.get(user.guild.roles, name=role4))
        elif channel == client.get_channel(764017265125228544):
            channel2available = True
            role5 = 'ships and fleets 2' #role to add
            await user.remove_roles(discord.utils.get(user.guild.roles, name=role5))
        elif channel == client.get_channel(764017300424622100):
            channel3available = True
            role6 = 'ships and fleets 3' #role to add
            await user.remove_roles(discord.utils.get(user.guild.roles, name=role6))

client.run("BOT TOKEN")
