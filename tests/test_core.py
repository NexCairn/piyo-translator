import pytest
from piyo.core import PiyoTranslator

def test_encode_decode_simple():
    original = "Hello"
    encoded = PiyoTranslator.encode(original)
    decoded = PiyoTranslator.decode(encoded)
    assert decoded == original
    assert all(c in ["ピ", "ヨ"] for c in encoded)

def test_encode_decode_japanese():
    original = "こんにちは"
    encoded = PiyoTranslator.encode(original)
    decoded = PiyoTranslator.decode(encoded)
    assert decoded == original

def test_encode_decode_emoji():
    original = "🐣"
    encoded = PiyoTranslator.encode(original)
    decoded = PiyoTranslator.decode(encoded)
    assert decoded == original

def test_encode_empty():
    assert PiyoTranslator.encode("") == ""
    assert PiyoTranslator.decode("") == ""

def test_invalid_input():
    with pytest.raises(ValueError):
        PiyoTranslator.decode("ピヨピヨあ")

def test_invalid_length():
    # 7 chars (not multiple of 8)
    # 'ピ' is 1 char.
    invalid_piyo = "ピ" * 7
    with pytest.raises(ValueError):
        PiyoTranslator.decode(invalid_piyo)
