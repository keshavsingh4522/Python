from bs4 import BeautifulSoup as bsoup
import pandas as pd
import numpy as np
import humanfriendly

# Read in email data file
df = pd.read_csv('../bodytext.csv', header = 0)

# Filter out sent mail 
emails = df.query('FromEmail != "[my email address]"').copy()

def wordCount(row):

    if(row['Format'] == 'Html'):
        return htmlWordCount(row['Body'])

    return textWordCount(row['Body'])

def textWordCount(text):
    if not(isinstance(text, str)):
        return 0

    return len(text.split(None))

def htmlWordCount(text):
    if not(isinstance(text, str)):
        return 0

    soup = bsoup(text, 'html.parser')

    if soup is None:
        return 0

    stripped = soup.get_text(" ", strip=True)

    [s.extract() for s in soup(['style', 'script', 'head', 'title'])]

    stripped = soup.get_text(" ", strip=True)

    return textWordCount(stripped)

averageWordsPerMinute = 350 

# Count the words in each message body
emails['WordCount'] = emails.apply(wordCount, axis=1)
emails['MinutesToRead'] = emails['WordCount'] / averageWordsPerMinute

# Get total number of minutes required to read all these emails
totalMinutes = emails['MinutesToRead'].sum()

# And convert that to a more human-readable timespan
timeToRead = humanfriendly.format_timespan(totalMinutes * 60)
