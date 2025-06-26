class Summarizer:
    def __init__(self):
        pass

    def generate_summary(self, chat_data):
        # Count messages by speaker
        user_messages = sum(1 for message in chat_data if message['speaker'] == 'User')
        ai_messages = sum(1 for message in chat_data if message['speaker'] == 'AI')
        total_messages = len(chat_data)
        
        summary = {
            'total_messages': total_messages,
            'user_messages': user_messages,
            'ai_messages': ai_messages
        }
        return summary