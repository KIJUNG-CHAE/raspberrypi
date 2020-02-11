import os
class SndProt:
    def pFileSend(self,FileName,bDta):
        sze = len(bDta)
        btsend = bytearray()
        btsend.append(0x4a)
        btsend.append(0x12)
        btsend.append(0x8b)
        btsend.append(0x13)
        flesze = len(FileName)
        sze +=(flesze+1)
        hsze = int(sze/0x1000000)
        btsend.append(hsze)                           
        hsze = sze - hsze*0x1000000
        lsze = int(hsze/0x10000)
        btsend.append(lsze)
        sze = hsze - lsze*0x10000
        hsze = int(sze/0x100)
        lsze =sze%0x100
        btsend.append(hsze)
        btsend.append(lsze)
        bcc=0
        for bt in btsend:
            bcc = bcc ^ bt
        btsend.append(bcc)
        btsend.append(flesze)
        for ch in FileName:
            btsend.append(ord(ch))
        btsend = btsend + bDta
        bcc=0
        for bt in btsend:
            bcc = bcc ^ bt
        btsend.append(bcc)
        return btsend