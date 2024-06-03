from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
from bot import chatbot

def get_feedback():

    text = input()

    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    elif text.lower() in exit_conditions:
        quit()
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()


trainer = ChatterBotCorpusTrainer(chatbot)
trainer2 = ListTrainer(chatbot)


trainer.train(
    'chatterbot.corpus.english'
)

exit_conditions = (":q", "quit", "exit")
print()
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        response = chatbot.get_response(
            query
        )

        print(f'\nis "{response.text}" what katbot would say to "{query}"?')
        yes_or_no = get_feedback()
        if yes_or_no is False:
            print('please input the correct one')
            correct_response = input()
            trainer2.train([
                query,
                correct_response,
                ])
            print('responses added to bot!')
        elif yes_or_no is True:
            print('great. carry on.')
