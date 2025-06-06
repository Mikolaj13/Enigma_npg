from Windows import MainWindow, PlugBoardWindow, SettingsWindow,IsItEncodingOrDecodingWindow


def main():
    plugboardwindow = PlugBoardWindow.PlugBoardWindow()
    plugboardwindow.mainloop()

    settingswindow = SettingsWindow.SettingWindow()
    settingswindow.mainloop()

    iieodwindow=IsItEncodingOrDecodingWindow.IsItEncodingOrDecodingWindow()
    iieodwindow.mainloop()

    mainwindow = MainWindow.EnigmaApp(settingswindow.get_settings(), plugboardwindow.get_plugboard(),iieodwindow.get())
    mainwindow.bind("<KeyPress>", mainwindow.on_key_press)
    settingswindow.mainloop()

main()
