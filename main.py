from translate import Translator

translator = Translator(to_lang="ja")

try:
  with open('./test.txt', mode='r') as my_file:
    text=my_file.read()
    print(translator.translate(text))
    with open("./test-ja.txt", mode="w") as myfile2:
      myfile2.write(translator.translate(text))
except FileNotFoundError as e:
  print("check your file path silly!")
  print(e)
