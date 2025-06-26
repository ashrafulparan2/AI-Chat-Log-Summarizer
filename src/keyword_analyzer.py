import nltk
from collections import Counter
import re
from sklearn.feature_extraction.text import TfidfVectorizer

class KeywordAnalyzer:
    def __init__(self):
        # Download NLTK stopwords if not already downloaded
        try:
            self.stop_words = set(nltk.corpus.stopwords.words('english'))
        except LookupError:
            nltk.download('stopwords')
            self.stop_words = set(nltk.corpus.stopwords.words('english'))
        
        # Add common chat words to stop words
        self.stop_words.update(['user', 'ai', 'can', 'you', 'i', 'me', 'my', 'hi', 'hello', 'thank', 'thanks', 'today', 'explain', 'tell', 'ask', 'question', 'answer', 'like', 'know', 'want', 'see', 'good', 'bad'])

    def extract_keywords(self, messages):
        # Extract text from messages
        all_text = ' '.join([msg['message'] for msg in messages])
        
        # Basic keyword extraction using word frequency
        basic_keywords = self._extract_basic_keywords(all_text)
        
        # TF-IDF based keyword extraction (bonus feature)
        tfidf_keywords = self._extract_tfidf_keywords([msg['message'] for msg in messages])
        
        return {
            'basic_keywords': basic_keywords,
            'tfidf_keywords': tfidf_keywords
        }
    
    def _extract_basic_keywords(self, text):
        # Use regex to find words and convert to lower case
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Filter out stop words and short words
        filtered_words = [word for word in words if word not in self.stop_words and len(word) > 2]
        
        # Count the frequency of each word
        word_counts = Counter(filtered_words)
        
        # Get the top 5 most common words
        return word_counts.most_common(5)
    
    def _extract_tfidf_keywords(self, messages):
        if len(messages) < 2:
            return []
        
        try:
            # Create TF-IDF vectorizer
            vectorizer = TfidfVectorizer(
                max_features=10,
                stop_words='english',
                ngram_range=(1, 2),
                min_df=1
            )
            
            # Fit and transform the messages
            tfidf_matrix = vectorizer.fit_transform(messages)
            
            # Get feature names and their average TF-IDF scores
            feature_names = vectorizer.get_feature_names_out()
            scores = tfidf_matrix.mean(axis=0).A1
            
            # Create keyword-score pairs and sort by score
            keyword_scores = list(zip(feature_names, scores))
            keyword_scores.sort(key=lambda x: x[1], reverse=True)
            
            return keyword_scores[:5]
        except:
            return []