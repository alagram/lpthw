class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


def peek(word_list):
    """
    word_list is in the form [('verb', 'run'), ('direction', 'north')]
    This function will get the first element of word_list tuple and assing it to word. And then return
    the first element of word. So this function will return 'verb' or None.
    Returns a word or None.
    """
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    """
    When given word_list and another word eg. 'verb' as parameters
    it will pop the first element in word_list and compare the first element of the popped
    tuple to expecting paramter. If this is true it'll return the popped tuple else return None. If word_list
    doesn't exist return None.
    Returns a tuple.
    """
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    """
    Loop and compare the return value in peek() eg. 'stop' to word_type paramter.
    While this is true run match() with given parameters. This function will either
    return a tuple or None.
    Simply put, remove any tuples that have word_type in them.
    """
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    """
    Run skip() with given parameters(this will return a tuple or None).
    If the returned value of peek() equals 'verb', run match and return a tuple that contains 'verb'
    else raise ParserError().
    Returns a tuple or ParserError()
    """
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    """
    run skip() with given paramter and pop that tuple. Run peek() on the next tuple.
    If returned value of peek() equals 'noun', return match() with given paramter.
    Returns a tuple or raise a ParserError() exception.
    """
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    """
    run skip() with given paramters and then run peek().
    If the returned value of peek() equals 'noun', return match() with given paramters.
    Else if the returned value of peek() equals 'verb', return ('noun', 'verb').
    Else raise a ParserError exception.
    """
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    """
    create paramters subj, verb, obj to build and return a Sentence object.
    """
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
