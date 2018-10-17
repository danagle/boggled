import builtins
import pytest
from unittest.mock import mock_open, patch

from boggled import BoggleWords, Trie, TrieNode


class TestBoggleWords:

    file_content = """apple
ball
card
door"""

    def test_trie_node_method_returns_none(self):
        _trie = Trie()
        test_node = _trie.node('ASH')
        assert test_node is None

    def test_child_node_can_locate_parent(self):
        test_class = BoggleWords()
        root = test_class.wordsRoot
        # Add a word to the Trie
        test_class.iteratorPopulateTrie(['TESTING'])
        assert len(root.children) == 1
        assert isinstance(root.children['T'], TrieNode)
        child_T = root.children['T']
        assert child_T.parent is root

    def test_getWordStartNode_return_values(self):
        """_getWordStartNode() returns expected values"""
        _first = 'BOOK'
        _second = 'BOOKS'
        test_class = BoggleWords()
        # Prefixes is empty
        assert test_class.prefixes == {}
        start_node, word, prefix = test_class._getWordStartNode(_first)
        # start_node should be the Trie root node
        assert word in _first
        assert prefix == _first[:3]
        assert start_node is test_class.wordsRoot
        assert isinstance(start_node, TrieNode)
        # Add the word to the Trie
        test_class.iteratorPopulateTrie([_first])
        assert len(test_class.prefixes) == 1
        # Begin the test
        test_node, test_word, test_prefix = test_class._getWordStartNode(
            _second)
        # test_node should be in the prefixes dict()
        assert test_node is test_class.prefixes[_second[:3]]
        # test_word should be the tail end of _second
        assert test_word == _second[3:]
        # test_prefix should be None
        assert test_prefix == None

    @patch('builtins.open', new_callable=mock_open, read_data=file_content)
    @patch.object(BoggleWords, 'iteratorPopulateTrie')
    def test_loadFromFile_method_reads_file_content(self, mock_method, mock_file):
        """'_loadFromFile' opens a file and passes its content to 'iteratorPopulateTrie()'"""
        # Massage file_content into the expected format
        expected = [l + '\n' for l in self.file_content.split()]
        expected[-1] = expected[-1].strip()
        _file_path = '/path/to/open/file.txt'
        # Perform load with the mocked file content
        _words = BoggleWords()
        _words.loadFromFile(_file_path)
        # The mock file was opened
        mock_file.assert_called_with(_file_path, 'r')
        # The mocked 'iteratorPopulateTrie' method was called
        mock_method.assert_called_once_with(expected)
