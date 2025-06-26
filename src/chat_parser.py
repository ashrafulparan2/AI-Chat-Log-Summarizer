class ChatParser:
    def __init__(self):
        self.messages = []

    def parse(self, chat_lines):
        self.messages = []
        for line in chat_lines:
            if line.strip():  # Ignore empty lines
                parsed_msg = self._parse_line(line)
                if parsed_msg:
                    self.messages.append(parsed_msg)
        return self.messages

    def _parse_line(self, line):
        if ':' in line:
            speaker, message = line.split(':', 1)
            return {'speaker': speaker.strip(), 'message': message.strip()}
        return None

    def get_messages_by_speaker(self, speaker):
        return [msg for msg in self.messages if msg and msg['speaker'] == speaker]

    def get_all_messages(self):
        return self.messages