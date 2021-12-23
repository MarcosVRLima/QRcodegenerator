import qrcode
from PIL import Image, ImageOps

face = ImageOps.expand(Image.open('img/linkedin_icon-icons.com_53609.ico'), border=11, fill='white')
face.load() # required for png.split()

background = Image.new("RGB", face.size, (255, 255, 255))
background.paste(face, mask=face.split()[3]) # 3 is the alpha channel

background.save('img/linkedin_icon-icons.com_53609.jpg', 'JPEG', quality=100)

face = Image.open('img/linkedin_icon-icons.com_53609.jpg')

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_Q
)

qr.add_data('https://www.linkedin.com/in/marcosvrlima/')
qr.make()
img_qr_big = qr.make_image().convert('RGBA')

pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)

img_qr_big.paste(face, pos)
img_qr_big.save('codeqr.png')