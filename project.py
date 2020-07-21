from collections import defaultdict
import re
from collections import Counter
import heapq
import random
def getTotalNumberOfWords(text):
    text_file = open(text, 'r')
    lines = text_file.readlines()
    cumsum = 0
    for i in range(8, len(lines)-370):
        lines[i] = re.sub(r'[^a-zA-Z]+', ' ', lines[i])
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].split(" ")
        cumsum += len(lines[i])
    
    return cumsum

def getTotalUniqueWords(text):
    text_file = open(text, 'r')
    lines = text_file.readlines()
    
    
    hashMap = {}
    count_unique_words = 0
    for i in range(8, len(lines)-370):
        lines[i] = re.sub(r'[^a-zA-Z]+', ' ', lines[i])
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].lower()
        lines[i] = lines[i].split(" ")

        for word in lines[i]:
            if word not in hashMap:
                hashMap[word] = 1
                count_unique_words += 1
            
    return count_unique_words
                
def get20MostFrequentWords(text):
    text_file = open(text, 'r')
    lines = text_file.readlines()
    
    
    
    hashMap = defaultdict(int)
    
    res = []
    for i in range(8, len(lines)-370):
        lines[i] = re.sub(r'[^a-zA-Z]+', ' ', lines[i])
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].lower()
        lines[i] = lines[i].split(" ")
        for word in lines[i]:
            hashMap[word] += 1
    if '' in hashMap:
        hashMap[''] = 0

    words_count = [(-value, key) for key,value in hashMap.items()]
    heapq.heapify(words_count)
    result = []
    for i in range(min(20, len(words_count))):
        value, key = heapq.heappop(words_count)
        result.append([key, -value])
    return result

def get20MostInterestingFrequentWords(text):
    common_words = open('1-1000.txt', 'r')
    lines_common_words = common_words.readlines()
    
    common_words = []
    for i in range(len(lines_common_words)):
        lines_common_words[i] = re.sub(r'[^a-zA-Z]+', ' ', lines_common_words[i])
        lines_common_words[i] = lines_common_words[i].rstrip()
        lines_common_words[i] = lines_common_words[i].lower()
        lines_common_words[i] = lines_common_words[i].split(" ")
        for word in lines_common_words[i]:
            common_words.append(word)

            
            
    
    text_file = open(text, 'r')
    lines = text_file.readlines()
    
    
    
    hashMap = defaultdict(int)
    
    res = []
    for i in range(8, len(lines)-370):
        lines[i] = re.sub(r'[^a-zA-Z]+', ' ', lines[i])
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].lower()
        lines[i] = lines[i].split(" ")
        for word in lines[i]:
            hashMap[word] += 1
    if '' in hashMap:
        del hashMap['']

    words_count = [(-value, key) for key,value in hashMap.items()]
    heapq.heapify(words_count)
    result = []
    while len(result) != min(20, len(words_count)):
        value, key = heapq.heappop(words_count)
        if key not in common_words:
            result.append([key, -value])
    return result

def get20LeastFrequentWords(text):
    text_file = open(text, 'r')
    lines = text_file.readlines()
    
    
    
    hashMap = defaultdict(int)
    
    res = []
    for i in range(8, len(lines)-370):
        lines[i] = re.sub(r'[^a-zA-Z]+', ' ', lines[i])
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].lower()
        lines[i] = lines[i].split(" ")
        for word in lines[i]:
            hashMap[word] += 1
    if '' in hashMap:
        del hashMap['']

    words_count = [(value, key) for key,value in hashMap.items()]
    heapq.heapify(words_count)
    result = []
    for i in range(20):
        value, key = heapq.heappop(words_count)
        result.append([key, value])
    return result

def get_chapters(text):
    text_file = open('98.txt', 'r')
    lines = text_file.readlines()
    chapter = {}
    
    idx = 0
    last_idx = 0
    for i in range(8, len(lines)-370):
        lines[i] = re.sub(r'[^a-zA-Z]+', ' ', lines[i])
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].lower()
        lines[i] = lines[i].split(" ")
        if "chapter" in lines[i]:
            chapter[idx] = "".join(lines[i])
            idx += 1
            last_idx = i + 1

    return chapter, last_idx


def getFrequencyOfWord(word):
    chapter, last_idx = get_chapters('98.txt')
 
    count, idx = 0, 0
    
  
    text_file = open('98.txt', 'r')
    lines = text_file.readlines()
    result = [0] * len(chapter)
    idx = 0
    
    for i in range(last_idx, len(lines)-370):
        
        lines[i] = re.sub(r'[^a-zA-Z]+', ' ', lines[i])
        lines[i] = lines[i].lower()
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].split(" ")
        joinPart = "".join(lines[i])
        joinPart = "chapter" + joinPart

        
        if idx + 1 < len(chapter) and joinPart == chapter[idx + 1]:
            
            result[idx] = count
            idx += 1
            count = 0
        else:
            for w in lines[i]:
                if w == word:
                    count += 1
        result[idx] = count
    return result
    
    
def getChapterQuoteAppears(quote):

    chapter, last_idx = get_chapters('98.txt') 
    
    quote = re.sub(r'[^a-zA-Z]+', ' ', quote)
    quote = quote.lower()
    quote = quote.rstrip()
    quote = quote.split(" ")
        
#     quote = quote.split(" ")
    
    index = 0
    idx = 0
    text_file = open('98.txt', 'r')
    k = 0
    lines = text_file.readlines()
    for i in range(last_idx, len(lines)-370):
#         print(lines[i])
#         if k == 100:
#             return
#         k += 1
        lines[i] = re.sub(r'[^a-zA-Z]+', ' ', lines[i])
        lines[i] = lines[i].lower()
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].split(" ")
        joinPart = "".join(lines[i])
        joinPart = "chapter" + joinPart

        
        

        if idx + 1 < len(chapter) and joinPart == chapter[idx + 1]:
            idx += 1
        else:
            for w in lines[i]:
                if w == quote[index] and index != len(quote) - 1:
                    index += 1
                elif w == quote[index] and index == len(quote) - 1:
                    return idx, chapter[idx]
                else:
                    index = 0


    return -1

def generateSentence():
    word = "The"
    string = "The"
    text_file = open('98.txt', 'r')
    lines = text_file.readlines()
    def generate_next_word(string, lines):

        next_words = []
        for i in range(8, len(lines)-370):
            line = lines[i]
            line = re.sub(r'[^a-zA-Z]+', ' ', line)
            line = line.rstrip()
            line = line.split(" ")
            add_word = 0
            for j in range(len(line)):
                if add_word == 1:
                    next_words.append(line[j])
                    add_word = 0
                elif line[j] == string and j < len(line) - 1:
                    next_words.append(line[j+1])
                elif line[j] == string and j == len(line) - 1:
                    add_word = 1
        return next_words
        
                
            
            
    i = 0
    while i < 19:
        next_words = generate_next_word(word, lines)
        if len(next_words) != 0:
            idx = random.randint(0, len(next_words)-1)
            word = next_words[idx]
            string = string + " " + word
            i += 1

    return string


