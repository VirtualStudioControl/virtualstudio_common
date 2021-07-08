from typing import List

from ..io.filewriter import readFileBinary
import base64


def readPNGIcon(path: str):
    """
    Reads the File from the given path and prepares it for sending to the configurator application
    :param path: Path to a PNG file containing the icon
    :return: the base64 encoded string ready for sending
    """
    data = readFileBinary(path)
    return encodeIconData(data)


def encodeIconData(data: bytes):
    """
    Encodes Icon data
    :param data: Data to encode
    :return: Encoded String
    """
    return base64.b64encode(data).decode("utf-8")


def decodeIconData(data: str):
    """
    Decodes Icon data
    :param data: Data String to decode
    :return: Decoded Bytes
    """
    if data is None:
        return None

    return base64.b64decode(data.encode("utf-8"))


def computeCategoryID(category: List[str]):
    """
    Computes the category ID used for storing the category Icon
    :param category: category list
    :return: Category Identifier computed ([0].[1].[2].[...].[n])
    """
    return category[0] + "".join("." + c for c in category[1:])