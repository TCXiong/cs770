from textblob import TextBlob


def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

def main():
    # Input your essay text here, or integrate a way to read from a file or other sources
    essay_text = """
    you are fucking good
    """
    sentiment = analyze_sentiment(essay_text)
    print("Sentiment of the essay:")
    print("Polarity: ", sentiment.polarity)  # How positive or negative the text is
    print("Subjectivity: ", sentiment.subjectivity)  # How subjective the text is

if __name__ == "__main__":
    main()
