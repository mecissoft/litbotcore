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
    await ctx.send('LitBot Core 2.1)
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send('Command Not Found.')

@client.event
async def on_ready():
     while True:
          await client.change_presence(status=discord.Status.online, activity=discord.Game("LBC Based"))

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
 await ctx.send('This Bot Based On LitBot Core!')

@client.command(pass_context = True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Member {member} Successfully Kicked.')
    
@client.command(pass_context = True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'The Member {member} Successfully Banned.')

@client.event
async def on_guild_join(guild):
   welcome = bot.get_channel(guild_welcome[member.guild.id])
   embed=discord.Embed(title="Welcome!", description=f"Welcome{member.guild.name} To {member.mention}!", color=0x4682B4)
   await welcome.send(embed=embed)|

@client.command()
@commands.guild_only()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + ": Server Info",
        color=discord.Color(0x4682B4)
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Members", value=memberCount, inline=True)

token = open("token.txt", "r").readline()

client.run(token)

print("OK")
