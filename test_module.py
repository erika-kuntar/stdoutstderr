import sys
import os

def test_stderr_output():
    print("This is a stdrr error message", file=sys.stderr)
    assert False

def test_stdout_output():
    print("This is a stdrr error message", file=sys.stdout)
    assert False
