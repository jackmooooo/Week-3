import wx


class Example(wx.Frame):


    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(1000, 500))

        self.displayer = ""
        self.leng = 0
        self.InitUI()
        self.Centre()


    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        b7_button = (wx.Button(self, label='7'))
        b8_button = (wx.Button(self, label='8'))
        b9_button = (wx.Button(self, label='9'))
        bforslash_button = (wx.Button(self, label='/'))
        bbintodec_button = (wx.Button(self, label='Binary to decimal'))
        b4_button = (wx.Button(self, label='4'))
        b5_button = (wx.Button(self, label='5'))
        b6_button = (wx.Button(self, label='6'))
        bx_button = (wx.Button(self, label='*'))
        bbintooct_button = (wx.Button(self, label='Binary to base 8 numbers'))
        b1_button = (wx.Button(self, label='1'))
        b2_button = (wx.Button(self, label='2'))
        b3_button = (wx.Button(self, label='3'))
        b__button = (wx.Button(self, label='-'))
        bbintohex_button = (wx.Button(self, label='Binary to hexadecimal numbers'))
        bo_button = (wx.Button(self, label='.'))
        b0_button = (wx.Button(self, label='0'))
        b___button = (wx.Button(self, label='='))
        bad_button = (wx.Button(self, label='+'))
        call_button = (wx.Button(self, label='clear'))
        bpwr_button = (wx.Button(self, label='^'))
        bbintobase36_button = (wx.Button(self, label='Binary to base-36 numbers'))

        self.Bind(wx.EVT_BUTTON, self.onButton_b7, (b7_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_b8, (b8_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_b8, (b9_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_forslash, (bforslash_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_dectobin, (bbintodec_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_b4, (b4_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_b5, (b5_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_b6, (b6_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_bx, (bx_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_bintooct, (bbintooct_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_b1, (b1_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_b2, (b2_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_b3, (b3_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_b_, (b__button))
        self.Bind(wx.EVT_BUTTON, self.onButton_bintohex, (bbintohex_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_bo, (bo_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_b0, (b0_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_b__, (b___button))
        self.Bind(wx.EVT_BUTTON, self.onButton_bad, (bad_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_call, (call_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_pwr, (bpwr_button))
        self.Bind(wx.EVT_BUTTON, self.onButton_bintobase36, (bbintobase36_button))

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(5, 5, 5, 5)


        gs.AddMany([(call_button, 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (bbintobase36_button, 0, wx.EXPAND),
            (b7_button, 0, wx.EXPAND),
            (b8_button, 0, wx.EXPAND),
            (b9_button, 0, wx.EXPAND),
            (bforslash_button, 0, wx.EXPAND),
            (bbintodec_button, 0, wx.EXPAND),
            (b4_button, 0, wx.EXPAND),
            (b5_button, 0, wx.EXPAND),
            (b6_button, 0, wx.EXPAND),
            (bx_button, 0, wx.EXPAND),
            (bbintooct_button, 0, wx.EXPAND),
            (b1_button, 0, wx.EXPAND),
            (b2_button, 0, wx.EXPAND),
            (b3_button, 0, wx.EXPAND),
            (b__button, 0, wx.EXPAND),
            (bbintohex_button, 0, wx.EXPAND),
            (bo_button, 0, wx.EXPAND),
            (b0_button, 0, wx.EXPAND),
            (b___button, 0, wx.EXPAND),
            (bad_button, 0, wx.EXPAND),
            (bpwr_button, 0, wx.EXPAND)])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def Operations(self, numbers):
        def Addition(a,b):
            sum = a + b
            sum = str(sum)
            self.display.WriteText(sum)

        def Subtraction(a,b):
            difference = a - b
            difference = str(difference)
            self.display.WriteText(difference)

        def Multiplication(a,b):
            c = 0
            count = 0
            while(count < b):
                count += 1
                c += a
            product = c
            product = str(c)
            self.display.WriteText(product)

        def Division(a,b):
            count = 0
            while(a >= b):
                count += 1
                a -= b
            quotient = count
            quotient = str(quotient)
            self.display.WriteText(quotient)


        def Exponent(a,b):
            c = 1
            count = 0
            while(count < b):
                count += 1
                c *= a
            power = c
            power = str(power)
            self.display.WriteText(power)

        def Modulo(a,b):
            count = 0
            while(a >= b):
                count += 1
                a -= b
            remainder = a
            remainder = str(remainder)
            self.display.WriteText(remainder)

        def Bintodec(a):
            b = a.split('.')
            c = 0
            d = 0
            for i in range(len(b)):
                for x in range(len(b[i])):
                    if i == 0:
                        c += int(b[i][x])*(2**(len(b[i])-(x + 1)))
                    else:
                        d += int(b[i][x])*(2**(x-len(b[i])))
            e = str(c + d)
            self.display.WriteText(e)


        def Bintooc(a):
            left = ""
            right = ""
            if "." in a:
                [left, right] = a.split(".")
            else:
                left = a
            output = ""
            output2 = ""

            if len(left) % 3 == 1:
                left = "00" + left
            elif len(left) % 3 == 2:
                left = "0" + left

            if len(right) % 3 == 1:
                right = right + "00"
            elif len(right) % 3 == 2:
                right = right + "0"

            for value in range(0, len(left), 3):
                cur_group = left[value: value + 3]
                if cur_group == "000":
                    output = output + "0"
                elif cur_group == "001":
                    output = output + "1"
                elif cur_group == "010":
                    output = output + "2"
                elif cur_group == "011":
                    output = output + "3"
                elif cur_group == "100":
                    output = output + "4"
                elif cur_group == "101":
                    output = output + "5"
                elif cur_group == "110":
                    output = output + "6"
                elif cur_group == "111":
                    output = output + "7"

            if len(right) == 0:
                output2 = "0"
            else:
                for value in range(0, len(right), 3):
                    cur_group = right[value: value + 3]
                    if cur_group == "000":
                        output2 = output2 + "0"
                    elif cur_group == "001":
                        output2 = output2 + "1"
                    elif cur_group == "010":
                        output2 = output2 + "2"
                    elif cur_group == "011":
                        output2 = output2 + "3"
                    elif cur_group == "100":
                        output2 = output2 + "4"
                    elif cur_group == "101":
                        output2 = output2 + "5"
                    elif cur_group == "110":
                        output2 = output2 + "6"
                    elif cur_group == "111":
                        output2 = output2 + "7"

            if output2 == "0":
                self.display.WriteText(output)
            else:
                self.display.WriteText(output + "." + output2)

        def Bintohex(a):
            left = ""
            right = ""
            if "." in a:
                [left, right] = a.split(".")
            else:
                left = a
            output = ""
            output2 = ""

            if len(left) % 4 == 1:
                left = "000" + left
            elif len(left) % 4 == 2:
                left = "00" + left
            elif len(left) % 4 == 3:
                left = "0" + left

            if len(right) % 4 == 1:
                right = right + "000"
            elif len(right) % 4 == 2:
                right = right + "00"
            elif len(right) % 4 == 3:
                right = "0" + right

            for value in range(0, len(left), 4):
                cur_group = left[value: value + 4]
                if cur_group == "0000":
                    output = output + "0"
                elif cur_group == "0001":
                    output = output + "1"
                elif cur_group == "0010":
                    output = output + "2"
                elif cur_group == "0011":
                    output = output + "3"
                elif cur_group == "0100":
                    output = output + "4"
                elif cur_group == "0101":
                    output = output + "5"
                elif cur_group == "0110":
                    output = output + "6"
                elif cur_group == "0111":
                    output = output + "7"
                elif cur_group == "1000":
                    output = output + "8"
                elif cur_group == "1001":
                    output = output + "9"
                elif cur_group == "1010":
                    output = output + "A"
                elif cur_group == "1011":
                    output = output + "B"
                elif cur_group == "1100":
                    output = output + "C"
                elif cur_group == "1101":
                    output = output + "D"
                elif cur_group == "1110":
                    output = output + "E"
                elif  cur_group == "1111":
                    output = output + "F"


            if len(right) == 0:
                output2 = "0"
            else:
                for value in range(0, len(right), 4):
                    cur_group = right[value: value + 4]
                    if cur_group == "0000":
                        output2 = output2 + "0"
                    elif cur_group == "0001":
                        output2 = output2 + "1"
                    elif cur_group == "0010":
                        output2 = output2 + "2"
                    elif cur_group == "0011":
                        output2 = output2 + "3"
                    elif cur_group == "0100":
                        output2 = output2 + "4"
                    elif cur_group == "0101":
                        output2 = output2 + "5"
                    elif cur_group == "0110":
                        output2 = output2 + "6"
                    elif cur_group == "0111":
                        output2 = output2 + "7"
                    elif cur_group == "1000":
                        output2 = output2 + "8"
                    elif cur_group == "1001":
                        output2 = output2 + "9"
                    elif cur_group == "1010":
                        output2 = output2 + "A"
                    elif cur_group == "1011":
                        output2 = output2 + "B"
                    elif cur_group == "1100":
                        output2 = output2 + "C"
                    elif cur_group == "1101":
                        output2 = output2 + "D"
                    elif cur_group == "1110":
                        output2 = output2 + "E"
                    elif  cur_group == "1111":
                        output2 = output2 + "F"
            if output2 == "0":
                self.display.WriteText(output)
            else:
                self.display.WriteText(output + "." + output2)

        def Bintoalpha(a):
            left = ""
            right = ""
            if "." in a:
                [left, right] = a.split(".")
            else:
                left = a
            output = ""
            output2 = ""

            if len(left) % 6 == 1:
                left = "00000" + left
            elif len(left) % 6 == 2:
                left = "0000" + left
            elif len(left) % 6 == 3:
                left = "000" + left
            elif len(left) % 6 == 4:
                left = "00" + left
            elif len(left) % 6 == 5:
                left = "0" + left

            if len(right) % 6 == 1:
                right = "00000" + right
            elif len(left) % 6 == 2:
                right = "0000" + right
            elif len(left) % 6 == 3:
                right = "000" + right
            elif len(left) % 6 == 4:
                right = "00" + right
            elif len(left) % 6 == 5:
                right = "0" + right

            for value in range(0, len(left), 6):
                cur_group = left[value: value + 6]
                if cur_group == "000000":
                    output = output + "0"
                elif cur_group == "000001":
                    output = output + "1"
                elif cur_group == "000010":
                    output = output + "2"
                elif cur_group == "000011":
                    output = output + "3"
                elif cur_group == "000100":
                    output = output + "4"
                elif cur_group == "000101":
                    output = output + "5"
                elif cur_group == "000110":
                    output = output + "6"
                elif cur_group == "000111":
                    output = output + "7"
                elif cur_group == "001000":
                    output = output + "8"
                elif cur_group == "001001":
                    output = output + "9"
                elif cur_group == "001010":
                    output = output + "A"
                elif cur_group == "001011":
                    output = output + "B"
                elif cur_group == "001100":
                    output = output + "C"
                elif cur_group == "001101":
                    output = output + "D"
                elif cur_group == "001110":
                    output = output + "E"
                elif  cur_group == "001111":
                    output = output + "F"
                elif  cur_group == "010000":
                    output = output + "G"
                elif  cur_group == "010001":
                    output = output + "H"
                elif  cur_group == "010010":
                    output = output + "I"
                elif  cur_group == "010011":
                    output = output + "J"
                elif  cur_group == "010100":
                    output = output + "K"
                elif  cur_group == "010101":
                    output = output + "L"
                elif  cur_group == "010110":
                    output = output + "M"
                elif  cur_group == "010111":
                    output = output + "N"
                elif  cur_group == "011000":
                    output = output + "O"
                elif  cur_group == "011001":
                    output = output + "P"
                elif  cur_group == "011010":
                    output = output + "Q"
                elif  cur_group == "011011":
                    output = output + "R"
                elif  cur_group == "011100":
                    output = output + "S"
                elif  cur_group == "011101":
                    output = output + "T"
                elif  cur_group == "011110":
                    output = output + "U"
                elif  cur_group == "011111":
                    output = output + "V"
                elif  cur_group == "100000":
                    output = output + "W"
                elif  cur_group == "100001":
                    output = output + "X"
                elif  cur_group == "100010":
                    output = output + "Y"
                elif  cur_group == "100011":
                    output = output + "Z"
                elif  cur_group == "100100":
                    output = output + " "




            if len(right) == 0:
                output2 = "0"
            else:
                for value in range(0, len(right), 6):
                    cur_group = right[value: value + 6]
                    if cur_group == "000000":
                        output2 = output2 + "0"
                    elif cur_group == "000001":
                        output2 = output2 + "1"
                    elif cur_group == "000010":
                        output2 = output2 + "2"
                    elif cur_group == "000011":
                        output2 = output2 + "3"
                    elif cur_group == "000100":
                        output2 = output2 + "4"
                    elif cur_group == "000101":
                        output2 = output2 + "5"
                    elif cur_group == "000110":
                        output2 = output2 + "6"
                    elif cur_group == "000111":
                        output2 = output2 + "7"
                    elif cur_group == "001000":
                        output2 = output2 + "8"
                    elif cur_group == "001001":
                        output2 = output2 + "9"
                    elif cur_group == "001010":
                        output2 = output2 + "A"
                    elif cur_group == "001011":
                        output2 = output2 + "B"
                    elif cur_group == "001100":
                        output2 = output2 + "C"
                    elif cur_group == "001101":
                        output2 = output2 + "D"
                    elif cur_group == "001110":
                        output2 = output2 + "E"
                    elif  cur_group == "001111":
                        output2 = output2 + "F"
                    elif  cur_group == "010000":
                        output2 = output2 + "G"
                    elif  cur_group == "010001":
                        output2 = output2 + "H"
                    elif  cur_group == "010010":
                        output2 = output2 + "I"
                    elif  cur_group == "010011":
                        output2 = output2 + "J"
                    elif  cur_group == "010100":
                        output2 = output2 + "K"
                    elif  cur_group == "010101":
                        output2 = output2 + "L"
                    elif  cur_group == "010110":
                        output2 = output2 + "M"
                    elif  cur_group == "010111":
                        output2 = output2 + "N"
                    elif  cur_group == "011000":
                        output2 = output2 + "O"
                    elif  cur_group == "011001":
                        output2 = output2 + "P"
                    elif  cur_group == "011010":
                        output2 = output2 + "Q"
                    elif  cur_group == "011011":
                        output2 = output2 + "R"
                    elif  cur_group == "011100":
                        output2 = output2 + "S"
                    elif  cur_group == "011101":
                        output2 = output2 + "T"
                    elif  cur_group == "011110":
                        output2 = output2 + "U"
                    elif  cur_group == "011111":
                        output2 = output2 + "V"
                    elif  cur_group == "100000":
                        output2 = output2 + "W"
                    elif  cur_group == "100001":
                        output2 = output2 + "X"
                    elif  cur_group == "100010":
                        output2 = output2 + "Y"
                    elif  cur_group == "100011":
                        output2 = output2 + "Z"
                    elif  cur_group == "100100":
                        output2 = output2 + " "

            if output2 == "0":
                self.display.WriteText(output)
            else:
                self.display.WriteText(output + "." + output2)



        if '+' in numbers:
            [a, b] = numbers.split("+")
            Addition(int(a),int(b))
        elif '-' in numbers:
            [a, b] = numbers.split("-")
            Subtraction(int(a), int(b))
        elif '*' in numbers:
            [a, b] = numbers.split("*")
            Multiplication(int(a), int(b))
        elif '/' in numbers:
            [a, b] = numbers.split("/")
            Division(int(a), int(b))
        elif '^' in numbers:
            [a, b] = numbers.split("^")
            Exponent(int(a), int(b))
        elif '%' in numbers:
            [a, b] = numbers.split("%")
            Modulo(int(a), int(b))
        elif '_bintodec' in numbers:
            [a, b] = numbers.split("_bintodec")
            Bintodec(str(a))
        elif '_bintooct' in numbers:
            [a, b] = numbers.split("_bintooct")
            Bintooc(str(a))
        elif '_bintohex' in numbers:
            [a, b] = numbers.split("_bintohex")
            Bintohex(str(a))
        elif '_bintoalpha' in numbers:
            [a, b] = numbers.split("_bintoalpha")
            Bintoalpha(str(a))



    def onButton_call(self, event):
        self.display.Clear()
        self.displayer = ""
        self.leng = 0
    def onButton_b7(self, event):
        self.display.WriteText("7")
        self.displayer += "7"
        self.leng += 1
    def onButton_b8(self, event):
        self.display.WriteText("8")
        self.displayer += "8"
        self.leng += 1
    def onButton_b9(self, evenr):
        self.display.WriteText("9")
        self.displayer += "9"
        self.leng += 1
    def onButton_forslash(self, event):
        self.display.WriteText("/")
        self.displayer += "/"
        self.leng += 1
    def onButton_dectobin(self, event):
        self.display.WriteText("_bintodec")
        self.displayer += "_bintodec"
        self.leng += 9
    def onButton_b4(self, event):
        self.display.WriteText("4")
        self.displayer += "4"
        self.leng += 1
    def onButton_b5(self, event):
        self.display.WriteText("5")
        self.displayer += "5"
        self.leng += 1
    def onButton_b6(self, event):
        self.display.WriteText("6")
        self.displayer += "7"
        self.leng += 1
    def onButton_bx(self, event):
        self.display.WriteText("*")
        self.displayer += "*"
        self.leng += 1
    def onButton_bintooct(self, event):
        self.display.WriteText("_bintooct")
        self.displayer += "_bintooct"
        self.leng += 1
    def onButton_b1(self, event):
        self.display.WriteText("1")
        self.displayer += "1"
        self.leng += 1
    def onButton_b2(self, event):
        self.display.WriteText("2")
        self.displayer += "2"
        self.leng += 1
    def onButton_b3(self, event):
        self.display.WriteText("3")
        self.displayer += "3"
        self.leng += 1
    def onButton_b_(self, event):
        self.display.WriteText("-")
        self.displayer += "-"
        self.leng += 1
    def onButton_bintohex(self, event):
        self.display.WriteText("_bintohex")
        self.displayer += "_bintohex"
        self.leng += 9
    def onButton_bo(self, event):
        self.display.WriteText(".")
        self.displayer += "."
        self.leng += 1
    def onButton_b0(self, event):
        self.display.WriteText("0")
        self.displayer += "0"
        self.leng += 1
    def onButton_b__(self, event):
        self.display.WriteText("=")
        self.leng += 1
        self.Operations(self.displayer)
    def onButton_bad(self, event):
        self.display.WriteText("+")
        self.displayer += "+"
        self.leng += 1
    def onButton_pwr(self, event):
        self.display.WriteText("^")
        self.displayer += "^"
        self.leng += 1
    def onButton_bintobase36(self, event):
        self.display.WriteText("_bintoalpha")
        self.displayer += "_bintoalpha"
        self.leng += 1




def main():

    app = wx.App()
    ex = Example(None, title='Calculator')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
