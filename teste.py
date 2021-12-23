import qrcode
from PIL import Image, ImageOps
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

face = ImageOps.expand(Image.open('img/whatsapp-black.png').resize((96, 96)), fill='white', border=7)
#face.load() # required for png.split()

#background = Image.new("RGB", face.size, (255, 255, 255))
#background.paste(face, mask=face.split()[3]) # 3 is the alpha channel

#background.save('img/zapblack.jpg', 'JPEG', quality=100)

#face = Image.open('img/zapblack.jpg')

qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_Q
)

qr.add_data('https://api.whatsapp.com/send?phone=5588981656639&text=Hello%20there!')
img_qr_big = qr.make_image().convert('RGB') #image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer()

pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)

img_qr_big.paste(face, pos)
img_qr_big.save('whatsappblack.png')