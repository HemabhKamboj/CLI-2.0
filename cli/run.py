#!/usr/bin/env python3

from packages import (
    run_quotewebscrapping, 
    run_openweatherapi,
    run_newsapi,
    run_youtubedownload,
    run_wallpaperwebscrapping,
    run_movieapi,
    run_crypto,
    run_hackathols,
    run_wiki,
    run_stocks,
    facebook,
)

import cmd
import sys

class customcli(cmd.Cmd):

    try:
        intro = "Welcome {username}!".format(username=sys.argv[1])
    except IndexError:
        print("Please provide your username!")
        exit()
    prompt = 'cli: '

    def do_history(self, arg):
        "history"
        print(self._history)

    def do_weather(self, arg):
        "weather"
        run_openweatherapi()

    def do_news(self, arg):
        "news"
        run_newsapi()

    def do_movie(self, arg):
        "movie ratings"
        run_movieapi()        


    def do_quote(self, arg):
        ""
        run_quotewebscrapping()

    def do_wallpaper(self, arg):
        "wallpaper"
        run_wallpaperwebscrapping()

    def do_exit(self, arg):
        "exit"
        return -1

    def do_download(self, arg):
        "download youtube videos"
        run_youtubedownload()    

    def do_stocks(self, arg):
        "stock prices"    
        run_stocks

    def do_crypto(self, arg):
        "crypto prices"
        run_crypto

    def do_hackathons(self, arg):
        "upcoming hackathons"
        run_hackathon

    def do_wiki(self, arg):
        "wikipedia"
        run_wiki

    def do_facebook(self, arg):
        "facebook"
        facebook
                 
    def precmd(self, line):
        """ It is called after the input but before
            it has been interpreted. If you want to modify the input line
            before execution, it can be done here.
        """
        if line != '':
            self._history += [ line.strip() ]
        return line

    def postcmd(self, stop, line):
        """in case of stopping the console and returning something, it can be done here """
        return stop

    def preloop(self):
        "Initialization before prompting user for commands"
        cmd.Cmd.preloop(self)
        self._history = []

    def postloop(self):
        "exit the cli"
        print("I'm done")
        cmd.Cmd.postloop(self)

if __name__=='__main__':
    customcli().cmdloop()