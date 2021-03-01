def test_japanese_punctuation():
  from pygoogletranslation import Translator
  t = Translator()
  assert t.translate("今日は。今晩は").text == "Today. Tonight"
  assert t.translate("今日は、今晩は").text == "Today, tonight"
  # assert t.translate("「こんにちは」").text == "\"Hello\""