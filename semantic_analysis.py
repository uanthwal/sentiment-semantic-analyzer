import json
from prettytable import PrettyTable
import math

with open('newsapi_data.json', 'r') as myfile:
    data_from_file = json.load(myfile);

frequency = {}

# Setting up basic keywords
keywords_list = {"Canada": 0, "University": 0, "Dalhousie University": 0, "Halifax": 0, "Canada Education": 0}
log_value_for_keywords = {}


def TF_IDF(total):
    total_split = total.split(" ")
    search_query_1 = ["Canada", "University", "Dalhousie University", "Halifax", "Canada Education"]
    search_query_2 = ["Dalhousie University", "Canada Education"]

    for search in search_query_1:
        for i in range(len(total_split)):
            if (total_split[i].lower() == search.lower() or search.lower() == total_split[i].lower()[0:len(search)]):
                keywords_list[search] = keywords_list[search] + 1
                break

    for search in search_query_2:
        for i in range(len(total_split) - 1):
            x = total_split[i] + " " + total_split[i + 1]
            if (x.lower() == search.lower() or x.lower()[0:len(search)] == search.lower()):
                keywords_list[search] = keywords_list[search] + 1
                break


def occurence(words):
    list = []
    words_split = words.split(" ")
    total_words = len(words_split)
    freq = 0
    list.append(total_words)
    for i in range(total_words):
        if (words_split[i].lower() == "Canada" or words_split[i].lower() == "canada"):
            freq = freq + 1
    list.append(freq)
    return list


def relative_frequency_calculation(list):
    relative_freq = round(list[1] / list[0], 2)
    return relative_freq


def calculate_log_value(value):
    return (math.log10(value))


for i in range(len(data_from_file)):
    news_content_str = str(data_from_file[i]["title"]) + " " + str(data_from_file[i]["description"]) + " " + str(
        data_from_file[i]["content"])
    TF_IDF(news_content_str)
    l = occurence(news_content_str)
    s = "Article " + str(i + 1)
    frequency[s] = l

relative_frequency = {}

for i in keywords_list:
    if keywords_list[i] != 0:
        log_value_for_keywords[i] = calculate_log_value(len(data_from_file) / keywords_list[i])
    else:
        log_value_for_keywords[i] = keywords_list[i]


def calculate_highest_relative_freq():
    for i in range(len(frequency)):
        s = "Article " + str(i + 1)
        x = relative_frequency_calculation(frequency[s])
        relative_frequency[s] = x


data_str = "<b>Total Documents (N):</b> " + str(100) + "<br/>"
print("Total Documents (N): " + str(100))
pretty_table_1 = PrettyTable(border=True)
pretty_table_1.field_names = ["Search Query", "Document containing term (df)",
                              "Total Documents (N)/number of documents term appeared (df)",
                              "Log10 (N/df)"]
pretty_table_1.align = "l"
total_documents = 100
for key in keywords_list:
    total_documents_by_df = 0
    if keywords_list[key] == 0:
        total_documents_by_df = 0
    else:
        total_documents_by_df = total_documents / keywords_list[key]
    pretty_table_1.add_row([key, keywords_list[key], total_documents_by_df, log_value_for_keywords[key]])

print(pretty_table_1)
data_str = data_str + pretty_table_1.get_html_string()

pretty_table_2 = PrettyTable(border=True)
pretty_table_2.field_names = ["Article", "Total Words (m)", "Frequency (f)"]
pretty_table_2.align = "l"
for key in frequency:
    f = frequency[key][1]
    m = frequency[key][0]
    if f != 0:
        pretty_table_2.add_row([key, m, f])

print(pretty_table_2)
data_str = data_str + "<br/><br/>"
data_str = data_str + pretty_table_2.get_html_string()

calculate_highest_relative_freq()
x = sorted(relative_frequency.items(), key=lambda x: x[1])
highest_relative_freq = (x[len(x) - 1])
data_str = data_str + "<br/><br/>"
data_str = data_str + "<b>Highest Relative Frequency:</b> " + str(highest_relative_freq[1])
data_str = data_str + "<br/><b>Highest Relative Frequency Article:</b> " + str(highest_relative_freq[0])

print("Highest Relative Frequency: " + str(highest_relative_freq[1]))
print("Highest Relative Frequency Article: " + str(highest_relative_freq[0]))

text_file = open("semantic_analysis_output.html", "w")
n = text_file.write(data_str)
text_file.close()
