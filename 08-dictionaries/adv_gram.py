import random
import re

grammar = {
    "_S"  : ["_NP _VP"],
    "_NP" : ["_N", "_A _NP _P _A _N"],
    "_VP" : ["_V", "_V _NP"],
    "_N"  : ["developer", "teacher", "student"],
    "_A"  : ["smart", "interesting", "nice", "desperate", "anoying"],
    "_P"  : ["about", "near"],
    "_V"  : ["learns", "trains", "tests", "is", "studies", "asks"]
}

def create_sentence(g, sentence="_S"):
    done = True
    patterns = ["_[A-Z]", "_[A-Z]{2}"]
    for pattern in patterns:

        if re.search(pattern, sentence):
            done = False

    if done:
        return sentence

#    print('{0} is {1} characters long'.format(sentence, len(sentence)))

    to_be_replaced = ""
    start = sentence.find("_")
    if start >= 0:
        count = start +1
        while count < len(sentence) and sentence[count].isupper and sentence[count] != " ":
#            print('count: {0}; sentence: {1}'.format(str(count), sentence[count]))
            count+=1

        to_be_replaced = sentence[start:count]

        if start == 0 and count >= len(sentence) -1:
#            print('start was 0, and count was {0}'.format(len(sentence) - count))
            return create_sentence(g, random.choice(g[sentence]))

        elif (count>=len(sentence)-1):
            parts = []
            parts.append(sentence[:start])
            parts.append(random.choice(g[sentence[start:]]))
            sentence = ' '.join(parts)
            return create_sentence(g, sentence)

        else:
            parts = []
            parts.append(sentence[:start])
            parts.append(random.choice(g[to_be_replaced]))
            parts.append(sentence[count+1:])
            sentence = ' '.join(parts)
            return create_sentence(g, sentence)

#        print('to be replaced:{0}'.format(to_be_replaced))
#    print('sentence: {0}'.format(sentence))

result = create_sentence(grammar)
print('result: {0}'.format(result))
