def count_code(str):
  co=0
  for i in range(len(str)):
    if (str[i:i+2] == "co" and str[i+3:i+4] == "e"):
      co=co+1
  return co

