def test_japanese_punctuation():
  from pygoogletranslation import Translator
  t = Translator()
  assert t.translate("おはよう。げんきですか。").text == "Good morning. How are you." #<--- this is how google translate web translates it. Sadly, with the english-point replacement method, the result is different from this, as can be seen in the test.
  assert t.translate("今日、明日").text == "Today, tomorrow"
  # assert t.translate("「こんにちは」").text == "\"Hello\""