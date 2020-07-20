import unittest
import yandex_translate as app


class TestTranslateIt(unittest.TestCase):
	def	setUp(self):
		self.text, self.from_lang, self.to_lang = app.get_args()

	def	test_response_status_code(self):
		self.assertEqual(200, app.translate_it(self.text, self.from_lang, self.to_lang).status_code)

	def test_translation(self):
		self.assertEqual('привет', app.main(self.text, self.from_lang, self.to_lang))

	def test_negative_text_arg_missing(self):
		self.assertEqual(400, app.translate_it(None, self.from_lang, self.to_lang).status_code)


def suite():
	tests = ['test_negative_text_arg_missing', 'test_translation', 'test_response_status_code']

	return unittest.TestSuite(map(TestTranslateIt, tests))



if __name__ == '__main__':
	suites = suite()
	runner = unittest.TextTestRunner(verbosity=2)

	testResult = runner.run(suites)