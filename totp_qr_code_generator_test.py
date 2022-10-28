import totp_qr_code_generator as tqcg

tuples = [('A', 'IE'), ('AB', 'IFBA'), ('ABC', 'IFBEG'), ('ABCD', 'IFBEGRA'), ('ABCDE', 'IFBEGRCF')]

def test_encode_secret_string():
    for (plain, encoded) in tuples:
        assert tqcg.encode_secret_string(plain) == encoded

def test_create_totp_url():
    assert tqcg.create_totp_url('Example', 'alice@google.com', 'JBSWY3DPEHPK3PXP') == 'otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example'
