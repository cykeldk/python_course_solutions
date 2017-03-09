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

def make_sentence(g, sentence=''):
    if sentence == '':
        sentence = '_S'

    print('sentence so far:{0}.'.format(sentence))

    if '_' not in sentence:
        print('no underscore - DONE')
        return sentence

    low = sentence.find('_')
    print('low: '.format(str(low))
    #from_low = sentence[low:]
    if len(re.find(" ", sentence)) < 1:
        print('no spaces were found - DONE')
        print('whole sentence:{0}'.format(sentence))
        print('substring:{0}'.format(sentence[:low]))
        print('choice string:{0}'.format(random.choice(sentence[low:-1]))

        if not low:
            sentence = random.choice(sentence)
        else:
            sentence = sentence[:low] + sentence[low:]

        return make_sentence(g, sentence)

    high = sentence.find('_')

    to_be_inserted = random.choice(g[sentence[low:high]])

    sentence = sentence[:low] + to_be_inserted + sentence[high+1:]
    print('sentence so far:{0}'.format(sentence))
    return make_sentence(g, sentence)






print('result: '.format(make_sentence2(grammar)))
