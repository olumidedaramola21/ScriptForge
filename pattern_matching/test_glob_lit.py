from glob_lit  import Lit

def test_literal_match_entire_string():
    # /abc/ matches "abc"
    assert Lit("abc").match("abc")

def test_literal_substring_alone_no_match():
    # /ab/ does not match "abc"
    assert not Lit("ab").match("abc")

def test_literal_superstring_no_match():
    # /abc/ does not match "ab"
    assert not Lit("abc").match("ab")

def test_litral_followed_by_literal_match():
    # /a/+/b/ matches "ab"
    assert Lit("a", Lit("b")).match("ab")