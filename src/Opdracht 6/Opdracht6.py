import argparse
from Crypto.Cipher import AES
from Crypto import Random
import os
import random
import struct
import hashlib

parser = argparse.ArgumentParser(description='Dit is Opdracht 6, IFSCP 1516')

class opdracht6():
    args = parser.parse_args()

    # Block sized need to be defined, for the working of AES.
    # https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
    # For AES, NIST selected three members of the Rijndael family,
    # each with a block size of 128 bits, but three different key lengths: 128, 192 and 256 bits.

    # AES implementation is pretty standard nowadays in python. To many examples that would not
    # be mostly derived from the source material
    # using: https://gist.github.com/dreikanter/2780734

    def __init__(self):
        args = parser.parse_args()
        source_file_name = "1-source.txt"
        encoded_file_name = "2-encoded.txt"
        decoded_file_name = "3-decoded.txt"

        self.create_source_file(source_file_name)

        # Length could be 16, 14 or 32
        key = Random.get_random_bytes(16)
        self.encrypt_file(key, source_file_name, encoded_file_name)
        self.decrypt_file(key, encoded_file_name, decoded_file_name)

        source_md5 = self.md5_for_file(source_file_name)
        decoded_md5 = self.md5_for_file(decoded_file_name)

        print("Source: %s [%s]" % (source_file_name, source_md5))
        print("Encoded: %s" % (source_file_name))
        print("Decoded: %s [%s]" % (decoded_file_name, decoded_md5))
        print("Hash check %s" % "passed" if source_md5 == decoded_md5 else "not passed")

    def create_source_file(self, file_name):
        f = open(file_name, "wt")
        f.write("Hello!\nThis is an example text file.")
        f.close()


    def write_file(self, file_name, data):
        f = open(file_name, "w")
        f.write(data)
        f.close()


    def encrypt_file(self, key, in_filename, out_filename=None, chunksize=64 * 1024):
        """ Encrypts a file using AES (CBC mode) with the
            given key.

            key:
                The encryption key - a string that must be
                either 16, 24 or 32 bytes long. Longer keys
                are more secure.

            in_filename:
                Name of the input file

            out_filename:
                If None, '<in_filename>.enc' will be used.

            chunksize:
                Sets the size of the chunk which the function
                uses to read and encrypt the file. Larger chunk
                sizes can be faster for some files and machines.
                chunksize must be divisible by 16.
        """
        if not out_filename:
            out_filename = in_filename + '.enc'

        iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(in_filename)

        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)

                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += ' ' * (16 - len(chunk) % 16)

                    outfile.write(encryptor.encrypt(chunk))


    def decrypt_file(self, key, in_filename, out_filename=None, chunksize=24 * 1024):
        """ Decrypts a file using AES (CBC mode) with the
            given key. Parameters are similar to encrypt_file,
            with one difference: out_filename, if not supplied
            will be in_filename without its last extension
            (i.e. if in_filename is 'aaa.zip.enc' then
            out_filename will be 'aaa.zip')
        """
        if not out_filename:
            out_filename = os.path.splitext(in_filename)[0]

        with open(in_filename, 'rb') as infile:
            origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, iv)

            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))

                outfile.truncate(origsize)


    def md5_for_file(self, file_name, block_size=2 ** 20):
        md5 = hashlib.md5()
        f = open(file_name, "r")

        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)

        f.close()
        return md5.hexdigest()


if __name__ == "__main__":
    opdracht6()