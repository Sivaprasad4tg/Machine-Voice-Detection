def normal():
    print("*****Normal*****")
    Path=["D:/programs/project/focus/voice/database/human/MANIKYACHIRAKULLA FIRST PART.wav",
    "D:/programs/project/focus/voice/database/human/merin_hindi.wav",
    "D:/programs/project/focus/voice/database/human/norm_1.wav",
    "D:/programs/project/focus/voice/database/human/norm_2.wav",
    "D:/programs/project/focus/voice/database/human/norm_3.wav",
    "D:/programs/project/focus/voice/database/human/norm_4.wav",
    "D:/programs/project/focus/voice/database/human/norm_5.wav",
    "D:/programs/project/focus/voice/database/human/norm_6.wav",
    "D:/programs/project/focus/voice/database/human/Record-102.wav",
    "D:/programs/project/focus/voice/database/human/WhatsApp Audio 2023-02-25 at 12.55.03.waptt (1).wav",
    "D:/programs/project/focus/voice/database/human/WhatsApp Audio 2023-02-25 at 22.39.43.waptt.wav",
    "D:/programs/project/focus/voice/database/human/WhatsApp Audio 2023-05-07 at 11.01.13.waptt.wav",
    "D:/programs/project/focus/voice/database/human/WhatsApp Audio 2023-05-07 at 11.51.33.waptt.wav",
    "D:/programs/project/focus/voice/database/human/WhatsApp Audio 2023-05-08 at 09.11.48.dat.wav",
    "D:/programs/project/focus/voice/database/human/WhatsApp Audio 2023-05-12 at 14.06.48 (1).wav",
    "D:/programs/project/focus/voice/database/human/WhatsApp Audio 2023-05-12 at 14.51.35.waptt.wav",
    "D:/programs/project/focus/voice/database/human/WhatsApp Audio 2023-05-12 at 14.52.04.waptt.wav",
    "D:/programs/project/focus/voice/database/human/WhatsApp Audio 2023-05-12 at 14.53.00.waptt.wav",
    "D:/programs/project/focus/voice/database/human/WhatsApp Audio 2023-05-12 at 14.54.04.waptt.wav",
    "D:/programs/project/focus/voice/database/human/WhatsApp Audio 2023-05-12 at 14.54.37.waptt.wav"]


    return(Path)

def machine():
    print("*****Machine*****")
    Path=["D:/programs/project/focus/voice/database/machine/common_voice_en_34925861.wav",
    "D:/programs/project/focus/voice/database/machine/common_voice_en_34926026.wav",
    "D:/programs/project/focus/voice/database/machine/common_voice_en_34926094.wav",
    "D:/programs/project/focus/voice/database/machine/common_voice_en_35934580.wav",
    "D:/programs/project/focus/voice/database/machine/common_voice_en_36529771.wav",
    "D:/programs/project/focus/voice/database/machine/common_voice_en_36529772.wav",
    "D:/programs/project/focus/voice/database/machine/common_voice_en_36529773.wav",
    "D:/programs/project/focus/voice/database/machine/de-DE-Standard-B.wav",
    "D:/programs/project/focus/voice/database/machine/de-DE-Standard-D.wav",
    "D:/programs/project/focus/voice/database/machine/en-AU-Neural2-A.wav",
    "D:/programs/project/focus/voice/database/machine/en-AU-Neural2-B.wav",
    "D:/programs/project/focus/voice/database/machine/en-AU-Neural2-C.wav",
    "D:/programs/project/focus/voice/database/machine/en-AU-News-E.wav",
    "D:/programs/project/focus/voice/database/machine/en-GB-Neural2-C.wav",
    "D:/programs/project/focus/voice/database/machine/en-GB-Neural2-D.wav",
    "D:/programs/project/focus/voice/database/machine/en-GB-News-K.wav",
    "D:/programs/project/focus/voice/database/machine/en-IN-Standard-A.wav",
    "D:/programs/project/focus/voice/database/machine/en-IN-Standard-B.wav",
    "D:/programs/project/focus/voice/database/machine/en-IN-Standard-D.wav",
    "D:/programs/project/focus/voice/database/machine/en-US-News-L.wav",
    "D:/programs/project/focus/voice/database/machine/en-US-News-M.wav",
    "D:/programs/project/focus/voice/database/machine/hi-IN-Wavenet-B.wav",
    "D:/programs/project/focus/voice/database/machine/ml-IN-Standard-B.wav",
    "D:/programs/project/focus/voice/database/machine/ml-IN-Wavenet-A.wav",
    "D:/programs/project/focus/voice/database/machine/af-ZA-Standard-A.wav",
    "D:/programs/project/focus/voice/database/machine/ar-XA-Standard-A.wav",
    "D:/programs/project/focus/voice/database/machine/common_voice_en_34925857.wav",
    "D:/programs/project/focus/voice/database/machine/common_voice_en_34925858.wav"]
    return(Path)



def classify(path):
    l=[]
    for x in path:
        l.append(fr.form(x))
        l.append(fr.spec_centroid(x))
        l.append(fr.mfc(x))
        l.append(fr.prosody(x))
        l.append(fr.amplitude_env(x))
        l.append(fr.spec_flux(x))

        c=np.mean(l)
        if c > 0.5:
            print("machine voice"+str(l))
        else:print("normal voice"+str(l))
        l=[]

import numpy as np
import features as fr 

path=normal()
classify(path)
path=machine()
classify(path)
