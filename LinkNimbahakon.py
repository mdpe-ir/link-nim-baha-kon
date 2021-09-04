#!/usr/bin/python
#Import Modules
import requests
import json
from termcolor import colored
import os


class NimbahaLinkGenerator  :
    url_input = None

    def __init__(self) :
        self.clearConsole()
        self.printBaseInfo()
        self.gotoNextLine()
        self.getUrl()


    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def gotoNextLine(self):
        print("\n")

    def printBaseInfo(self) :
        print (colored('Salam dooste man!', 'magenta'), colored('Ba man mitooni, link haye downloadet ro', 'green')  , colored("Nim baha" , "blue") ,  colored("koni." , "green") )
        print (colored("AUTHOR:" , "red") , colored("github.com/mdpe-ir" , "cyan"))

    def displayProcessingText(self):
        self.clearConsole()
        print(colored("Processing Link ...." , "green"))

    def displayGeneratingLinkText(self):
        self.clearConsole()
        print (colored("This operation may take up to 10 seconds!" , "cyan"))
        self.gotoNextLine()
        print(colored("Generating links ...." , "green"))

    def getUrl(self):
        self.url_input = input("Enter file url>  ")

    def preparationOfPrerequisites(self):
        #DetectSearchPrase
        self.displayProcessingText()
        detect_search_prase_url = 'https://www.digitalbam.ir/Home/DetectSearchPrase'
        form = {'Phrase': self.url_input}
        result = requests.post(detect_search_prase_url, data = form)
        print(type(result))
        if result.text == "downloadLink" :
            return True
        else:
            return False

    def generatingLink (self) :
        generate_download_url = 'https://www.digitalbam.ir/DirectLinkDownloader/Download'

        form = {'downloadUri': self.url_input}

        result = requests.post(generate_download_url, data = form)



        json_result = json.loads(result.text)

        fileUrl = json_result['fileUrl']
        message = json_result['message']

        self.clearConsole()
        print (colored("Your link is ready!" , "green"))
        self.gotoNextLine()
        print (colored("Link download nim baha >" , "cyan") ,fileUrl )
        self.gotoNextLine()
        print (colored("Message >" , "cyan") ,message )

    def start(self) :
        if self.preparationOfPrerequisites() :
            self.displayGeneratingLinkText()
            self.generatingLink()
        else :
            self.clearConsole()
            print(colored("Link Vared shode moatabar nist!" , "red"))

#https://i.stack.imgur.com/6otvY.png


if __name__ == "__main__" :
    link_generator = NimbahaLinkGenerator()
    link_generator.start()
