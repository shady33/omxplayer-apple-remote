from subprocess import Popen, PIPE
import lirc
import sys

sockid=lirc.init("myprogram")
process = Popen(['sudo','omxplayer',sys.argv[1]], stdin=PIPE, stdout=PIPE)
while True:
        try:
                z=lirc.nextcode()[0]
                process.stdin.write(z)
                if z== 'q':
                        break
        except:
                print "error"

print 'Exiting omxplayer'