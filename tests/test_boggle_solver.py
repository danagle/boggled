"""Unit tests for BoggleDice() class."""
import pytest
from unittest.mock import Mock, patch

from boggled import BoggleBoard, BoggleSolver, BoggleWords, TrieNode
import boggled


class TestBoggleSolver:

    def mockedBoggleBoard(self):
        _neighbors = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 4], 4: [1, 2, 3]}
        _rangeLimit = 5
        _tiles = {1: 'O', 2: 'B', 3: 'K', 4: 'O'}
        return Mock(BoggleBoard, neighbors=_neighbors, rangeLimit=_rangeLimit, tiles=_tiles)

    def mockedBoggleWords(self):
        _minLength = 3
        _words = ['BOOK']
        _prefixes = ['BOO']
        return Mock(BoggleWords, minLength=_minLength, words=_words, prefixes=_prefixes)

    def setup_solver_dependencies(self):
        _board = BoggleBoard('OBOK')
        _words = BoggleWords()
        _words.iteratorPopulateTrie(['book', 'cook', 'look', 'took'])
        return (_board, _words)

    def iterPrefixPaths(self, prefix: str=None, path: list=None):
        for _tuple in [('BOO', [2, 1, 4], None), ('BOO', [2, 4, 1], None)]:
            yield _tuple

    def iterFoundWords(self, prefix: str=None, path: list=None, node: TrieNode=None):
        for _found in [('BOOK', [2, 1, 4, 3]), ('BOOK', [2, 4, 1, 3])]:
            yield _found

    def test_instance_is_valid(self):
        """A BoggleSolver instance is created"""
        # Test setup
        mock_board = self.mockedBoggleBoard()
        mock_words = self.mockedBoggleWords()
        solver = BoggleSolver(mock_board, mock_words)
        # Assert instance type
        assert isinstance(solver, BoggleSolver)

    def test_board_properties_are_accessible(self):
        """BoggleBoard properties are accessible from BoggleSolver instance"""
        # Expected results
        _neighbors = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 4], 4: [1, 2, 3]}
        _rangeLimit = 5
        _tiles = {1: 'O', 2: 'B', 3: 'K', 4: 'O'}
        # Test setup
        mock_board = self.mockedBoggleBoard()
        mock_words = self.mockedBoggleWords()
        # Perform the test
        solver = BoggleSolver(mock_board, mock_words)
        # Assert that the properties are accessible
        assert _neighbors == solver.boardNeighbors
        assert _rangeLimit == solver.boardRangeLimit
        assert _tiles == solver.boardTiles
        assert mock_board == solver.board

    def test_dictionary_properties_are_accessible(self):
        """BoggleWords properties are accessible from BoggleSolver instance"""
        # Expected results
        _minLength = 3
        _prefixes = ['BOO']
        _words = ['BOOK']
        # Test setup
        mock_board = self.mockedBoggleBoard()
        mock_words = self.mockedBoggleWords()
        # Perform the test
        solver = BoggleSolver(mock_board, mock_words)
        # Assert that the properties are the same
        assert _minLength == solver.minWordLength
        assert _prefixes == solver.prefixes
        assert _words == solver.dictionary

    def test_solve_method_populates_found_property(self):
        """'solve' method populates '_found' property"""
        # Test setup
        _board, _words = self.setup_solver_dependencies()
        solver = BoggleSolver(_board, _words)
        # Call the solve method
        solver.solve()
        # Check the results
        assert len(solver._found) == 1
        assert 'BOOK' in solver._found
        assert solver.found is solver._found
        assert (2, 1, 3, 4) in solver.found['BOOK']
        assert (2, 3, 1, 4) in solver.found['BOOK']
        assert len(solver.foundWords) == 1
        assert 'BOOK' in solver.foundWords
