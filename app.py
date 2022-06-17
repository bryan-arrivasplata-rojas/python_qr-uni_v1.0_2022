import qrcode
from PIL import Image

def createQR(imagenlogo,url,path):
    logo = Image.open(imagenlogo)

    # Ajustamos el tamaño de la imagen
    hsize = int((float(logo.size[1])*float(500/float(logo.size[0]))))
    logo = logo.resize((500, hsize), Image.ANTIALIAS)
    #QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    QRcode = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size = 40,
            border=2,
        )
    # Llenamos de datos el código QR
    QRcode.add_data(url)
    QRcode.make

    # Le damos un color al código y un color al fondo
    QRcolor = '#800404'
    QRfondo = '#ffffff'

    # Agregamos nuestra imagen al código QR
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color=QRfondo).convert('RGB')

    #Establecemos la posicion de la imagen, en este caso será el centro.
    pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    # Guardamos la imagen de nuestro código QR en un directorio
    QRimg.save(path)


imagen = 'logo-uni.png'
imagenlogo = 'img/logo/'+imagen
url = 'https://forms.gle/bkvT3dCUC34xSN4E9'
path = 'img/qr/'+imagen

createQR(imagenlogo,url,path)