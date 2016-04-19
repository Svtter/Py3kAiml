#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
sys.path.insert(0, "../")

import aiml

# The Kernel object is the public interface to
# the AIML interpreter.
kern = aiml.Kernel()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
# k.learn("cn-startup.xml")


brainLoaded = False
forceReload = False
while not brainLoaded:
    if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
        # Use the Kernel's bootstrap() method to initialize the Kernel. The
        # optional learnFiles argument is a file (or list of files) to load.
        # The optional commands argument is a command (or list of commands)
        # to run after the files are loaded.
        kern.bootstrap(learnFiles="cn-startup.xml", commands="load aiml cnask")
        brainLoaded = True
        # Now that we've loaded the brain, save it to speed things up for
        # next time.
        kern.saveBrain("standard.brn")
    else:
        # Attempt to load the brain file.  If it fails, fall back on the Reload
        # method.
        try:
            # The optional branFile argument specifies a brain file to load.
            kern.bootstrap(brainFile = "standard.brn")
            brainLoaded = True
        except:
            forceReload = True

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
# k.respond("load aiml cnask")

# Loop forever, reading user input from the command
# line and printing responses.
while True: print(kern.respond(input("> ")))
