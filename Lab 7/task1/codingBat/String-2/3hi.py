def count_hi(str):
  co=0
  for i in range (len(str)):
    if (str[i:i+2] == "hi"):
      co=co+1
  return co
