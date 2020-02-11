class RcvProt:
    def __init__(self):
        self.btary = bytearray();
        self.btFileName =bytearray()
        self.state = 0
        self.dtaSze = 0
        self.Sze = 0
        self.Bcc = 0
        self.lst = []
    def ByteTrace(self,dta):
        self.Bcc = self.Bcc ^ dta
        self.TracePrt(dta)
    def TracePrt(self,dta):
        if self.state == 0:
            if dta == 0x4A:
                self.Bcc = 0x4A
                self.state = 1
            else:
                self.lst.append(dta)
        elif self.state == 1:
            if dta ==0x12:
                self.state = 2
            else:
                self.state = 0
                self.lst.append(0x4a)
                self.lst.append(dta)
        elif self.state == 2:
            if dta ==0x8b:
                self.state = 3
            else:
                self.state = 0
                self.lst.append(0x4a)
                self.lst.append(0x12)
                self.lst.append(dta)
        elif self.state == 3:
            if dta == 0x13:
                self.Sze = 0
                self.state = 4
            else:
                self.state = 0
                self.lst.append(0x4a)
                self.lst.append(0x12)
                self.lst.append(0x8b)
                self.lst.append(dta)
        elif self.state == 4:
            self.dtaSze = dta*0x1000000;
            self.state = 5
        elif self.state == 5:
            self.dtaSze =self.dtaSze +  dta*0x10000
            self.state = 6
        elif self.state == 6:
            self.dtaSze = self.dtaSze + dta*0x100
            self.state = 7
        elif self.state == 7:
            self.dtaSze = self.dtaSze + dta
            self.state = 8
        elif self.state == 8:
            if self.Bcc == 0:
                self.state = 9
            else:
                self.lst.append('Syntex Error!!!')
                self.state = 0
        elif self.state == 9:
            self.Sze = dta
            self.dtaSze = self.dtaSze - self.Sze - 1
            self.btFileName.clear()
            if self.Sze == 0:
                self.lst.append('Syntex Error!!!')
                self.state = 0
            else:
                self.state = 10
        elif self.state == 10:
            self.btFileName.append(dta)
            self.Sze = self.Sze - 1
            if self.Sze == 0:
                self.state = 11
                self.btary.clear()
        elif self.state == 11:
            self.btary.append(dta)
            self.dtaSze = self.dtaSze - 1
            if self.dtaSze == 0:
                self.state = 12
        elif self.state == 12:
            if self.Bcc == 0:
                self.FileSave()
            self.state = 0
            
    def FileSave(self):
        fstr = ''
        for bt in self.btFileName:
            fstr = fstr+chr(bt)
        fle = open(fstr,'wb')
        fle.write(self.btary)
        fle.close()
        print(fstr,'File is Saved!!!')
