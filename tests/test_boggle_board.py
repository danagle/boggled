"""Unit tests for BoggleBoard() class."""
import pytest

from boggled import BoggleBoard


class TestDice():
    """Test the BoggleBoard class"""

    def test_01_instance(self):
        """Verify instance of BoggleDice() class is instantiated."""
        # Instantiate empty board
        board = BoggleBoard()
        # Assert instance type
        assert isinstance(board, BoggleBoard) == True
        # Assert the tiles property is None
        assert board._tiles is None

    def test_02_instance_with_tiles(self):
        """Verify tokens from a string are added."""
        _letters = 'A B C D'
        # Instantiate board
        board = BoggleBoard(_letters)
        # Assert the neighbors property is populated
        assert len(board.neighbors) == 4
        # Assert the tiles property is populated
        assert len(board.tiles) == 4
        # Assert the columns property is populated
        assert board.columns == 2
        # Assert the rows property is populated
        assert board.rows == 2
        # Assert the rangeLimit property is populated
        assert board.rangeLimit == 5

    def test_03_instance_with_6_letters(self):
        """6 letters creates a 2x3 board."""
        _letters = 'ABCDEF'
        # Instantiate board
        board = BoggleBoard(_letters)
        # Assert the neighbors property is populated
        assert len(board.neighbors) == 6
        # Assert the tiles property is populated
        assert len(board.tiles) == 6
        # Assert the columns property is populated
        assert board.columns == 2
        # Assert the rows property is populated
        assert board.rows == 3
        # Assert the rangeLimit property is populated
        assert board.rangeLimit == 7

    def test_04_instance_with_18_letters(self):
        """6 letters creates a 3x6 board."""
        _letters = 'ABCDEF GHIJKL MNOPQR'
        # Instantiate board
        board = BoggleBoard(_letters)
        # Assert the neighbors property is populated
        assert len(board.neighbors) == 18
        # Assert the tiles property is populated
        assert len(board.tiles) == 18
        # Assert the columns property is populated
        assert board.columns == 3
        # Assert the rows property is populated
        assert board.rows == 6
        # Assert the rangeLimit property is populated
        assert board.rangeLimit == 19

    def test_05_invalid_position_index_error(self):
        """positionNeighbors() raises an IndexError for an invalid value."""
        _letters = 'ABCDEF'
        # Instantiate board
        board = BoggleBoard(_letters)
        # Should raise an error
        with pytest.raises(IndexError):
            board.positionNeighbors(42)

    def test_06_tiles_setter(self):
        """Adding new tiles from a string recreates the board."""
        _letters = 'A B C D'
        # Instantiate board
        board = BoggleBoard(_letters)
        # Assert the properties are populated
        assert len(board.neighbors) == 4
        assert len(board.tiles) == 4
        assert board.columns == 2
        assert board.rows == 2
        assert board.rangeLimit == 5
        # Change the letters by calling the tiles setter
        board.tiles = 'ZYXWVU'
        # Assert the board properties have changed
        assert len(board.neighbors) == 6
        assert len(board.tiles) == 6
        assert board.columns == 2
        assert board.rows == 3
        assert board.rangeLimit == 7
