from PIL import Image

def importTable(fileName:str) -> list:
  file = open(fileName,"r")
  list =[]
  cle = file.readline().strip("\n").split(",")

  skip = True
  for l in file.readlines():
    dict= {}
    l_split = l.strip("\n").split(",")

    for i in range(len(cle)):
      dict[cle[i]] = l_split[i]

    list.append(dict)
  file.close()
  return list

def occurences(dic:dict) -> dict:
  occ = {}
  for e in dic:
    if not e in occ:
        occ[e] = 1
    else:
        occ[e] += 1

  occSorted = {k: v for k, v in sorted(occ.items(), key=lambda item: item[1], reverse=True)}
  return occSorted

def get_image_as_point(path:str) -> tuple:
  img = Image.open(path).convert('RGB')
  label = path.removeprefix("MyDB/").removesuffix(".png")
  point = []
  for y in range(img.height):
    for x in range(img.width):
         point.append(img.getpixel((x,y))[0])
  return {"label":label,"point":point}

def get_image_from_point(value) -> tuple:
  img = Image.open("Output.png")
  for p in range(784):
         x = int(p%28)
         y = int(p//28)
         gs = int(value["point"][p])
         img.putpixel((x,y),(gs,gs,gs))
  img.save("Output.png")

