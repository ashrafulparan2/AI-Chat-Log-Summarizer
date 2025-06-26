class ChatParser:
    
    def __init__(self):
        self.messages = []

    def parse(self, chat_lines):
        self.messages = []
        current_message = None
        
        for line in chat_lines:
            line = line.strip()
            if not line: 
                continue
                
            # Check if line starts with "User:" or "AI:"
            if line.startswith('User:') or line.startswith('AI:'):
                # If we have a previous message, save it
                if current_message:
                    self.messages.append(current_message)
                
                # Start new message
                speaker, message = line.split(':', 1)
                current_message = {
                    'speaker': speaker.strip(),
                    'message': message.strip()
                }
            elif current_message:
                
                current_message['message'] += ' ' + line
        
        if current_message:
            self.messages.append(current_message)
            
        return self.messages

    def get_messages_by_speaker(self, speaker):
        
        return [msg for msg in self.messages if msg['speaker'] == speaker]

    def get_all_messages(self):
        return self.messages
    
    def get_message_count(self):
        
        return len(self.messages)
    
    def get_speaker_count(self, speaker):
        
        return len(self.get_messages_by_speaker(speaker))