from chatterbot.trainers import ChatterBotCorpusTrainer
from bot import chatbot

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    './kat_corpus/ai.yml',
    './kat_corpus/botprofile.yml',
    './kat_corpus/conversations.yml',
    './kat_corpus/emotion.yml',
    './kat_corpus/food.yml',
    './kat_corpus/gossip.yml',
    './kat_corpus/greetings.yml',
    './kat_corpus/humor.yml',
    './kat_corpus/psychology.yml',
    './kat_corpus/science.yml',
    './kat_corpus/sports.yml',
)
