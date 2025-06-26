from collections import Counter
import re

class KeywordAnalyzer:
    def __init__(self):
        # Define common stop words to exclude
        self.stop_words = {
            'the', 'is', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
            'a', 'an', 'as', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
            'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must',
            'can', 'you', 'i', 'me', 'my', 'we', 'us', 'our', 'they', 'them', 'their', 'he',
            'him', 'his', 'she', 'her', 'it', 'its', 'this', 'that', 'these', 'those',
            'user', 'ai', 'hi', 'hello', 'thank', 'thanks', 'welcome', 'please', 'sure'
        }

    def extract_keywords(self, messages):
        # Extract text from all messages
        all_text = ' '.join([msg['message'] for msg in messages])
        
        # Use regex to find words and convert to lowercase
        words = re.findall(r'\b\w+\b', all_text.lower())
        
        # Filter out stop words and short words (less than 3 characters)
        filtered_words = [word for word in words if word not in self.stop_words and len(word) > 2]
        
        # Count the frequency of each word
        word_counts = Counter(filtered_words)
        
        # Get the top 5 most common words
        return word_counts.most_common(5)