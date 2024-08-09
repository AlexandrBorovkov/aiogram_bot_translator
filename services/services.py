from googletrans import Translator


"""translator = Translator()
result = translator.translate('World', src='en', dest='ru')
print(result.src)
print(result.dest)
print(result.origin)
print(result.text)
print(result.pronunciation)
print()
trans = Translator()
print(trans.detect("Hello"))"""


async def translation_func(lang, text):

    if lang == 'en':
        origin = 'en'
        out = 'ru'
    elif lang == 'ru':
        origin = 'ru'
        out = 'en'
    
    translator = Translator()
    result = translator.translate(text, src=origin, dest=out)

    return result.text