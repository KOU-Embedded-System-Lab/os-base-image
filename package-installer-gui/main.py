#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
import subprocess
import Tkinter as tk
import tkMessageBox

PROGRAMS = [
    ("Programlama", "codeblocks"),
    ("Programlanabilir Yapilar", "tkgate-kou"),
    ("Ubuntu Software Center", "software-center"),
]

def run(cmd):
    p = subprocess.Popen(cmd, shell=True)
    p.communicate()
    r = p.wait()
    if r:
        return False
    return True


def get_installed_programs():
    installed = set()
    uninstalled = set()
    for package_title, package_name in PROGRAMS:
        if os.path.isfile("/var/lib/dpkg/info/%s.list" % package_name):
            installed.add(package_name)
        else:
            uninstalled.add(package_name)
    return installed, uninstalled

def configure(install_package_list, remove_package_list):
    install_package_list = " ".join(install_package_list)
    remove_package_list = " ".join(remove_package_list)

    cmd = "xfce4-terminal -e 'bash -c \"apt-get -y update && apt-get -y install %s && apt-get -y autoremove --purge %s\"'" % (
        install_package_list, remove_package_list
    )

    print cmd
    import os
    os.execl("/usr/bin/gksudo", "gksudo", cmd)


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.program_list = []

        for package_title, package_name in PROGRAMS:
            v = tk.StringVar()
            if os.path.isfile("/var/lib/dpkg/info/%s.list" % package_name):
                v.set(package_name)
            else:
                v.set("")
            cb = tk.Checkbutton(self, text=package_title, variable=v, onvalue=package_name, offvalue="")
            cb.pack()
            self.program_list.append(v)

        self.submitButton = tk.Button(self, text="Kaydet", command=self.query_checkbuttons)
        self.submitButton.pack()


        # self.tb_info.setText("asdda")

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
