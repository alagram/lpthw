from nose.tools import *
from ex48 import parser

def test_peek():
    assert_equal(parser.peek([('verb', 'run'), ('direction', 'north')]), 'verb')
    assert_equal(parser.peek([('stop', 'the'), ('direction', 'north')]), 'stop')
    peek = parser.peek([])
    assert_equal(peek, None)

def test_match():
    assert_equal(parser.match([('stop', 'the'), ('direction', 'north')], 'stop'), ('stop', 'the'))
    assert_equal(parser.match([('verb', 'run'), ('direction', 'north')], 'noun'), None)
    match = parser.match([], 'verb')
    assert_equal(match, None)

def test_skip():
    assert_equal(parser.skip([('stop', 'the'), ('direction', 'north')], 'stop'), None)

def test_parse_verb():
    assert_equal(parser.parse_verb([('stop', 'the'), ('verb', 'run'), ('direction', 'north')]), ('verb', 'run'))
    assert_raises(parser.ParserError, parser.parse_verb, [('stop', 'the'), ('direction', 'north')])

def test_parse_object():
    assert_equal(parser.parse_object([('stop', 'the'), ('noun', 'bear'), ('direction', 'north')]), ('noun', 'bear'))
    assert_equal(parser.parse_object([('stop', 'the'), ('direction', 'north')]), ('direction', 'north'))
    assert_raises(parser.ParserError, parser.parse_object, [('foo', 'bar')])

def test_parse_subject():
    assert_equal(parser.parse_subject([('stop', 'the'), ('noun', 'bear')]), ('noun', 'bear'))
    assert_equal(parser.parse_subject([('stop', 'the'), ('verb', 'run')]), ('noun', 'player'))
    assert_raises(parser.ParserError, parser.parse_subject, [('direction', 'north')])

def test_sentence():
    subj = parser.parse_subject([('stop', 'the'), ('noun', 'bear')])
    verb = parser.parse_verb([('stop', 'the'), ('verb', 'run'), ('direction', 'north')])
    obj = parser.parse_object([('stop', 'the'), ('direction', 'north')])
    sentence = parser.Sentence(subj, verb, obj)
    assert_equal(sentence.subject, "bear")
    assert_equal(sentence.verb, "run")
    assert_equal(sentence.object, "north")
