def show_message(messages):
    for message in messages:
        print(f"\n{message}")
def send_message(message_1,message_2):
    while message_1:
        current_message = message_1.pop()
        message_2.append(current_message)
messages_1= ['nihao','wohao','dajiahao']
message_2 =[]
show_message(messages_1)
send_message(messages_1[:],message_2)
show_message(messages_1)
show_message(message_2)