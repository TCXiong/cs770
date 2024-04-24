from textblob import TextBlob
import os

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

def main():
    print("Welcome to the sentiment analyzer!")
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    try:
        with open(file_path, 'r') as file:
            essay_text = file.read()
            sentiment = analyze_sentiment(essay_text)
            print("\nSentiment analysis result:")
            print("Polarity:", sentiment.polarity)  # How positive or negative the text is
            print("Subjectivity:", sentiment.subjectivity)  # How subjective the text is
    except FileNotFoundError:
        print("File not found. Please make sure there is a file named 'input.txt' in the same directory as this script.")

if __name__ == "__main__":
    main()
