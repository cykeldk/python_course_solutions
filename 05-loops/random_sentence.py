# adjectives from: http://www.enchantedlearning.com/wordlist/adjectives.shtml
# nouns from: http://www.talkenglish.com/vocabulary/top-1500-nouns.aspx

import random

file_names = {'nouns':'dirty_noun_list.txt', 'adjectives': 'clean_adjective_list.txt'}
word_lists = {'nouns': [], 'adjectives':[]}

def read_data(file_name):
    res = []
    with open(file_name) as f:
        for line in f:
            if line.strip():
                words = line.split()
                res.append(words[0])
    return res

for k, v in file_names.items():
    word_lists[k] = read_data(v)
'''
for noun in word_lists['nouns']:
    print(noun)

for adjective in word_lists['adjectives']:
    print(adjective)
'''
def generate_group_names(amount):
    res = []
    for i in range(20):
        a = random.choice(word_lists['adjectives'])
        n = random.choice(word_lists['nouns'])
        temp = '{0} {1}'.format(a,n)
        res.append(temp)
    return res


print(generate_group_names(20))
