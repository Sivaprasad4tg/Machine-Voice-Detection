def normal():
    print("*****Normal*****")
    Path=['/workspaces/Machine-Voice-Detection/database/human/norm_2.wav',
    '/workspaces/Machine-Voice-Detection/database/human/norm_3.wav',
    '/workspaces/Machine-Voice-Detection/database/human/norm_4.wav',
    '/workspaces/Machine-Voice-Detection/database/human/norm_5.wav',
    '/workspaces/Machine-Voice-Detection/database/human/norm_6.wav',
    '/workspaces/Machine-Voice-Detection/database/human/Record-102.wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-02-25 at 12.55.03.waptt (1).wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-02-25 at 22.39.43.waptt.wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-05-07 at 11.01.13.waptt.wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-05-07 at 11.51.33.waptt.wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-05-08 at 09.11.48.dat.wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-05-12 at 14.06.48 (1).wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-05-12 at 14.51.35.waptt.wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-05-12 at 14.52.04.waptt.wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-05-12 at 14.53.00.waptt.wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-05-12 at 14.54.04.waptt.wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-05-12 at 14.54.37.waptt.wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-05-12 at 14.55.42.waptt.wav',
    '/workspaces/Machine-Voice-Detection/database/human/WhatsApp Audio 2023-05-12 at 16.54.05.wav']


    return(Path)

def machine():
    print("*****Machine*****")
    Path=["/workspaces/Machine-Voice-Detection/database/machine/common_voice_en_34925861.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/common_voice_en_34926026.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/common_voice_en_34926094.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/common_voice_en_35934580.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/common_voice_en_36529771.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/common_voice_en_36529772.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/common_voice_en_36529773.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/de-DE-Standard-B.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/de-DE-Standard-D.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-AU-Neural2-A.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-AU-Neural2-B.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-AU-Neural2-C.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-AU-News-E.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-GB-Neural2-C.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-GB-Neural2-D.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-GB-News-K.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-IN-Standard-A.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-IN-Standard-B.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-IN-Standard-D.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-US-News-L.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/en-US-News-M.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/hi-IN-Wavenet-B.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/ml-IN-Standard-B.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/ml-IN-Wavenet-A.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/af-ZA-Standard-A.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/ar-XA-Standard-A.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/common_voice_en_34925857.wav",
    "/workspaces/Machine-Voice-Detection/database/machine/common_voice_en_34925858.wav"]
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
