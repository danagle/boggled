"""Unit tests for BoggleDice() class."""
import builtins
import pytest
from unittest.mock import call, mock_open, patch

from boggled import BoggleDice


class TestDice():
    """Test the BoggleDice class"""

    file_content = """ABCDEF
GHIJKL
MNOPQR
STUVWX"""

    def test_instance_is_created(self):
        """Verify instance of BoggleDice() class is instantiated."""
        # Instantiate dice
        _dice = BoggleDice()
        # Assert instance type
        assert isinstance(_dice, BoggleDice)
        assert len(_dice.dice) == 0

    def test_can_add_dice_from_string(self):
        """Verify tokens from a string are added."""
        _token_str = 'ABCDEF'
        _expected = tuple([ch for ch in _token_str])
        _dice = BoggleDice()
        # Use the _token_str string
        _dice.addDiceFromTokensString(_token_str)
        # Assert the dice property is populated
        assert len(_dice.dice) == 1
        assert _dice.dice[0].tiles == _expected

    def test_can_hold_multiple_dice(self):
        """Verify container can hold multiple dice."""
        _tokens = ['ABCD', 'EFGH', 'ABCD', 'H I J K']
        _dice = BoggleDice()
        # Use the _tokens list of strings
        for token_str in _tokens:
            _dice.addDiceFromTokensString(token_str)
        # Assert the correct number of dice were added
        assert len(_dice.dice) == len(_tokens)

    def test_letters_property_contains_valid_data(self):
        """Verify the letters property returns the correct values."""
        _tokens = ['ABCDEG', 'ABCDEF', 'CH QU CH TH E E']
        expected = {'A': 2, 'B': 2, 'C': 2, 'D': 2, 'E': 3, 'F': 1, 'G': 1,
                    'CH': 1, 'QU': 1, 'TH': 1}
        # Prepare the container
        _dice = BoggleDice()
        assert len(_dice.letters) == 0
        for token_str in _tokens:
            _dice.addDiceFromTokensString(token_str)
        assert len(_dice.letters) == 10
        for token in expected.keys():
            assert _dice.letters[token] == expected[token]

    def test_the_shake_method_returns_a_result(self):
        """Verify shake() does something."""
        _tokens = ['A A A', 'A A A', 'A A A']
        _expected = ['A', 'A', 'A']
        # Prepare the container
        _dice = BoggleDice()
        for token_str in _tokens:
            _dice.addDiceFromTokensString(token_str)
        # Shake the container
        result = _dice.shake()
        # Assert the expected result
        assert result == _expected

    def test_the_result_of_shake_is_stored(self):
        """Verify shake() stores the result in its lastRoll property"""
        _tokens = ['A A A', 'B B B', 'C C C']
        # Prepare the container
        _dice = BoggleDice()
        for token_str in _tokens:
            _dice.addDiceFromTokensString(token_str)
        # Shake the container
        result = _dice.shake()
        # Assert the lastRoll property has the result
        assert result == _dice.lastRoll

    @patch('builtins.open', new_callable=mock_open, read_data=file_content)
    @patch.object(BoggleDice, 'addDiceFromTokensString')
    def test_loadFromFile_method_reads_file_content(self, mock_method, mock_file):
        """Verify dice can be imported from a file."""
        expected = [call('ABCDEF'), call('GHIJKL'),
                    call('MNOPQR'), call('STUVWX')]
        _file_path = '/path/to/open/file.txt'
        # Load the test data!
        _dice = BoggleDice()
        _dice.loadFromFile(_file_path)
        # Assert the mocked file was opened
        mock_file.assert_called_once_with(_file_path, 'r')
        # Verify 'iteratorPopulateTrie()' was called the correct number of times
        assert mock_method.call_count == len(expected)
        # Confirm the 'iteratorPopulateTrie' method calls were as expected
        mock_method.assert_has_calls(expected)
