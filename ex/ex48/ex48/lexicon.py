directions = ['north', 'south', 'east', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def scan(sentence):
    """split the sentence into words and then save the type and word in a tuple"""
    words = sentence.split()
    new_sentence = []
    for word in words:
        if word.lower() in directions:
            new_sentence.append(('direction', word.lower()))
        elif word.lower() in verbs:
            new_sentence.append(('verb', word.lower()))
        elif word.lower() in stops:
            new_sentence.append(('stop', word.lower()))
        elif word in nouns:
            new_sentence.append(('noun', word))
        elif not word.isdigit():
            new_sentence.append(('error', word))
    for i in range(len(words)):
        if (words[i]).isdigit():
            new_sentence.append(('number', int(words[i])))

    return new_sentence
