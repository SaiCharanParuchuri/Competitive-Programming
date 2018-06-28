import unittest
 
class TrieNode:
	def __init__(self):
		self.children = [None]*26
		self.isEndOfWord = False
 
class Trie(object):
	def __init__(self):
		self.root = self.getNode()
 
	def getNode(self):
		return TrieNode()
 
	def _charToIndex(self,ch):
		return ord(ch)-ord('a')
 
 
	def add_word(self,key):
		if self.search(key):
			return False
		else:
			rootNode = self.root
			length = len(key)
			for level in range(length):
				index = self._charToIndex(key[level])
				if not rootNode.children[index]:
					rootNode.children[index] = self.getNode()
				rootNode = rootNode.children[index]
			rootNode.isEndOfWord = True
			return True
			
	def search(self, key):
		rootNode = self.root
		length = len(key)
		for level in range(length):
			index = self._charToIndex(key[level])
			if not rootNode.children[index]:
				return False
			rootNode = rootNode.children[index] 
		return rootNode != None and rootNode.isEndOfWord


# Tests

class Test(unittest.TestCase):

	def test_trie_usage(self):
		trie = Trie()

		result = trie.add_word('catch')
		self.assertTrue(result, msg='new word 1')

		result = trie.add_word('cakes')
		self.assertTrue(result, msg='new word 2')

		result = trie.add_word('cake')
		self.assertTrue(result, msg='prefix of existing word')

		result = trie.add_word('cake')
		self.assertFalse(result, msg='word already present')

		result = trie.add_word('caked')
		self.assertTrue(result, msg='new word 3')

		result = trie.add_word('catch')
		self.assertFalse(result, msg='all words still present')

		result = trie.add_word('')
		self.assertTrue(result, msg='empty word')

		result = trie.add_word('')
		self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)