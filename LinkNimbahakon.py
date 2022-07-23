#!/usr/bin/python

# Import Modules
import datetime
import pathlib

import requests
import json
from termcolor import colored
import os
import wget


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
        self.downloads_folder = ""

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
        print(colored("Project:", "red"), colored(
            "github.com/mdpe-ir/link-nim-baha-kon", "cyan"))
        print(colored("AUTHOR:", "red"), colored("github.com/mdpe-ir", "cyan"))

    def display_processing_text(self, is_list=False):
        if not is_list:
            self.clear_console()
        print(colored("Processing Link ....", "green"))

    def display_generating_link_text(self, index=0, is_list=False):

        if is_list:
            # print(colored("This operation may take up to 10 seconds!", "cyan"))
            print(
                colored(f"Start Downloading link {index + 1} of {len(self.urls)}", "green"))
            self.goto_next_line()
        else:
            self.clear_console()
            print(colored("", "cyan"))
            self.goto_next_line()
            print(colored("Start Downloading ....", "green"))

    def get_url(self):
        self.url_input = input("Enter .txt file path or url >  ")

    def preparation_of_prerequisites(self, input, is_list=False):
        # DetectSearchPrase

        self.display_processing_text(is_list=is_list)

        generate_download_url = 'https://linknim.ir/dl/'

        form = {'url': input, 'step': 'send link'}

        result = requests.post(generate_download_url, data=form)

        if result.status_code == 200:
            return True
        else:
            return False

    def generating_link(self, link, index=0, is_list=False, is_need_to_create_file=False, f=None):
        generate_download_url = 'https://linknim.ir/dl/'

        form = {'url': str(link).strip(), 'res': 'download'}

        # result = requests.post(generate_download_url, data=form)

        local_filename = os.path.join(
            self.downloads_folder,  link.split('/')[-1])
        # NOTE the stream=True parameter below
        with requests.post(generate_download_url, stream=True, data=form) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    # if chunk:
                    f.write(chunk)

        self.goto_next_line()

        if is_list:
            print(colored(f"Link {index + 1} >", "cyan"), local_filename)
        else:
            self.clear_console()
            print(colored(f"Link Downloaded. "), local_filename)

        self.goto_next_line()

        # json_result = json.loads(result.text)

        # file_url = json_result['fileUrl']
        # message = json_result['message']

        # else:
        #     self.clear_console()
        #     print(colored("Your link is ready!", "green"))
        #     self.goto_next_line()
        #     print(colored("Link >", "cyan"), file_url)
        #     self.goto_next_line()
        # print(colored("Message >", "cyan"), message)

    def ask_for_downlod_file(self):
        self.goto_next_line()
        input_response = input(
            "All the link(s) entered in the downloads folder will be downloaded. do you continue (y/n) > ")
        if input_response == "y" or input_response == "Y":
            self.create_result_file = True

        if self.create_result_file:
            self.goto_next_line()
            print(colored("", "cyan"))
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
        self.ask_for_downlod_file()
        if self.valid_type == "txt":
            self.urls = open(self.url_input, "r").readlines()
            self.start_generating_link()
        elif self.valid_type == "url":
            self.urls.append(self.url_input)
            self.start_generating_link()
        else:
            self.clear_console()
            print(colored("Link Vared shode moatabar nist!", "red"))

    def get_download_path(self):
        """Returns the default downloads path for linux or windows"""
        if os.name == 'nt':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        else:
            return os.path.join(os.path.expanduser('~'), 'Downloads')

    def start_generating_link(self):
        self.downloads_folder = os.path.join(self.get_download_path(
        ), f'link-nim-baha-kon-{datetime.datetime.now().strftime("%Y-%m-%d-%H")}')

        if not os.path.exists(self.downloads_folder):
            os.mkdir(self.downloads_folder)

        if self.valid_type == "txt":

            for index, link in enumerate(self.urls):
                if self.preparation_of_prerequisites(link, is_list=True):
                    self.display_generating_link_text(index, is_list=True)
                    self.generating_link(
                        link, index, is_list=True, is_need_to_create_file=self.create_result_file, f=self.downloads_folder)

                else:
                    self.clear_console()
                    print(colored("Link Vared shode moatabar nist!", "red"))

            if self.create_result_file:
                self.clear_console()
                self.goto_next_line()
                print(colored("All files Downloaded!", "green"))
                self.goto_next_line()
                print(colored(f"Folder path: {self.downloads_folder}", "cyan"))
                self.goto_next_line()

        elif self.valid_type == "url":
            if self.preparation_of_prerequisites(self.url_input):
                self.display_generating_link_text()
                self.generating_link(self.url_input)
            else:
                self.clear_console()
                print(colored("Link Vared shode moatabar nist!", "red"))


# Sample image : http://www.africau.edu/images/default/sample.pdf


if __name__ == "__main__":
    link_generator = NimbahaLinkGenerator()
    link_generator.start()
