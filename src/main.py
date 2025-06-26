# main.py

import os
from chat_parser import ChatParser
from utils.file_handler import read_chat_log

def main():
    # Read the chat log file
    chat_log_path = os.path.join('..', 'data', 'chat.txt')
    chat_log = read_chat_log(chat_log_path)

    # Parse the chat log
    parser = ChatParser()
    parsed_chat = parser.parse(chat_log)

    # Display the parsed messages
    print("Chat Log Parsing Results:")
    print("=" * 40)
    
    for message in parsed_chat:
        print(f"{message['speaker']}: {message['message']}")
    
    print("\n" + "=" * 40)
    print(f"Total messages parsed: {len(parsed_chat)}")
    
    # Show messages by speaker
    user_messages = parser.get_messages_by_speaker('User')
    ai_messages = parser.get_messages_by_speaker('AI')
    
    print(f"User messages: {len(user_messages)}")
    print(f"AI messages: {len(ai_messages)}")

if __name__ == "__main__":
    main()