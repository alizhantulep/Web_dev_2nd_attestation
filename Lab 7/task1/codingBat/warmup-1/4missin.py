def missing_char(str, n):
  sew = ""
  for i in range(len(str)):
    if i != n:
      sew = sew + str[i]
  return sew


