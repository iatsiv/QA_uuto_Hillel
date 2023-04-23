import pytest

import library


testcases_test_filter_cut_string_positive = [
    ('', ''),
    ('@!дSasdU 5С5С E@s@@S_=23wwdSaffsss', 'SUССESS'),
    ('!@435656fdg@324', ''),
    ('AAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBB', 'AAAAAAAAAAAAAAAAAAAAAAAAA')
]

testcases_test_filter_cut_string_negative = [
    (2.2, TypeError),
    (2, TypeError),
    (True, TypeError),
    ((2, 2), AttributeError)
]


@pytest.mark.parametrize('my_string, expected',
                         testcases_test_filter_cut_string_positive)
def test_filter_cut_string_positive(my_string, expected):
    result = library.filter_cut_string(my_string)
    assert result == expected, 'oops, something went wrong'


@pytest.mark.parametrize('my_string, expected_error',
                         testcases_test_filter_cut_string_negative)
def test_filter_cut_string_negative(my_string, expected_error):
    with pytest.raises(expected_error):
        library.filter_cut_string(my_string)
