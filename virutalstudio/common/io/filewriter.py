import os
import errno

def writeFile (path, content, mode="w"):
    """
    Writes content to a file at the given path

    :param path: Path of the file to write
    :param content: Content to write to the file
    :param mode: File Open mode, 'w' for write, 'a' for append
    :return: None
    """
    f = open(path, mode)
    try:
        dirname = os.path.dirname(path)
        if len(dirname.strip()) > 0 and not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        f.write(content)
    finally:
        f.close()

def readFileLinesStripped(path):
    """
    Read the file Line by Line and strip each line of leading and trailing whitespaces

    :param path: Path to read from
    :return: a list of stripped Lines
    """
    f = open(path, "r")
    lines = []
    try:
        for line in f:
            lines.append(line.strip())
    finally:
        f.close()

    return lines

def readFile(path):
    """
    Read the file Line by Line and strip each line of leading and trailing whitespaces

    :param path: Path to read from
    :return: a list of stripped Lines
    """
    f = open(path, "r")
    result = ""
    try:
        result = f.read()
    finally:
        f.close()

    return result
