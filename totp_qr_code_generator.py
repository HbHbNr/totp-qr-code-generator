import base64
import io
import getpass
import readline
import qrcode as qrc

def create_totp_url(issuer, accountname, encoded_secret_string):
    # Example from https://github.com/google/google-authenticator/wiki/Key-Uri-Format
    # otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example

    # TODO: check issuer and accountname for ':' and other forbidden characters

    # remove whitespace from secret string
    stripped_encoded_secret_string = encoded_secret_string.replace(' ', '')

    url = f"otpauth://totp/{issuer}:{accountname}?secret={stripped_encoded_secret_string.upper()}&issuer={issuer}"
    return url

def encode_secret_string(secret_string):
    encoded_secret_string = encode_secret_bytes(secret_string.encode('utf-8'))
    return encoded_secret_string

def encode_secret_bytes(secret_bytes):
    encoded_secret_bytes = base64.b32encode(secret_bytes).decode('ascii').rstrip('=')
    return encoded_secret_bytes

def print_qrcode(url):
    qrcode = qrc.QRCode()
    qrcode.add_data(url)
    buffer = io.StringIO()
    qrcode.print_ascii(out=buffer)
    buffer.seek(0)
    print(buffer.read())

if __name__ == '__main__':
    issuer = input('Issuer: ')
    accountname = input('Account: ')
    secret = getpass.getpass('Secret: ')

    url = create_totp_url(issuer, accountname, secret)
    print(url)
    print_qrcode(url)
