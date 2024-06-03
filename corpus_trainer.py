from chatterbot.trainers import ChatterBotCorpusTrainer
from bot import chatbot

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')