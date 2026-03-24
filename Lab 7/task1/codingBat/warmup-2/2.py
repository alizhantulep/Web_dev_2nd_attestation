def string_splosion(str):
  strr = ""
  for i in range(len(str)):
    strr = strr + str[0:i]
  return strr+str