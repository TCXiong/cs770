import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
    # Convert NaN values to empty strings
    if pd.isnull(text):
        text = ""
    blob = TextBlob(str(text))  # Convert text to string
    return blob.sentiment.polarity, blob.sentiment.subjectivity

df = pd.read_csv('real_reviews.csv')

# Extracting columns
df_number = df['number']
df_rating = df['rating']
df_confidence = df['confidence']
df_summary = df['summary']
df_strengths_and_weaknesses = df['strengths_and_weaknesses']
df_questions = df['questions']
df_limitations = df['limitations']

# Analyzing sentiment for each column
data = []
for num, rat, conf, summ, strength_weakness, que, limit in zip(df_number, df_rating, df_confidence, df_summary, df_strengths_and_weaknesses, df_questions, df_limitations):
    rating_polarity, rating_subjectivity = analyze_sentiment(rat)
    confidence_polarity, confidence_subjectivity = analyze_sentiment(conf)
    summary_polarity, summary_subjectivity = analyze_sentiment(summ)
    strength_weakness_polarity, strength_weakness_subjectivity = analyze_sentiment(strength_weakness)
    question_polarity, question_subjectivity = analyze_sentiment(que)
    limitation_polarity, limitation_subjectivity = analyze_sentiment(limit)
    data.append([num, rating_polarity, rating_subjectivity, confidence_polarity, confidence_subjectivity, summary_polarity, 
                 summary_subjectivity, strength_weakness_polarity, strength_weakness_subjectivity,
                 question_polarity, question_subjectivity, limitation_polarity, limitation_subjectivity ])

# Constructing DataFrame
output_df = pd.DataFrame(data, columns=['number', 'rating_polarity', 'rating_subjectivity', 'confidence_polarity', 'confidence_subjectivity',
                                         'summary_polarity', 'summary_subjectivity', 'strength_weakness_polarity', 'strength_weakness_subjectivity',
                                         'question_polarity', 'question_subjectivity', 'limitation_polarity', 'limitation_subjectivity'])

# Writing to CSV
output_df.to_csv('sentiment_analysis.csv', index=False)
