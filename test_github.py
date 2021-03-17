import unittest
from unittest.mock import patch
import github


class TestlistRepos(unittest.TestCase):

    @patch("github.requests.get")
    def test_getRepos(self, mock):
        mock.return_value.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
        self.assertEqual(github.getRepos("test"), ['repo1', 'repo2'])

    @patch("github.requests.get")
    def test_getReposInvalid(self, mock):
        mock.side_effect = TypeError
        self.assertRaises(TypeError, github.listRepos)

    @patch("github.requests.get")
    def test_getCommits(self, mock):
        mock.return_value.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
        self.assertEqual(github.getCommits("ID", "test"), 2)
         
   
    @patch("github.getCommits")
    @patch("github.getRepos")
    def test_listRepos(self, getRepos_mock, getCommits_mock):
        getRepos_mock.return_value = ["testRepo1", "testRepo2"]
        getCommits_mock.side_effect = [2, 4]
        self.assertEqual(github.listRepos("ID"), [["testRepo1", 2], ["testRepo2", 4]])


if __name__ == "__main__":
    unittest.main(exit=True)

