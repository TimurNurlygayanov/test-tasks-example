#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is very simple example of some code
# which will use files and will try call external REST API
# so - we will try to create mock for these methods

import requests


class MySuperProgram():

    def read_string_from_file(self):
        """ This function reads first string in file and
            returns this string. """

        with open('my_file.txt', 'r') as f:
            result = f.readline()

        return result

    def read_and_sort_all_strings(self):
        """ This function reads all strings from file and returns
            sorted list of strings.
        """

        with open('my_file.txt', 'r') as f:
            result = f.readlines()

        return sorted(result)

    def get_current_ip(self):
        """ This function returns the current external ip of the host. """

        res = requests.get('https://api.ipify.org/?format=json')
        data = res.json()

        return data['ip']
