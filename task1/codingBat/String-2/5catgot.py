def cat_dog(str):
  count=0
  countt=0
  for i in range (len(str)):
    if str[i:i+3] == "cat":
      count=count+1
    elif str[i:i+3] == "dog":
      countt=countt+1
  return countt == count
