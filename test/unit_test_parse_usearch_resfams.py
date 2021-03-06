import unittest

#Test first function - create_bacteria_dict
from parse_usearch_resfams_output import create_bacteria_dict

class TestCreateBactDict(unittest.TestCase):

	def test_createdict(self):
		self.input = open('test_resfams_input.txt','r')
		expected = {'Bug1': {'abx-gene1': 2, 'abx-gene2': 1}, 'Bug2': {'abx-gene1': 1}, 'Bug3': {'abx-gene1': 1}, 'Bug4': {'abx-gene3': 1}, 'Bug5': {'abx-gene3': 1, 'abx-gene4': 1, 'abx-gene6': 1, 'abx-gene7': 1}} 
		actual = create_bacteria_dict(self.input)
		self.assertEqual(actual, expected)
		
#Test second function - get_resfams_IDs		
from parse_usearch_resfams_output import get_resfams_IDs

class TestGetResfams(unittest.TestCase):

	def test_getresfams(self):
		self.resfams_map = open('test_resfams_map.txt', 'r')
		expected = set(['abx-gene1','abx-gene2','abx-gene3','abx-gene4','abx-gene5','abx-gene6','abx-gene7','abx-gene8','abx-gene9','abx-gene10'])
		actual = get_resfams_IDs(self.resfams_map)
		self.assertEqual(actual, expected)
		
#Test third function - write header
#from parse_usearch_resfams_output import write_header

#class TestWriteHeader(unittest.TestCase):

#	def test_writeheader(self):
#		self.refams_ids = ?
#		expected = ?
#		actual = write_header(self.resfams_ids????)
#		self.assertEqual(actual, expected)

#Test fourth function - write rows
#from parse_usearch_resfams_output import write_rows

#class TestWriteHeader(unittest.TestCase):

#	def test_writeheader(self):
#		self.img_Ids = ?
#		expected = ?
#		actual = write_rows(self.resfams_ids????)
#		self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
