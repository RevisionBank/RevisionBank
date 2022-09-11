from PIL import Image
from io import BytesIO
import base64
import json
with open("exampleimage.json","r") as f:
    img = json.load(f)["exampleimage"]
    #img = f.read()["exampleimage"]
    print(img)

im = Image.open(BytesIO(base64.b64decode(img)))
im.save('image.png', 'PNG')