#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode wxPython tutorial

This example shows a simple menu.

author: Jan Bodnar
website: www.zetcode.com
last modified: April 2018
"""

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)
        self.Centre()
        self.initUI()

    def initUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.append(fileMenu, '&file')
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(5, 4, 5, 5)

        gs.AddMany([(wx.Button(self, label='Cls'), 0, wx.EXPAND),
            (wx.Button(self, label='Cls'), 0, wx.EXPAND),
            (wx.Button(self, label='Cls'), 0, wx.EXPAND),
            (wx.Button(self, label='Cls'), 0, wx.EXPAND),
            (wx.Button(self, label='Cls'), 0, wx.EXPAND),
            (wx.Button(self, label='Cls'), 0, wx.EXPAND),
            (wx.Button(self, label='Cls'), 0, wx.EXPAND),
            (wx.Button(self, label='Cls'), 0, wx.EXPAND),])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

def main():
    app = wx.App()
    ex = Example(None, title='Calcutator')
    ex.Show()
    app.MainLoop()

main()
