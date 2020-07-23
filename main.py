import random

words = []
dictionary = dict()
usedwords = []
nextletter = ''

# テキストファイルから読み込み
def readWords(w):
  with open('dict.txt') as f:
    for s in f.readlines():
      s = s.strip()
      if len(s) > 0:
        w.append(s)
        dictionary.setdefault(s[0],[]).append(s)

# 単語を検索
# 知っていれば True
# 知らなければ False
def searchWord(w):
  firstchar = getFirstLetter(w)
  if not(firstchar in dictionary):
    return False
  if w in dictionary[firstchar]:
    return True
  else:
    return False

# 使った単語リストの検索
# 使っていれば True
# 使われていなければ False
def isUsed(w):
  if w in usedwords:
    return True
  else:
    return False

def addUsed(w):
  usedwords.append(w)

# 辞書に単語を登録する
def addDictionary(w):
  with open('dict.txt','a+') as f:
    firstchar = getFirstLetter(w)
    dictionary.setdefault(firstchar,[]).append(w);
    f.write(w + '\n')

def getFirstLetter(w):
  return w[0]

def getNextLetter(w):
  c = w[-1]
  # c が「ぁぃぅぇぉゃゅょ」なら、「あいうえおやゆよ」にしたい
  sh = 'ぁぃぅぇぉゃゅょ'
  lh = 'あいうえおやゆよ'
  if c in sh:
    c = lh[ sh.index(c) ]
  return c

# 人間の入力した単語を受け取る
# ちゃんとした入力→ 受け取った単語
# 再入力が必要→ False
def receiveWord(w, n):
  if (len(n)>0) and (w[0]!=n):
    print('最初の字が違います。あなたの負け')
    return False
  if w[-1]=='ん':
    print('「ん」で終わりました。あなたの負け')
    return False
  if isUsed(w):
    print('もう使われています。あなたの負け')
    return False
  if not(searchWord(w)):
    while True:
      ans = input('ほんとうにそんな言葉があるんですか？ [1/0] ')
      # print(ans)
      if ans=='1':
        addDictionary(w)
        break
      elif ans=='0':
        print('ずるはいけません')
        return False
  return w

readWords(words)
# print(dictionary)

while True:
  # 人間のターン
  s = input('ひらがなで単語を入力 > ')
  result = receiveWord(s,nextletter)
  if result == False:
    print('おつかれさま！')
    break
  addUsed(result)
  nextletter = getNextLetter(result)
  print('次は [' + nextletter + '] です')
  # print( usedwords )
  # コンピュータのターン

  wl = dictionary.get( nextletter, [] )
  random.shuffle(wl)
  # print(wl)
  for w in wl:
    if not isUsed(w):
      print(w)
      addUsed(w)
      nextletter = getNextLetter(w)
      break
  # else に入るのは「break しなかったとき」
  else:
    print('私の負けです。まいりました')
    break
  

