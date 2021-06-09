#defining bot
def discord_code():
    import discord
    import random
    from chatterbot import ChatBot
    from chatterbot.trainers import ListTrainer
    from chatterbot.trainers import ChatterBotCorpusTrainer
    from keep_alive import keep_alive
    from pretty_help import PrettyHelp
    from pretty_help import DefaultMenu
    from discord.ext import commands
    import os
    token = os.environ['token']
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
    list_trainer.train("./train.yml")

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
