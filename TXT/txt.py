from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Baca isi file teks
file_path = "D:/Sistem Keamanan Data/RSA Widi.txt"
with open(file_path, "rb") as f:
    file_content = f.read()

# Inisialisasi kunci dan enkripsi teks menggunakan Fernet
fernet_key = Fernet.generate_key()
cipher_suite = Fernet(fernet_key)
cipher_text = cipher_suite.encrypt(file_content)

# Simpan file terenkripsi menggunakan Fernet
encrypted_file_path_fernet = "D:/Sistem Keamanan Data/RSA Widi_encrypted_fernet.txt"
with open(encrypted_file_path_fernet, "wb") as f:
    f.write(cipher_text)

# Inisialisasi kunci privat dan publik RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Enkripsi kunci Fernet menggunakan kunci publik RSA
encrypted_fernet_key = public_key.encrypt(
    fernet_key,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# Simpan kunci privat dan publik RSA
private_key_path_rsa = "private_key_rsa.pem"
public_key_path_rsa = "public_key_rsa.pem"
with open(private_key_path_rsa, "wb") as f:
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    f.write(private_key_bytes)

with open(public_key_path_rsa, "wb") as f:
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    f.write(public_key_bytes)

# Simpan kunci Fernet terenkripsi menggunakan kunci privat RSA
encrypted_key_path_rsa = "encrypted_fernet_key_rsa.bin"
with open(encrypted_key_path_rsa, "wb") as f:
    f.write(encrypted_fernet_key)

print(f"File {file_path} telah dienkripsi dan disimpan sebagai {encrypted_file_path_fernet} menggunakan Fernet.")
print(f"Kunci Fernet: {fernet_key}")
print(f"Kunci privat RSA: {private_key_path_rsa}")
print(f"Kunci publik RSA: {public_key_path_rsa}")
print(f"Kunci Fernet terenkripsi menggunakan RSA: {encrypted_key_path_rsa}")
