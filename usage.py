# import  argostranslate.translate
from argostranslate import translate
from pathlib import Path


from_code1 = "he"
from_code2 = "en"
to_code = "fa"

installed_languages = translate.get_installed_languages(package_path= Path(r"D:.\src\argos-translate\packages"))
from_lang = list(filter(
    lambda x: x.code == from_code1,
    installed_languages))[0]
to_lang1 = list(filter(
    lambda x: x.code == from_code2,
    installed_languages))[0]
to_lang2 = list(filter(
    lambda x: x.code == to_code,
    installed_languages))[0]


translation_he2en = from_lang.get_translation(to_lang1)
translation_en2fa = to_lang1.get_translation(to_lang2)

translatedText = translation_he2en.translate("בשיחה שנערכה בין אבו מאזן לבין שולץ עוד קודם לכן, דחה הקנצלר הגרמני את טענותיו שישראל מקיימת משטר אפרטהייד - והבהיר כי מבחינתו אין זה הזמן להכיר ברשות הפלסטינית כמדינה, למרות בקשותיו החוזרות ונשנות של אבו מאזן.")
final_translate = translation_en2fa.translate(translatedText)

print(translatedText)
print(final_translate)

# '¡Hola Mundo!'
