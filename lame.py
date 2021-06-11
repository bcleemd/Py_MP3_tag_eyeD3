import os
import eyed3

for f in os.listdir('.'):
    # print (f, type(f))
    
    if f.split('.')[-1] == 'mp3':


        af = eyeD3.mp3.Mp3AudioFile(f) 

        print (type(af))
        # lamever = af.lameTag[‘encoder_version’] 
        # name, ver = lamever[:4], lamever[4:] 
        # gain = af.lameTag[‘replaygain’][‘radio’][‘adjustment’] 
        # print (lamever, name, ver, gain)

        
        # if name == ‘LAME’ and eyeD3.mp3.lamevercmp(ver, ‘3.95’) > 0:

        #     gain -= 6

        #     endcode
    

