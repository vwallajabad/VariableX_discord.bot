from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("Variable X",
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
              {
                  'import_path': 'chatterbot.logic.BestMatch',
                  'default_response': 'I am sorry, but I do not understand.',
                  'maximum_similarity_threshold': 0.80
              }])


list_trainer = ListTrainer(bot)
automatic_trainer = ChatterBotCorpusTrainer(bot)

automatic_trainer.train("chatterbot.corpus.english")
list_trainer.train('train.txt')
