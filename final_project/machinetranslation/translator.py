import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('rpT5TFewQ4HnPai3fe7YY-48TRzdHDNsVF4EiPDRnoDH')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(
    'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/9d9d7e4c-d96b-499b-b6a8-205d909a313a'
)

def english_to_french(english_text):
    french_text=language_translator.translate(
        english_text, model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    english_text=language_translator.translate(
        french_text, model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']
