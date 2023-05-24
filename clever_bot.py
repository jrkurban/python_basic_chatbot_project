from cleverbotfree import Cleverbot
from googletrans import Translator

translator = Translator()

def translate_text(who, text, lang):
    text_translated = translator.translate(text, dest =lang)
    print(who, '(', lang, '):', text_translated.text)
    return text_translated.text

@Cleverbot.connect
def chat(bot,user_prompt,bot_prompt):
    while True:
        user_input = input(user_prompt)
        user_input_en = translate_text(user_prompt, user_input, 'en')
        if user_input == "quit":
            break
        reply = bot.single_exchange(user_input_en)
        print(bot_prompt, reply)
        bot_reply_tr = translate_text(bot_prompt, reply, 'tr')
    bot.close()


chat("You:","Cleverbot:")