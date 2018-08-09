
import json
import os
class Config(object):

  social_domains = ('buzzfeed.com','facebook.com','vk.com','pinterest.com','twitter.com','instagram.com','tumblr.com')

  def __init__(self):

    with open(os.path.dirname(os.path.realpath(__file__))+'/configs.json') as file:
        self.config_file = json.load(file)

  # def getStartingUrls(self):
  #     pass
  #
  # def setIgnoreSocial(self,state):
  #   self.config_file['ignore_social'] = state


  def getIgnoreSocial(self):
    return self.config_file['ignore_social']

  def getConfigFile(self):

    return self.config_file
 
