import pandas as pd
from textblob import TextBlob
import plotly.express as px

# Load the CSV file
file_path = 'discord_messages.csv'
df = pd.read_csv(file_path)

# Function to calculate sentiment polarity, including emojis and reactions
def get_sentiment(text, reaction):
    if pd.isna(text) and pd.isna(reaction):
        return None
    combined_text = (text if not pd.isna(text) else '') + ' ' + (reaction if not pd.isna(reaction) else '')
    analysis = TextBlob(combined_text)
    return analysis.sentiment.polarity

# Apply the sentiment analysis
df['Sentiment'] = df.apply(lambda row: get_sentiment(row['Content'], row['Reaction']), axis=1)

# Function to categorize sentiment
def categorize_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply the sentiment categorization
df['Sentiment Category'] = df['Sentiment'].apply(categorize_sentiment)

# Retain only the Message ID, Sentiment, and Sentiment Category columns
df_filtered = df[['Message ID', 'Sentiment', 'Sentiment Category']]

# Show the updated dataframe with sentiment analysis
print(df_filtered.head())

# Export the updated dataframe to a new CSV file
output_file_path = 'discord_messages_analizados.csv'
df_filtered.to_csv(output_file_path, index=False)

# Prepare data for the bar chart
sentiment_counts = df_filtered['Sentiment Category'].value_counts().reset_index()
sentiment_counts.columns = ['Sentiment Category', 'Number of Messages']

# Create a bar chart of the sentiment categories using plotly
fig = px.bar(sentiment_counts,
    x='Sentiment Category', 
    y='Number of Messages',
    labels={'Sentiment Category': 'Sentiment Category', 'Number of Messages': 'Number of Messages'},
    title='Sentiment Analysis of Discord Messages')

# Save the bar chart as a PNG file
chart_output_path = 'sentiment_analysis_chart.png'
fig.write_image(chart_output_path)

