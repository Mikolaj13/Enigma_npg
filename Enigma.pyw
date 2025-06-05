from Windows import MainWindow, PlugBoardWindow, SettingsWindow


def main():
    plugboardwindow = PlugBoardWindow.PlugBoardWindow()
    plugboardwindow.mainloop()

    settingswindow = SettingsWindow.SettingApp()
    settingswindow.mainloop()

    mainwindow = MainWindow.EnigmaApp(settingswindow.get_settings(), plugboardwindow.get_plugboard())
    mainwindow.bind("<KeyPress>", mainwindow.on_key_press)
    settingswindow.mainloop()

main()
