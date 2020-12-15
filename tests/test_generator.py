from buzz import generator


def test_sample_single_word():
    b = ('foo', 'bar', 'foobar')
    word = generator.sample(b)
    assert word in b


def test_sample_multiple_words():
    c = ('foo', 'bar', 'foobar')
    words = generator.sample(c, 2)
    assert len(words) == 2
    assert words[0] in c
    assert words[1] in c
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
