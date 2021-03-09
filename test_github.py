import unittest
import github


class TestlistRepos(unittest.TestCase):
    def test_user1(self):  # i'm not sure where to find more github users with inactive repos so these tests wont break when more commits are made
        self.assertEqual(github.listRepos("richkempinski"), [['csp', 2], ['hellogitworld', 30], ['helloworld', 6], ['Mocks', 10], [
                         'Project1', 2], ['richkempinski.github.io', 9], ['threads-of-life', 1], ['try_nbdev', 2], ['try_nbdev2', 5]])
        self.assertEqual(github.listRepos("Richkempinski"), [['csp', 2], ['hellogitworld', 30], ['helloworld', 6], ['Mocks', 10], [
                         'Project1', 2], ['richkempinski.github.io', 9], ['threads-of-life', 1], ['try_nbdev', 2], ['try_nbdev2', 5]])
    
    def test_invalidUser(self):
        self.assertRaises(TypeError, github.listRepos, "3782749817") # this random github username doesn't exist and thus will raise a TypeError due to the invalid api response
        self.assertRaises(TypeError, github.listRepos, "") # similarly, if no username is provided a TypeError will also be raised

if __name__ == '__main__':
    unittest.main(exit=True)
