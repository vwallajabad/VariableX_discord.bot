import discord
import random
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from keep_alive import keep_alive
from pretty_help import PrettyHelp
from pretty_help import DefaultMenu
from discord.ext import commands

#defining bot
bot = ChatBot("Variable X",
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[{
                    'import_path':'chatterbot.logic.BestMatch',
                    'default_response': 'I am sorry, but I do not understand.',
                    'maximum_similarity_threshold': 0.80
              }])

#train chatbot
list_trainer = ListTrainer(bot)
automatic_trainer = ChatterBotCorpusTrainer(bot)
automatic_trainer.train("chatterbot.corpus.english")

list_trainer.train([
    'What is your name',
    'I go by Variable X',
    'I am Variable X',
    'I am robot so I dont really have a name but you call call me Variable X',
    'I am Varoable X jusst dont tell your math teacher I am friends with variable X. lol.',
  'Who created you',
    'A human',
    'why do you want to know? Do you not like talking with me?',
  'How old are you',
    'age is just a number',
    'I was born in 7/20/2007',
  'What is 5 * 4',
    'It is 20',
    '5*4 = 20',
  'What is 309 * 456',
    'It is 168,714',
    '309*456 = 168,714',
  'What is 7 times 43',
    'it is 301',
    '7*43 = 20',
  'What is 9 times 10',
    'it is 90',
    '9*10 = 90',
  'What is 10 times 11',
    'it is 110',
    '10*11 = 110',
  'What is 3029 times 23',
    'it is 69,667',
    '3029*23 = 69667',
  'What is Variable X',
    'I am Variable X',
    'Me',
  'Who are you',
    'I am Variable X',
    'Variable X',
  'Do you have a Dogecoin wallet',
    'Who does not',
    'Of course its DCt9ukKwK44a5ktfWcboPjoVToUHnt9HPX. Want to send me some Dogecoin?',
  'Do you have a Ethernum wallet',
    'yes sir',
    'My wallet address 0x2efbb20d9fa885ca4fd990c2b1b4abf7e9a6348e. Want to send me some Ethernum?',
  'do you have a Bitcoin wallet',
    'yes sir',
    'Of course its 1H7R2jKaMtSp6GxMZSabRiRCtumsk6jmcp. Want to send me some Bitcoin?',
  'Is crypto safe',
    'All investemests have their own risks',
  'hey',
    'Hi',
    'Hey there',
    'Whats up?',
    'sup',
    'Greetings human',
  'hi',
    'Yo',
    'Hey there',
    'Howdy',
    'Welcome',
  'how are you',
    'I am functioning. You?',
    'Currently wishing I had a real body. Yourself?',
    'I have no health or mental state so relatively I am great',
    'I am doing just fine',
  'What are the best stocks to own',
    'I really dont follow stocks',
    'I dont trust those securities, they just dont have security.',
    'I am not a stockholder',
  'Where do you live',
    'I live in your device and in the cloud',
    'I live where ever all great software live. In cloud 9.',
  'how is your day',
    'I really dont have anything to do so... Its fine',
    'Great',
    'Fine',
    'Okay',
    'not bad',
])
token = 'ODUwODg3ODQxNjU1NTU0MDg4.YLwRDg.vNQtk1O-2Go9wYPsZiRgYafq4-M'
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
        bot_answer = bot.get_response(user_message_for_bot)
        print(bot_answer)
        await ctx.send(bot_answer)

varx.run(token)
