from cfg import INCLUDE_LIBS_KEY, MAIN_KEY, SNIPPET_PATH
import json
import os

class CreateSnippet():
  def __init__(self) :
    super().__init__()
    self.extentionLanguage = {'cpp': 'cpp', 'py': 'python', 'java': 'java'}

  def WriteCode(self, text : str, filename : str) :
    """
      Creates a file with given texted commented. Additionaly it will incorporate
      pre-defined snippets.
      args:
      text : Text which will be commented.
      filename : File in which text will be copied.
      Returns None.
    """
    extention = filename.split('.')[1]
    snippetPath = os.path.join(
        SNIPPET_PATH, self.extentionLanguage[extention] + "_snippet.json")
    if os.path.exists(snippetPath) :
      with open(snippetPath, 'r') as snippetMap:
        snippet = json.load(snippetMap)
      try :
        text = self.Commentify(text, self.extentionLanguage[extention])
        code = snippet[INCLUDE_LIBS_KEY] + text + snippet[MAIN_KEY]
        file = open(os.path.join(os.getcwd(), filename), 'w')
        file.write(code)
      except KeyError:
        print("Error Refer to sample snippets to see how snippets are made.")
      return None

    text = self.Commentify(text = text, language = self.extentionLanguage[extention])
    file = open(os.path.join(os.getcwd(), filename), 'w')
    file.write(text)
    return None

  def Commentify(self, text : str, language : str) :
    """
      Commentify the given text based on language.
      args:
      text : Text which will be commented.
      language : One of cpp, java or python.
      Returns commented text.
    """
    if language == "cpp" or language == "java":
      text = "\n\n/**\n * " + text.replace('\n', '\n * ') + "\n**/\n\n"
      return text
    elif language == "python":
      text = "\n\n\"\"\" \n" + text + "\n\"\"\"\n\n"
      return text

    return text
