# sentiment-semantic-analyzer

## 1. Sentiment Analysis:
• Source code script name: sentiment_analysis.py
• Input: The python script takes the twitter data fetched in Assignment 2[1], the
name of file is ‘twitter_data json’
• Steps performed in the python program:
o The data from above named file is cleaned by removing the special characters, urls etc.,
o Bag of tweets is created for each tweet present in the json file mentioned above.
o List of positive [2] and negative [3] words is fetched from internet. o For each tweet, comparison is done against the positive and negative
words list fetched in previous step and further a final object is created that contains below information for every tweet:
▪ tweet message
▪ list of positive words (if any) ▪ list of negative words (if any)
o A file (most_occurring_keywords.csv) that contains list of words with their count is prepared for creating the word cloud using Tableau [4].
• Output: The script creates a html file which shows the polarity of every tweet in a tabular format. File name sentiment_analysis_output.html file (The output has been stored in a html file for better readability).

## 2. Semantic Analysis:
• Source code script name: sentiment_analysis.py
• Input: The python script takes the news api data fetched in Assignment 2[1], the
name of file is ‘newsapi_data json’
• Steps performed in the python program:
o Data is organized as per the instructions in the assignment handout i.e. the title, description, and the news content are to be fetched from the raw news article.
o Data cleaning is done as in Assignment 2 [1], since the raw data is used for this assignment, this step is required.
o Computation of TF-IDF (term frequency – inverse document frequency) is carried out.
o Calculation for finding the occurrence of the word ‘Canada’ in every news article is carried out.
o Calculation and printing the news article, which has highest relative frequency
    
• Output: The script creates a html file which shows the output in a tabular format. File name semantic_analysis_output.html file (The output has been stored in a html file for better readability).


## References:
[1] Datawarehouse Assignment, “Assignment 2” in Brightspace, [online portal], 06 November 2019. Available: brightspace.com Reference Online, https://dal.brightspace.com/d2l/lms/dropbox/user/folders_history.d2l?db=62303&grpid=0&isprv =0&bp=0&ou=100142 [Accessed: November 30, 2019].<br/>
[2] Github Gist, “positive-words.txt” in Github, [online portal], 22 August 2004. Available: gist.github.com Reference Online, https://gist.github.com/mkulakowski2/4289437 [Accessed: December 01, 2019].<br/>
[3] Github Gist, “negative-words.txt” in Github, [online portal], 22 August 2004. Available: gist.github.com Reference Online, https://gist.github.com/mkulakowski2/4289441 [Accessed: December 01, 2019].<br/>
[4] Parul Pandey, “Word Clouds in Tableau: Quick & Easy” in Towards Data Science, [online article], 20 February 2019. Available: dzone.com Reference Online, https://towardsdatascience.com/word-clouds-in-tableau-quick-easy-e71519cf507a [Accessed: November 02, 2019].
