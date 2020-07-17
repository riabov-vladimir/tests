import unittest
import app
from unittest.mock import patch


class TestSecretary(unittest.TestCase):
	def setUp(self):
		with patch('app.input', return_value='q'):
			app.secretary_program_start()

	def test_move_doc(self):
		with patch('app.input', side_effect=['10006', '3']):
			app.move_doc_to_shelf()
		self.assertIn('10006', app.directories.get('3', []))

	def test_add_new_document(self):
		self.assertNotIn('1234567890', app.directories['3'])
		with patch('app.input', side_effect=['1234567890', 'pasp', 'Max', '3']):
			app.add_new_doc()
		self.assertIn('1234567890', app.directories.get('3', []))

	def test_delete_doc(self):
		self.assertIn('10006', [x['number'] for x in app.documents])
		with patch('app.input', return_value='10006'):
			app.delete_doc()
		self.assertNotIn('10006', [x['number'] for x in app.documents])

	def test_add_shelf(self):
		self.assertNotIn('1234567890', app.directories.keys())
		with patch('app.input', return_value='1234567890'):
			app.add_new_shelf()
		self.assertIn('1234567890', app.directories.keys())

	def test_shelf_number(self):
		with patch('app.input', return_value='10006'):
			app.delete_doc()

