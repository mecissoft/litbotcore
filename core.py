import discord 
from discord.ext import commands
import json
import requests
import asyncio
client = commands.Bot(command_prefix = "!")

@client.event

async def on_ready():
	print("Bot Is Started!")

async def ver ( ctx ):
    await ctx.send('Ubutal Bot Core 1.6.1)
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send('Command Not Found.')

@client.command()
async def rcat(ctx):
    response = requests.get("https://some-random-api.ml/img/cat")
    json_data = json.loads(response.text)

    s = discord.Embed(color = 0xff9900, title = 'Random Cat')
    s.set_image(url = json_data['link'])
    await ctx.send(embed = s)

@client.event
async def on_ready():
     while True:
          await client.change_presence(status=discord.Status.online, activity=discord.Game("UBC Based"))

@client.command(name='say')
async def audit(ctx, *, msg=None):
    if msg is not None:
        await ctx.send(msg)

@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@client.command(pass_context = True)
async def ping( ctx ):
    author = ctx.message.author 
    await ctx.send(f'{author.mention}, Pong!')

@client.command(pass_context = True)
async def info( ctx ):
 await ctx.send('This Bot Based On Ubutal Bot Core!')

@client.command(pass_context = True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Member {member} Successfully Kicked.')
    
@client.command(pass_context = True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'The Member {member} Successfully Banned.')

token = open("token.txt", "r").readline()

client.run(token)

print("OK")
