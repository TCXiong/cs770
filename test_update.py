from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

def main():
    print("Welcome to the sentiment analyzer!")
    print("Type your text and press Enter to analyze. Type 'exit' to quit.")

    while True:
        user_input = input("Enter text: ")

        if user_input.lower() == 'exit':
            print("Exiting...")
            break

        sentiment = analyze_sentiment(user_input)
        print("\nSentiment analysis result:")
        print("Polarity:", sentiment.polarity)  # How positive or negative the text is
        print("Subjectivity:", sentiment.subjectivity)  # How subjective the text is
        print()

if __name__ == "__main__":
    main()
