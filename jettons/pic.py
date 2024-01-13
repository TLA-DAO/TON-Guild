import base64

with open('trust_icon.webp', 'rb') as f:
    img = open('icon_trust.raw', 'wb')
    img.write(base64.b64encode(f.read()))
    img.close()

