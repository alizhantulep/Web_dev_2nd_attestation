def xyz_there(str):
  count=0
  countt=0
  for i in range (len(str)):
    if str[i:i+4] == ".xyz":
      count=count+1
    if str[i:i+3] == "xyz":
      countt=countt+1
  return countt > count
