from chatterbot import ChatBot

chatbot = ChatBot("KatBot", 
    #storage_adapter='chatterbot.storage.SQLStorageAdapter'
)

exit_conditions = (":q", "quit", "exit")
print()
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
        print(response)