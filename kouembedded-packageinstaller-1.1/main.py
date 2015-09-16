#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2015 Ata Niyazov <ata.niazov@gmail.com> & Taner Guven <tanerguven@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import subprocess
import Tkinter as tk
import tkMessageBox
import apt

PROGRAMS = [
    ("Programlama Dersi Programlari", "kouembedded-programming-course"),
    ("Programlanabilir Yapilar Dersi Programlari", "kouembedded-programmablestructures-course"),
    ("Web Browser (Firefox)", "firefox"),
    ("Ubuntu Software Center", "software-center"),
]


def get_installed_programs():
    apt_cache = apt.Cache()
    installed = set()
    uninstalled = set()
    for package_title, package_name in PROGRAMS:
        if package_name not in apt_cache:
            print "WARNING: package not found: %s" % package_name
        elif apt_cache[package_name].is_installed:
            installed.add(package_name)
        else:
            uninstalled.add(package_name)
    return installed, uninstalled

def configure(install_package_list, remove_package_list):
    install_package_list = " ".join(install_package_list)
    remove_package_list = " ".join(remove_package_list)

    cmd = "xterm -e 'bash -c \"apt-get -y update && apt-get -y install %s && apt-get -y autoremove --purge %s\"'" % (
        install_package_list, remove_package_list
    )

    print cmd
    os.execl("/usr/bin/gksudo", "gksudo", cmd)


def system_update():
    cmd = "xterm -e 'bash -c \"apt-get -y update && apt-get -y dist-upgrade \"'"
    print cmd
    os.execl("/usr/bin/gksudo", "gksudo", cmd)


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.program_list = []

        installed_packages, uninstalled_packages = get_installed_programs()
        for package_title, package_name in PROGRAMS:
            v = tk.StringVar()
            if package_name in installed_packages:
                v.set(package_name)
            else:
                v.set("")
            cb = tk.Checkbutton(self, text=package_title, variable=v, onvalue=package_name, offvalue="")
            cb.pack()
            self.program_list.append(v)

        self.submitButton = tk.Button(self, text="Kaydet", command=self.query_checkbuttons)
        self.submitButton.pack()

        self.updateButton = tk.Button(self, text="Sistemi Guncelle", command=self.updateButton_clicked)
        self.updateButton.pack()


    def updateButton_clicked(self):
        system_update()


    def query_checkbuttons(self):

        selected = set()
        for var in self.program_list:
            value = var.get()
            if value != "":
                selected.add(value)
        installed, uninstalled = get_installed_programs()
        install_package_list = selected - installed
        remove_package_list = installed - selected

        print "uninstalled:", uninstalled
        print "installed:", installed
        print "selected:", selected
        print "remove:", install_package_list
        print "install:", remove_package_list


        if len(install_package_list) == 0 and len(remove_package_list) == 0:
            return

        result = tkMessageBox.askquestion("Degisiklikleri Kaydet", "Bu islem icin internet baglantisi gerekmektedir. Islem yapilsin mi?", icon='warning')
        if result == 'yes':
            pass
        else:
            return

        configure(install_package_list, remove_package_list)


gui = GUI()
gui.minsize(width=480, height=320)
# gui.maxsize(width=640, height=500)
gui.mainloop()
