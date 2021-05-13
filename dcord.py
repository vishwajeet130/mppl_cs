import os
import discord
import random
import praw
from discord.ext import commands, tasks
client = commands.Bot(command_prefix=".")

reddit = praw.Reddit(client_id = "o0F26BJZ9KQgKA",
                     client_secret = "MYn_BkdtD90qBjfNSAxjLgTrWKLzXw",
                     username = "maj_vishwa",
                     password = "VisualKing007",
                     user_agent = "Vishwa Jr.")



f = open("data/greeting.txt")
greeting = f.readlines()

f = open("data/status.txt","r")
status = f.readlines()

f = open("data/menuitem.txt","r")
menuitem = f.readlines()

f = open("data\line.txt","r")
line = f.readlines()

f = open("data\menu1.txt","r")
menu1 = f.readlines()

f = open("data\menu2.txt","r")
menu2 = f.readlines()


@client.event
async def on_ready():
    print("Bot is Online")

#Status
@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(random.choice(status)))

#hello
@client.command(aliases=['hi','Hii','Hello','hola','Hi'])
async def hello(ctx):
    await ctx.send(random.choice(greeting))


@client.group(invoke_without_command=True)
async def menu(ctx):
    menuEmbed= discord.Embed(title="Main Menu",description="Type the corresponding number i.e. (.menu number)",color=0xff0000)

    for i in range(0,len(menuitem)):
        menuEmbed.add_field(name=menuitem[i],value=line[0],inline=False)

    await ctx.send(embed=menuEmbed)

@menu.command()
async def one(ctx):
    menuEmbed= discord.Embed(title="Online Compilers for Programming",description="Type the corresponding number i.e. (.menu number)",color=0xff0000)

    for i in range(0,len(menu1)):
        menuEmbed.add_field(name=menu1[i],value=line[0],inline=False)

    await ctx.send(embed=menuEmbed)

@menu.command()
async def two(ctx):
    menuEmbed= discord.Embed(title="Study Material",description="Type the corresponding number i.e. (.menu number)",color=0xff0000)

    for i in range(0,len(menu2)):
        menuEmbed.add_field(name=menu2[i],value=line[0],inline=False)

    await ctx.send(embed=menuEmbed)


    



#deletemsg

@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx,amount = 2):
    await ctx.channel.purge(limit = amount)

#moderation

@client.command()
@commands.has_permissions(administrator = True)
async def kick(ctx,member : discord.Member,*,reason = "Violation of Rules."):
    await member.kick(reason=reason)

#memes

@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    meme_list = []
    top = subreddit.top(limit = 50)

    for submission in top:
        meme_list.append(submission)
    
    random_sub = random.choice(meme_list)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)

    em.set_image(url = url)

    await ctx.send(embed = em)


client.run("ODA2MDg2MTQ5MjM5NDcyMTY4.YBkUOg.DhfNKECCc7Gsp5HrlIt65V3nlrI")