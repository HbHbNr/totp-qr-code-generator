import base64
import io
import qrcode as qrc

def create_totp_url(issuer, accountname, secret):
    # Example from https://github.com/google/google-authenticator/wiki/Key-Uri-Format
    # otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example

    # check issuer and accountname for ':' and other forbidden characters
    encodedsecret = base64.b32encode(secret.encode('ascii')).decode('ascii').rstrip('=')

    url = f"otpauth://totp/{issuer}:{accountname}?secret={encodedsecret}&issuer={issuer}"
    return url

def print_qrcode(url):
    qrcode = qrc.QRCode()
    qrcode.add_data(url)
    buffer = io.StringIO()
    qrcode.print_ascii(out=buffer)
    buffer.seek(0)
    print(buffer.read())

if __name__ == '__main__':
    url = create_totp_url('GMail', 'a@b.com', 'secretsecretsecretsecret')
    print(url)
    print_qrcode(url)
