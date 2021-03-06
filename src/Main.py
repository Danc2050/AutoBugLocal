import argparse
import selectors2
import sys
import subprocess
import src.SendToServer as server
from src.FilterLists import filterBugReport
from time import sleep
import logging


class Main(object):

    def __init__(self):
        self.server = server.SendToServer()
        self.filterBugReport = filterBugReport()

    def parsingCommandLineArguments(self):
        """
        Return dictionary

        capture command line arguments.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('-S', '--userScript', help='User script Required!', required=True)
        arguments = parser.parse_args()
        return vars(arguments)

    def run(self):
        """
        Listen to invoked script for any bugs to report
        """
        scriptName = self.parsingCommandLineArguments()['userScript']
        p = subprocess.Popen([scriptName],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=True)

        sel = selectors2.DefaultSelector()
        sel.register(p.stderr, selectors2.EVENT_READ)

        while True:
            for key, _ in sel.select():
                sleep(1.5)
                traceback = key.fileobj.read1().decode()
                if not traceback:
                    exit()
                # Visual / Demo purposes
                print(traceback, end="", file=sys.stderr)

                if str(traceback).find("ModuleNotFoundError:") != -1:
                    raise Exception(f'{scriptName}, module is not found!')
                elif str(traceback).find("No such file or directory") != -1:
                    raise Exception(f'{scriptName} script is not found!')
                # if bug encountered DOES NOT appear in black list data, you CAN send bug to server
                if not self.filterBugReport.blacklist_check(str(traceback)):
                    # send bug to server
                    respondCode = self.server.sendToServer(traceback)
                    if respondCode.status_code != 200:
                        logging.error("Unable to report bug to server, response code: " + str(respondCode.status_code))


if __name__ == '__main__':
    execute = Main()
    execute.run()
