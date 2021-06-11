import os
import eyed3
import re
#for filename in os.listdir('.'):
    # print (filename)

     # 파일수정

re_header = re.compile("^[0-9][0-9][0-9]_")     
path = './'
#path = "M:\\__Arrange_WCS_Music"

for f in os.listdir(path):
    # print (f'"{f}", {type(f)}')

    if f.split('.')[-1] == 'mp3':
        # print (f, type(f))
        print (f'"{f}", {type(f)}')
        # title = ''
        # track_num = 0
        # try:
        #     track_num = int(f.split()[0])
        # except:
        #     pass
        # print('Track num: ' + str(track_num))
        # if track_num:
        #     title = f[5:]
        #     save_title = title.split('.')[0]
        #     os.rename(f, title)

        # mp3af = eyed3.load(path+"\\"+f)
        mp3af = eyed3.load(f)
        # print (f"Tag: {mp3af.tag}")   # <eyed3.id3.tag.Tag object at 0x10d26a710>

        # print (mp3af.tag.lame)
        try: 
            bpm = mp3af.tag.bpm
            # date = mp3af.tag.date
        except Exception as E: 
            print (f"tag ERROR at file : {f}") 
            print(E)
        # if  bpm == None :
        # print(f'" {f}  "', end='' )
        # print (f"        bpm: {mp3af.tag.bpm}  date: {date}")
        print (f"   bpm: {mp3af.tag.bpm} , {type(mp3af.tag.bpm)} ")
        if not bpm == None :
            s_bpm = f"{bpm :03d}_"
            if re_header.match(f) : 
                if f[:4] == s_bpm :
                    continue
                else : 
                    os.rename (f, s_bpm+f[4:])
                    print(f"   >>> Renamed to : {s_bpm+f[4:]}")
            else :
                os.rename(f, s_bpm+f)
                print(f"   >>> Renamed to : {s_bpm+f}")
  
         
# os.chdir('../')


