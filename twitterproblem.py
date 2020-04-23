# similarity score +1 for each same letter -1 for each not same letter
def similarity(newhandle, handles, k):
  letterdict = {}
  handlevalues = []
  output = []
  for letter in newhandle:
    if letter in letterdict:
      letterdict[letter] += 1
    else:
      letterdict[letter] = 1
  for handle in handles:
    score = 0
    for letter in handle:
      if letter in letterdict:
        score += 1
      else:
        score -= 1
    handlevalues.append((handle, score))
  handlevalues.sort(key=lambda a: a[1], reverse=True)
  for i in range(k):
    output.append(handlevalues[i][0])
  return output
  

print(similarity('iLoveDogs', ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust'], 3))