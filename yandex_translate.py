import requests
import json
import os

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def get_args():
	current_path = str(os.path.dirname(os.path.abspath(__file__)))
	f_documents = os.path.join(current_path, 'fixtures/translation_args.json')
	with open(f_documents, 'r') as out_docs:
		text = json.load(out_docs).get('text')
		from_lang = json.load(out_docs).get('from_lang')
		to_lang = json.load(out_docs).get('to_lang')
	return text, from_lang, to_lang


def translate_it(text, from_lang, to_lang):
	"""
	ПОРЯДОК ПЕРЕДАЧИ АРГУМЕНТОВ:
	1* - ручной ввод текста для перевода
	2 - язык с которого переводим
	3 - язык на который переводим (по умолчанию русский)
	"""

	params = {
		'key': API_KEY,
		'text': text,
		'lang': '{0}-{1}'.format(from_lang, to_lang),
		# если в поле lang оставить только переменную to_lang, можно будет не указывать исходный язык и тогда
		# можно было бы пользоваться функцией в упрощенном варианте, передавая ей только текст, а она бы переводила
		# его на русский.
	}

	response = requests.get(URL, params=params)

	return response
	# json_ = response.json()
	#
	# return ''.join(json_['text'])


if __name__ == '__main__':
	# text, from_lang, to_lang = get_args()
	#
	# json_ = translate_it(text, from_lang, to_lang).json()
	# print(translate_it(text, from_lang, to_lang).status_code)
	# print(json_)
	pass