"""
Program: client.py
Author: Ryan Elliott
Last date modified: 07/26/2020
Client Class with Driver
"""


class Client:
    """Client Class """

    def __init__(self, clientid, lname, fname, pnum, address):
        """Client constructor"""

        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_characters = set("0123456789-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not (phone_characters.issuperset(pnum)):
            raise ValueError
        if not isinstance(clientid, int):
            raise AttributeError

        self._client_id = clientid
        self._last_name = lname
        self._first_name = fname
        self._phone_number = pnum
        self._address = address

    def display(self):
        """Display client information """
        return str(self._client_id) + "\n" + str(self._first_name) + "\n" + str(self._last_name) + "\n" + str(
            self._phone_number) + "\n" + str(self._address)

    def __str__(self):
        """str override"""
        return "client id " + str(self._client_id) + " last name " + str(self._last_name) + " first name " + \
               str(self._first_name) + " phone number " + str(self._phone_number) + " address " + str(self._address)

    def __repr__(self):
        """repr override"""
        return "client id " + str(self._client_id) + " last name " + str(self._last_name) + " first name " + \
            str(self._first_name) + " phone number " + str(self._phone_number) + " address " + str(self._address)
