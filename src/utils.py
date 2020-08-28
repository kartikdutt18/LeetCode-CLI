import os

def MakeDir(path) :
  """
    Creates a directory if doesn't exist.
    args :
    path : path to the Directory.
    returns None.
  """
  if not os.path.exists(path):
    os.mkdir(path)