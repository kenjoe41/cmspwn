import sys, traceback

def get_err_file_and_line(tb=None):
    """Return the file and line number of the statement that raised the tb.

    Returns: (filename, lineno) tuple

    """
    if not tb:
        tb = sys.exc_info()[2]

    filename, lineno, _context, _line = traceback.extract_tb(tb)[-1]

    return filename, lineno

