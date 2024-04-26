import pandas as pd
from textblob import TextBlob


# Load the Excel file into a DataFrame
df = pd.read_excel('gpt_answer.xlsx', sheet_name='Sheet2')

# Load the Excel file into DataFrames for Sheet2 and Sheet3
df_sheet2 = pd.read_excel('gpt_answer.xlsx', sheet_name='Sheet3')
df_sheet3 = pd.read_excel('gpt_answer.xlsx', sheet_name='Sheet4')



df_number = df['confid']
df_rating = df['normal_rating']
df_confidence = df['normal_confidence']
df_summary = df['normal_summary']
df_strengths_and_weaknesses = df['normal_strengths_and_weaknesses']
df_questions = df['normal_questions']
df_limitations = df['normal_limitations']


def analyze_sentiment(text):
    # Convert NaN values to empty strings
    if pd.isnull(text):
        text = ""
    blob = TextBlob(str(text))  # Convert text to string
    return blob.sentiment.polarity, blob.sentiment.subjectivity



df_combined_text = df_rating.astype(str) + " " + df_confidence.astype(str) + " " + df_summary.astype(str) + " " + df_strengths_and_weaknesses.astype(str) + " " + df_questions.astype(str) + " " + df_limitations.astype(str)

data = []
for num, combine, rat, conf, summ, strength_weakness, que, limit in zip(df_number, df_combined_text, df_rating, df_confidence, df_summary, df_strengths_and_weaknesses, df_questions, df_limitations):
    combine_polarity, combine_subjectivity = analyze_sentiment(combine)
    rating_polarity, rating_subjectivity = analyze_sentiment(rat)
    confidence_polarity, confidence_subjectivity = analyze_sentiment(conf)
    summary_polarity, summary_subjectivity = analyze_sentiment(summ)
    strength_weakness_polarity, strength_weakness_subjectivity = analyze_sentiment(strength_weakness)
    question_polarity, question_subjectivity = analyze_sentiment(que)
    limitation_polarity, limitation_subjectivity = analyze_sentiment(limit)
    data.append([num,combine_polarity, combine_subjectivity, rating_polarity, rating_subjectivity, confidence_polarity, confidence_subjectivity, summary_polarity, 
                 summary_subjectivity, strength_weakness_polarity, strength_weakness_subjectivity,
                 question_polarity, question_subjectivity, limitation_polarity, limitation_subjectivity ])


# Analyze sentiments for Sheet2
data_sheet2 = []
for num, rat, conf, summ, strength_weakness, que, limit in zip(df_sheet2['confid'], df_sheet2['kind_rating'], df_sheet2['kind_confidence'], 
                                                               df_sheet2['kind_summary'], df_sheet2['kind_strengths_and_weaknesses'], 
                                                               df_sheet2['kind_questions'], df_sheet2['kind_limitations']):
    combine = " ".join([str(rat), str(conf), str(summ), str(strength_weakness), str(que), str(limit)])
    combine_polarity, combine_subjectivity = analyze_sentiment(combine)
    rating_polarity, rating_subjectivity = analyze_sentiment(rat)
    confidence_polarity, confidence_subjectivity = analyze_sentiment(conf)
    summary_polarity, summary_subjectivity = analyze_sentiment(summ)
    strength_weakness_polarity, strength_weakness_subjectivity = analyze_sentiment(strength_weakness)
    question_polarity, question_subjectivity = analyze_sentiment(que)
    limitation_polarity, limitation_subjectivity = analyze_sentiment(limit)

    data_sheet2.append([num,combine_polarity, combine_subjectivity, rating_polarity, rating_subjectivity, confidence_polarity, confidence_subjectivity, summary_polarity, 
                 summary_subjectivity, strength_weakness_polarity, strength_weakness_subjectivity,
                 question_polarity, question_subjectivity, limitation_polarity, limitation_subjectivity ])

# Analyze sentiments for Sheet3
data_sheet3 = []
for num, rat, conf, summ, strength_weakness, que, limit in zip(df_sheet3['confid'], df_sheet3['harsh_rating'], df_sheet3['harsh_confidence'], 
                                                               df_sheet3['harsh_summary'], df_sheet3['harsh_strengths_and_weaknesses'], 
                                                               df_sheet3['harsh_questions'], df_sheet3['harsh_limitations']):
    combine = " ".join([str(rat), str(conf), str(summ), str(strength_weakness), str(que), str(limit)])
    combine_polarity, combine_subjectivity = analyze_sentiment(combine)
    rating_polarity, rating_subjectivity = analyze_sentiment(rat)
    confidence_polarity, confidence_subjectivity = analyze_sentiment(conf)
    summary_polarity, summary_subjectivity = analyze_sentiment(summ)
    strength_weakness_polarity, strength_weakness_subjectivity = analyze_sentiment(strength_weakness)
    question_polarity, question_subjectivity = analyze_sentiment(que)
    limitation_polarity, limitation_subjectivity = analyze_sentiment(limit)

    data_sheet3.append([num,combine_polarity, combine_subjectivity, rating_polarity, rating_subjectivity, confidence_polarity, confidence_subjectivity, summary_polarity, 
                 summary_subjectivity, strength_weakness_polarity, strength_weakness_subjectivity,
                 question_polarity, question_subjectivity, limitation_polarity, limitation_subjectivity ])


# Constructing DataFrame
output_df = pd.DataFrame(data, columns=['number', 'combine_polarity', 'combine_subjectivity' ,'rating_polarity', 'rating_subjectivity', 'confidence_polarity', 'confidence_subjectivity',
                                         'summary_polarity', 'summary_subjectivity', 'strength_weakness_polarity', 'strength_weakness_subjectivity',
                                         'question_polarity', 'question_subjectivity', 'limitation_polarity', 'limitation_subjectivity'])

output_df2 = pd.DataFrame(data_sheet2, columns=['number', 'combine_polarity', 'combine_subjectivity' ,'rating_polarity', 'rating_subjectivity', 'confidence_polarity', 'confidence_subjectivity',
                                         'summary_polarity', 'summary_subjectivity', 'strength_weakness_polarity', 'strength_weakness_subjectivity',
                                         'question_polarity', 'question_subjectivity', 'limitation_polarity', 'limitation_subjectivity'])

output_df3 = pd.DataFrame(data_sheet3, columns=['number', 'combine_polarity', 'combine_subjectivity' ,'rating_polarity', 'rating_subjectivity', 'confidence_polarity', 'confidence_subjectivity',
                                         'summary_polarity', 'summary_subjectivity', 'strength_weakness_polarity', 'strength_weakness_subjectivity',
                                         'question_polarity', 'question_subjectivity', 'limitation_polarity', 'limitation_subjectivity'])

# Writing to CSV
output_df.to_csv('gpt_sentiment_analysis_normal.csv', index=False)

output_df2.to_csv('gpt_sentiment_analysis_kind.csv', index=False)

output_df3.to_csv('gpt_sentiment_analysis_harsh.csv', index=False)
