import random

grammar = {
        "_S"  : ["_N", "_V", "_N"],
        "_N"  : ["developer", "teacher", "student"],
        "_V"  : ["learns", "trains", "tests", "is", "studies", "asks"]
}

def make_sentence(index=0, sentence=[]):
    if index > len(grammar['_S'])-1:
        #print('done')
        return(' '.join(sentence))
    else:
        #print('should add stuff')
        key = grammar['_S'][index]
        sentence.append(random.choice(grammar[key]))
        #print('sentence so far: {0}'.format(sentence))
        return make_sentence(index+1, sentence)



# print(make_sentence())
# val2 = make_sentence()
print('prog result: {0}'.format(make_sentence()))
