from flask import Flask, request
from argostranslate import translate
from langdetect import detect, DetectorFactory
from pathlib import Path

installed_languages = translate.get_installed_languages(package_path= Path(r"src/argos-translate/packages"))
from_lang = list(filter(
    lambda x: x.code == "he",
    installed_languages))[0]
to_lang1 = list(filter(
    lambda x: x.code == "en",
    installed_languages))[0]
to_lang2 = list(filter(
    lambda x: x.code == "fa",
    installed_languages))[0]

# translate from hebrew to english
translation_he2en = from_lang.get_translation(to_lang1)
# translate from english to persian
translation_en2fa = to_lang1.get_translation(to_lang2)





app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/translate', methods=['POST'])
def prepare_text():
    request_data = request.get_json()

    sent = request_data['text']

    # Detect language of text
    try:
        DetectorFactory.seed = 0
        lang = detect(sent)
    except:
        return "No text enter", 400

    if lang != "he":
        return "the language is not Hebrew, please type Hebrew language to translate.", 400

    if len(sent) < 10:
        return "your text is too small, please type more words to detect", 400

    final_dict = {"translate": ""}

    translatedText = translation_he2en.translate(sent)

    trans_sent = translation_en2fa.translate(translatedText)

    # trans_sent = translate_he2fa(sent)
    final_dict["translate"] = trans_sent

    # Return on a JSON format
    return final_dict


@app.route('/check', methods=['GET'])
def check():
    return "every things right! "


if __name__ == '__main__':
    app.run(host='0.0.0.0')
