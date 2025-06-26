class Summarizer:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self._initialize_t5_model()
    
    def _initialize_t5_model(self):
        """Initialize T5 model for summarization."""
        try:
            from transformers import T5ForConditionalGeneration, T5Tokenizer
            self.tokenizer = T5Tokenizer.from_pretrained('t5-small')
            self.model = T5ForConditionalGeneration.from_pretrained('t5-small')
            print("T5-small model loaded successfully")
        except ImportError as e:
            raise ImportError("transformers library is required. Please install it with: pip install transformers") from e
        except Exception as e:
            raise RuntimeError(f"Could not load T5 model: {e}") from e

    def generate_summary(self, chat_data):
        user_messages = sum(1 for message in chat_data if message['speaker'] == 'User')
        ai_messages = sum(1 for message in chat_data if message['speaker'] == 'AI')
        total_exchanges = len(chat_data)
        
        # Generate conversational summary using T5
        conversational_summary = self._t5_generate_summary(chat_data)
        
        summary = {
            'total_exchanges': total_exchanges,
            'user_messages': user_messages,
            'ai_messages': ai_messages,
            'conversational_summary': conversational_summary
        }
        return summary
    
    def _t5_generate_summary(self, chat_data):
        """Use T5 model to generate conversational summary."""
        # Extract only user messages to focus on what they asked about
        user_messages = [msg['message'] for msg in chat_data if msg['speaker'] == 'User']
        user_text = ' '.join(user_messages)
        
        # Limit text length for T5
        user_text = user_text[:500]
        
        # Use a more specific prompt to get better summaries
        input_text = f"Complete this sentence about what the user wants to learn: 'The user is asking about' based on these questions: {user_text}"
        inputs = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        
        # Generate summary
        outputs = self.model.generate(
            inputs, 
            max_length=50, 
            min_length=10, 
            do_sample=False,
            num_beams=3
        )
        
        raw_summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Post-process the T5 output to make it more readable
        processed_summary = self._process_t5_summary(raw_summary, user_messages)
        return processed_summary

    def _process_t5_summary(self, raw_summary, user_messages):
        """Post-process T5 output to create better conversational summaries."""
        # Clean up the raw summary
        summary = raw_summary.strip()
        
        # If the summary is too generic or empty, return a simple default
        if not summary or len(summary) < 10:
            return "The user engaged in a conversation with the AI assistant."
        
        # Extract the part after "The user is asking about"
        if "the user is asking about" in summary.lower():
            # Find the relevant part
            start_idx = summary.lower().find("the user is asking about") + len("the user is asking about")
            topic_part = summary[start_idx:].strip()
            
            # Clean up and format
            if topic_part:
                # Remove any trailing periods and clean up
                topic_part = topic_part.rstrip('.')
                return f"The user is asking about {topic_part}."
        
        # Return the raw summary if it doesn't follow expected format
        return summary