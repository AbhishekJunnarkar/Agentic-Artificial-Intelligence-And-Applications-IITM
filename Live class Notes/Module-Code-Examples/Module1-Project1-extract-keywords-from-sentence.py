import re

def extract_keywords(sentence):
    # Convert to lowercase
    sentence = sentence.lower()

    # Remove punctuation
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # Define common stopwords
    stopwords = {
        'the', 'is', 'in', 'and', 'to', 'of', 'a', 'for', 'on',
        'at', 'by', 'an', 'be', 'as', 'are', 'from', 'with', 'that', 'this', 'it', 'can'
    }

    # Split words and filter out stopwords
    words = [word for word in sentence.split() if word not in stopwords]

    return list(set(words))  # return unique keywords


# Example
text = "Agentic AI enables systems that can plan, adapt, and act autonomously across contexts."
print(extract_keywords(text))
