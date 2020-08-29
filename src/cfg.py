import os

#Set base path.
BASE_PATH = "./"
CACHE_PATH = os.path.join(BASE_PATH, "cache")
CACHED_QUESTION = os.path.join(CACHE_PATH,  "cache.json")
SNIPPET_PATH = os.path.join(BASE_PATH, "snippets/")

# Snippet-config.
INCLUDE_LIBS_KEY = 'header'
MAIN_KEY = 'main'

################# Query Config #################

# Set source websites.
SRC_WEBSITE = "https://leetcode.com/"
QUERY_EXTENTION = "graphql/"
PROBLEM_EXTENTION = "problems/"

# PARAMETERS For setting query keys.
QUESTION_KEY = "variables"
QUESTION_QUERY_KEY = "titleSlug"

# Parameter that holds the title of the Question.
TITLE_KEY = "title"

# Set JSON Format.
data = {"operationName": "questionData",
        "variables": {"titleSlug": "two-sum"},
        "query": "query questionData($titleSlug: String!){\n \
          question(titleSlug: $titleSlug) \
          {\n questionId \n \
              questionFrontendId\n \
              boundTopicId\n \
              title\n \
              titleSlug\n \
              content\n \
              translatedTitle\n \
              translatedContent\n \
              isPaidOnly\n \
              difficulty\n \
              likes\n \
              dislikes\n \
              isLiked\n \
              similarQuestions\n \
              contributors {\n \
                username\n \
                profileUrl\n \
                avatarUrl\n \
                __typename\n \
              }\n \
              langToValidPlayground\n \
              topicTags \
                {\n name\n \
                    slug\n \
                    translatedName\n \
                    __typename\n \
                }\n \
                companyTagStats\n \
                codeSnippets {\n \
                lang\n \
                langSlug\n \
                code\n \
                __typename\n \
                }\n \
                stats\n \
                hints\n \
                solution \
                  {\n id\n \
                      canSeeDetail\n \
                      __typename\n \
                  }\n \
                  status\n \
                  sampleTestCase\n \
                  metaData\n \
                  judgerAvailable\n \
                  judgeType\n \
                  mysqlSchemas\n \
                  enableRunCode\n \
                  enableTestMode\n \
                  envInfo\n \
                  libraryUrl\n \
                  __typename\n \
          }\n}\n"}
