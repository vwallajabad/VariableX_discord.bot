import discord
import random
from keep_alive import keep_alive
from pretty_help import PrettyHelp
from pretty_help import DefaultMenu
token = 'ODUwODg3ODQxNjU1NTU0MDg4.YLwRDg.vNQtk1O-2Go9wYPsZiRgYafq4-M'
from discord.ext import commands
varx = commands.Bot(command_prefix = ">")
menu = DefaultMenu("\U0001F44D", "👎", ":discord:743511195197374563")
varx.help_command = PrettyHelp(navigation=menu, color=discord.Colour.blue())

bot_name = varx.user
@varx.event
async def on_ready():
  print('Welcome', varx.user.name, varx.user.id)
  print("This bot aka VariableX is ready to take over the WORLD!")

@varx.command()
async def randomnumber(ctx):
  await ctx.send(random.randrange(1, 100))

@varx.event
async def on_guild_join(member):
  channel = discord.utils.get(member.guild.channels, name = "Variable.X")
  await channel.send('Hello', member.mention)

@varx.event
async def on_guild_remove(member):
  channel = discord.utils.get(member.guild.channels, name = "Variable.X")
  await channel.send(member.mention, 'left the server')
  print(member,"Joined the server")

@varx.command()
async def chat(ctx):
    await ctx.send('Hello I am VariableX')


    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    while True:
        user_message = await varx.wait_for("message", check=check)
        user_message_for_bot = user_message.content
        print(user_message_for_bot)
    #   bot_answer = bot.get_response(user_message_for_bot)
        await ctx.send(user_message_for_bot)
varx.run(token)
