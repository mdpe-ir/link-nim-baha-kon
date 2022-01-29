#!/usr/bin/python
# Import Modules
import datetime
import pathlib

import requests
import json
from termcolor import colored
import os


class NimbahaLinkGenerator:
    url_input = None

    def __init__(self):
        self.clear_console()
        self.print_base_info()
        self.goto_next_line()
        self.get_url()
        self.valid_type = None  # txt url invalid
        self.urls = []
        self.create_result_file = False

    @staticmethod
    def clear_console():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    @staticmethod
    def goto_next_line():
        print("\n")

    @staticmethod
    def print_base_info():
        print(colored('Salam dooste man!', 'magenta'), colored('Ba man mitooni, link haye downloadet ro', 'green'),
              colored("Nim baha", "blue"), colored("koni.", "green"))
        print(colored("AUTHOR:", "red"), colored("github.com/mdpe-ir", "cyan"))
        print(colored("HELP:", "green"), colored(""
                                                 "shoma mitavanid url (example : https://example.com/test.png) "
                                                 "ya address yek file .txt ke dar har khat yek url neveshte shode bashad ra vered kond",
                                                 "cyan"))

    def display_processing_text(self, is_list=False):
        if not is_list:
            self.clear_console()
        print(colored("Processing Link ....", "green"))

    def display_generating_link_text(self, index=0, is_list=False):

        if is_list:
            # print(colored("This operation may take up to 10 seconds!", "cyan"))
            print(colored(f"Generating link {index + 1} of {len(self.urls)}", "green"))
            self.goto_next_line()
        else:
            self.clear_console()
            print(colored("This operation may take up to 10 seconds!", "cyan"))
            self.goto_next_line()
            print(colored("Generating links ....", "green"))

    def get_url(self):
        self.url_input = input("Enter .txt file path or url >  ")

    def preparation_of_prerequisites(self, input, is_list=False):
        # DetectSearchPrase
        self.display_processing_text(is_list=is_list)
        detect_search_prase_url = 'https://www.digitalbam.ir/Home/DetectSearchPrase'
        form = {'Phrase': input}
        result = requests.post(detect_search_prase_url, data=form)
        if result.text == "downloadLink":
            return True
        else:
            return False

    def generating_link(self, link, index=0, is_list=False, is_need_to_create_file=False, f=None):
        generate_download_url = 'https://www.digitalbam.ir/DirectLinkDownloader/Download'

        form = {'downloadUri': link}

        result = requests.post(generate_download_url, data=form)

        json_result = json.loads(result.text)

        file_url = json_result['fileUrl']
        message = json_result['message']

        if is_list:
            if is_need_to_create_file:
                f.write(file_url + "\n")
            else:

                print(colored(f"Link {index + 1} >", "cyan"), file_url)
                self.goto_next_line()

        else:
            self.clear_console()
            print(colored("Your link is ready!", "green"))
            self.goto_next_line()
            print(colored("Link >", "cyan"), file_url)
            self.goto_next_line()
        # print(colored("Message >", "cyan"), message)

    def ask_for_create_file(self):
        input_response = input("Aya mikhahid tamam link haye toolid shode dar yek file .txt zakhire shavand? (y/n) > ")
        if input_response == "y" or input_response == "Y":
            self.create_result_file = True

        if self.create_result_file:
            self.goto_next_line()
            print(colored("File toolid shode dar desktop shoma zakhire khahad shod.", "cyan"))
            self.goto_next_line()

    def valid_input(self):
        input = self.url_input
        if os.path.exists(input):
            self.valid_type = "txt"

        else:
            if input.startswith("http"):
                self.valid_type = "url"
            else:
                self.valid_type = "invalid"

    def start(self):
        self.valid_input()
        if self.valid_type == "txt":
            self.ask_for_create_file()
            self.urls = open(self.url_input, "r").readlines()
            self.start_generating_link()
        elif self.valid_type == "url":
            self.urls.append(self.url_input)
            self.start_generating_link()
        else:
            self.clear_console()
            print(colored("Link Vared shode moatabar nist!", "red"))

    def start_generating_link(self):
        desktop = pathlib.Path.home() / 'Desktop' / f'link-nim-baha-kon-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.txt'
        f = None
        if self.create_result_file:
            f = open(f"{desktop}", "a")
            # f.close()

        if self.valid_type == "txt":

            for index, link in enumerate(self.urls):
                if self.preparation_of_prerequisites(link, is_list=True):
                    self.display_generating_link_text(index, is_list=True)
                    self.generating_link(link, index, is_list=True, is_need_to_create_file=self.create_result_file, f=f)

                else:
                    self.clear_console()
                    print(colored("Link Vared shode moatabar nist!", "red"))

            if self.create_result_file:
                f.close()
                self.goto_next_line()
                print(colored("File created on your desktop!", "green"))
                self.goto_next_line()
                print(colored(f"File path: {desktop}", "cyan"))
                self.goto_next_line()

        elif self.valid_type == "url":
            if self.preparation_of_prerequisites(self.url_input):
                self.display_generating_link_text()
                self.generating_link(self.url_input)
            else:
                self.clear_console()
                print(colored("Link Vared shode moatabar nist!", "red"))


# https://i.stack.imgur.com/6otvY.png


if __name__ == "__main__":
    link_generator = NimbahaLinkGenerator()
    link_generator.start()
