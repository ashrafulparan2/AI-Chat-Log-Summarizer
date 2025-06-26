class Summarizer:
    def __init__(self):
        pass

    def generate_summary(self, chat_data):
        user_messages = sum(1 for message in chat_data if message['speaker'] == 'User')
        ai_messages = sum(1 for message in chat_data if message['speaker'] == 'AI')
        total_exchanges = len(chat_data)
        
        # Extract main topics based on message content
        all_text = ' '.join([msg['message'] for msg in chat_data])
        nature = self._determine_conversation_nature(all_text)
        
        summary = {
            'total_exchanges': total_exchanges,
            'user_messages': user_messages,
            'ai_messages': ai_messages,
            'nature': nature
        }
        return summary
    
    def _determine_conversation_nature(self, text):
        # Simple keyword-based topic detection
        topics = []
        if 'machine learning' in text.lower() or 'ml' in text.lower():
            topics.append('machine learning')
        if 'python' in text.lower():
            topics.append('programming')
        if 'data' in text.lower():
            topics.append('data science')
        if 'ai' in text.lower() or 'artificial intelligence' in text.lower():
            topics.append('artificial intelligence')
        
        if not topics:
            topics = ['general conversation']
        
        return ', '.join(topics)