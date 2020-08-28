import requests
import json
from bs4 import BeautifulSoup as bs
from utils import *
from cfg import *
from create_snippet import *

class LeetCodeCLI() :
  def __init__(self, questionName : str) :
    super().__init__()
    self.questionName = self.ProcessQuestionName(questionName)
    self.questionData = self.FetchQuestion()
    self.languageFileExtention = {'c++' : 'cpp', 'python' : 'py', 'java' : 'java'}

  def CreateCodeSnippet(self, language : str) :
    soup = bs(self.questionData['data']['question']['content'], 'lxml')
    title = self.questionData['data']['question']['title']
    text = soup.get_text().replace('\n\n\n\n', ' ')

    # Add Link to question in the text.
    text = text.strip()
    text = text + "\n Link : " + SRC_WEBSITE + PROBLEM_EXTENTION + self.questionName

    # clean up.
    text = title.strip() + text.strip()

    # Create code snippet.
    file_name = "_".join(self.questionName.split('-'))
    file_name = file_name + "." + self.languageFileExtention[language.lower()]
    fileWriter = CreateSnippet()
    fileWriter.WriteCode(text = text, filename = file_name)

  def ProcessQuestionName(self, questionName) :
    """
      Format the input for html address.
      args:
      questionName : Input string (question name).
      returns lower-cased input seperated by '-' instead of spaces.
    """

    if len(questionName) == 0 :
      return questionName

    return "-".join(questionName.lower().split())

  def FetchQuestion(self) :
    """
      Queries LeetCode for the given question. If passed string is empty,
      loads the last queried question.
      Returns a dictionary as obtained from querying LeetCode DB.
    """

    # Load question details from cache.
    if len(self.questionName) == 0 :
      with open(CACHED_QUESTION, 'r') as cachedQuestion:
        response = json.load(cachedQuestion)
      return response

    data[QUESTION_KEY][QUESTION_QUERY_KEY] = self.questionName
    response = requests.post(SRC_WEBSITE + QUERY_EXTENTION, json = data).json()

    # Store the current question in cache (in memory) to allow future queries.
    MakeDir(CACHE_PATH)
    with open(CACHED_QUESTION, 'w') as cachedQuestion :
      json.dump(response, cachedQuestion)
    return response

if __name__ == "__main__":
  obj = LeetCodeCLI("Two Sum")
  obj.CreateCodeSnippet("pyThon")
  obj.CreateCodeSnippet("C++")
