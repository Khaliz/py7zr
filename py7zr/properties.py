#
# p7zr library
#
# Copyright (c) 2019 Hiroshi Miura <miurahr@linux.com>
# Copyright (c) 2004-2015 by Joachim Bauch, mail@joachim-bauch.de
# 7-Zip Copyright (C) 1999-2010 Igor Pavlov
# LZMA SDK Copyright (C) 1999-2010 Igor Pavlov
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

from binascii import unhexlify
from enum import Enum, IntEnum
import lzma
from py7zr import altmethods


class ByteEnum(bytes, Enum):
    pass


class Property(ByteEnum):
    END = unhexlify('00')
    HEADER = unhexlify('01')
    ARCHIVE_PROPERTIES = unhexlify('02')
    ADDITIONAL_STREAMS_INFO = unhexlify('03')
    MAIN_STREAMS_INFO = unhexlify('04')
    FILES_INFO = unhexlify('05')
    PACK_INFO = unhexlify('06')
    UNPACK_INFO = unhexlify('07')
    SUBSTREAMS_INFO = unhexlify('08')
    SIZE = unhexlify('09')
    CRC = unhexlify('0a')
    FOLDER = unhexlify('0b')
    CODERS_UNPACK_SIZE = unhexlify('0c')
    NUM_UNPACK_STREAM = unhexlify('0d')
    EMPTY_STREAM = unhexlify('0e')
    EMPTY_FILE = unhexlify('0f')
    ANTI = unhexlify('10')
    NAME = unhexlify('11')
    CREATION_TIME = unhexlify('12')
    LAST_ACCESS_TIME = unhexlify('13')
    LAST_WRITE_TIME = unhexlify('14')
    ATTRIBUTES = unhexlify('15')
    COMMENT = unhexlify('16')
    ENCODED_HEADER = unhexlify('17')
    START_POS = unhexlify('18')
    DUMMY = unhexlify('19')


class CompressionMethod(ByteEnum):
    COPY = unhexlify('00')
    DELTA = unhexlify('03')
    LZMA = unhexlify('030101')
    CRYPTO = unhexlify('06')
    MISC = unhexlify('04')
    MISC_ZIP = unhexlify('0401')
    MISC_BZIP2 = unhexlify('040202')
    MISC_DEFLATE = unhexlify('040108')
    MISC_DEFLATE64 = unhexlify('040109')
    MISC_PPMD = unhexlify('030401')
    P7Z_AES256_SHA256 = unhexlify('06f10701')
    LZMA2 = unhexlify('21')
    BCJ = unhexlify('03030103')
    BCJ_PPC = unhexlify('03030205')
    BCJ_IA64 = unhexlify('03030401')
    BCJ_ARM = unhexlify('03030501')
    BCJ_ARMT = unhexlify('03030701')
    BCJ_SPARC = unhexlify('03030805')


class FileAttribute(IntEnum):
    DIRECTORY = 0x10
    READONLY = 0x01
    HIDDEN = 0x02
    SYSTEM = 0x04
    ARCHIVE = 0x20
    DEVICE = 0x40
    NORMAL = 0x80
    TEMPORARY = 0x100
    SPARSE_FILE = 0x200
    REPARSE_POINT = 0x400
    COMPRESSED = 0x800
    OFFLINE = 0x1000
    ENCRYPTED = 0x4000
    UNIX_EXTENSION = 0x8000

lzma_methods_map = {
    CompressionMethod.LZMA:lzma.FILTER_LZMA1,
    CompressionMethod.LZMA2:lzma.FILTER_LZMA2,
    CompressionMethod.DELTA:lzma.FILTER_DELTA,
    CompressionMethod.BCJ:lzma.FILTER_X86,
    CompressionMethod.BCJ_ARM:lzma.FILTER_ARM,
    CompressionMethod.BCJ_ARMT:lzma.FILTER_ARMTHUMB,
    CompressionMethod.BCJ_IA64:lzma.FILTER_IA64,
    CompressionMethod.BCJ_PPC:lzma.FILTER_POWERPC,
    CompressionMethod.BCJ_SPARC:lzma.FILTER_SPARC,
}

alt_methods_map = {
    CompressionMethod.COPY:altmethods.FILTER_COPY,
    CompressionMethod.MISC_BZIP2:altmethods.FILTER_BZIP2,
    CompressionMethod.MISC_ZIP:altmethods.FILTER_ZIP,
}
MAGIC_7Z = unhexlify('377abcaf271c')
READ_BLOCKSIZE = 16384