"""Unit tests for Dice() class."""
import pytest

from boggled import Dice

def fixture_ABCDEF():
    _tokens = 'A B C D E F'
    _tuple = ('A', 'B', 'C', 'D', 'E', 'F')
    _dice = Dice(_tokens)
    return (_dice, _tuple)

class TestDice():
    """Test the Dice class"""

    def test_01_instance(self):
        """Verify instance of Dice() class is instantiated."""
        # Instantiate dice
        my_dice = Dice()
        # Assert instance type
        assert isinstance(my_dice, Dice) == True

    def test_02_tiles(self):
        """Verify tokens are stored as a tuple."""
        _dice, _tuple = fixture_ABCDEF()
        # Assert tuple is stored
        assert isinstance(_dice.tiles, tuple) == True
        # Assert tuples are equal
        assert _dice.tiles == _tuple

    def test_03_roll(self):
        """Verify roll() returns a valid result."""
        _dice, _tuple = fixture_ABCDEF()
        result = _dice.roll()
        # Assert a string is returned
        assert isinstance(result, str) == True
        # Assert the result is in the tuple
        assert result in _tuple

    def test_04_lastRoll(self):
        """Verify lastRoll() returns the previous result."""
        _dice, _ = fixture_ABCDEF()
        result = _dice.roll()
        expected = _dice.lastRoll
        # Assert the values are equal
        assert result == expected

    def test_05_iterator_raises_error(self):
        """Verify next() raises an error for an empty dice."""
        # Instantiate dice without tokens
        my_dice = Dice()
        # Assert the iterator raises StopIteration
        with pytest.raises(StopIteration):
            next(my_dice)

    def test_06_iterator_returns_result(self):
        """Verify next() returns a valid result."""
        _dice, _tuple = fixture_ABCDEF()
        result = next(_dice)
        expected = _dice.lastRoll
        # Assert the values are equal
        assert result == expected
