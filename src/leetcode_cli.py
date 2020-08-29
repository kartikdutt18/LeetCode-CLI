import requests
import json
from bs4 import BeautifulSoup as bs
import re
from utils import *
from cfg import *
from create_snippet import *

class LeetCodeCLI() :
  def __init__(self, questionName : str) :
    super().__init__()
    self.questionName = self.ProcessQuestionName(questionName)
    self.questionData = self.FetchQuestion()
    self.languageFileExtention = {'c++' : 'cpp', 'python' : 'py', 'java' : 'java'}

  def CreateCodeSnippet(self,
                        language : str,
                        showHints = False,
                        showSuggestions = False) :
    """
      Creates a code snippet with predefined code snippet and adds the given question
      as comments. If no predefined snippet is found, an empty file is created with
      given question as comments.
      args :
      language : Language for which file will be created.
      showHints : Boolean, If true, shows hints if any. Defaults to False.
      showSuggestions : Boolean, If true, shows suggested questions. Defaults to False.
    """
    soup = bs(self.questionData['data']['question']['content'], 'lxml')
    title = self.questionData['data']['question'][TITLE_KEY]
    text = soup.get_text().replace('\n\n\n\n', ' ')

    text = text.strip()
    # Show Hints.
    if showHints :
      text = text + "\n Hints :\n"
      for hints in self.questionData['data']['question']['hints'] :
        text = text + hints + "\n"

    # Show suggestions.
    if showSuggestions :
      text = text + "\n Suggested Questions :\n"
      questionList = self.questionData['data']['question']['similarQuestions'].split("\"title\":")
      for question in questionList:
        if question[0] == "[" :
          continue
        text = text + question.split(',')[0].replace("\"", "") + "\n"

    # Add Link to question in the text.
    text = text + "\n Link : " + SRC_WEBSITE + PROBLEM_EXTENTION + self.questionName

    # clean up.
    text = title.strip() + "\n" + text.strip()

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

  def GetSuggestion(self) :
    text = ""
    text = text + "\n Suggested Questions :\n"
    questionList = self.questionData['data']['question']['similarQuestions'].split(
        "\"title\":")
    for question in questionList:
      if question[0] == "[":
        continue
    text = text + question.split(',')[0].replace("\"", "") + "\n"
    #print(text)

if __name__ == "__main__":
  obj = LeetCodeCLI("Two Sum")
  obj.CreateCodeSnippet("pyThon", True, True)
  obj.CreateCodeSnippet("C++", True, False)
  obj2 = LeetCodeCLI("")
  obj2.GetSuggestion()
