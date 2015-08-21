#-------------------------------------------------------------------------------
# Name:        Immunity debugger Exception Hook
# Purpose:      The script throws out values of EIP,ESP when a crash exception occours
#
# Author:      @abhinavbom
#
# Created:     19/10/2014
# Licence:     MIT
#-------------------------------------------------------------------------------

import immlib
from immlib import AllExceptHook

class DemoHook(AllExceptHook):

    def __init__(self):
        AllExceptHook.__init__(self)

    def run(self, regs):
        imm = immlib.Debugger()
        #picks up registers from the memory
        eip = regs['EIP']
        esp = regs['ESP']
        #logging register information
        imm.log("EIP: 0x%08X ESP:0x%08X"%(eip, esp))
        #reads the data from the ESP
        buff = imm.readString(esp)


def main(args):
    imm = immlib.Debugger()
    newHook = DemoHook()
    newHook.add('Demo Hook')
    return 'Hook PyCommand'

if __name__ == '__main__':
    main()
