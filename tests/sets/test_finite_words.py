r"""Finite words and multisets are the length-graded coproducts of their pieces."""

from dzack_research.preamble.all import NN, finite_ordered_set


def test_empty_alphabet_has_exactly_the_empty_word_or_multiset():
    alphabet = finite_ordered_set(())
    for words in (alphabet.finite_words(), alphabet.finite_multisets()):
        assert words.cardinality() == 1
        assert words.cofactor(NN(0)).cardinality() == 1
        assert words.cofactor(NN(3)).cardinality() == 0
        empty, = tuple(words)
        assert empty.summand_index() == 0
        assert words.ranking_map().inverse()(words.ranking_map()(empty)) == empty


def test_word_and_multiset_lengths_use_the_existing_finite_set_constructions():
    alphabet = finite_ordered_set(("a", "b"))
    words = alphabet.finite_words()
    multisets = alphabet.finite_multisets()
    assert words.cardinality().is_countably_infinite()
    assert multisets.cardinality().is_countably_infinite()
    assert words.cofactor(NN(2)).cardinality() == 4
    assert multisets.cofactor(NN(2)).cardinality() == 3
    assert alphabet.finite_words() is words
    assert alphabet.finite_multisets() is multisets
    ab = words(NN(2), words.cofactor(NN(2))(lambda i: "a" if int(i) == 0 else "b"))
    ba = words(NN(2), words.cofactor(NN(2))(lambda i: "b" if int(i) == 0 else "a"))
    assert ab != ba
    assert words.ranking_map().inverse()(words.ranking_map()(ab)) == ab
