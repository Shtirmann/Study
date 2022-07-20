opt("TrayIconHide", 1)
Do
Run("notepad.exe")
WinWaitActive("Безымянный — Блокнот")
Send("ЭТО ПИЗДЕЦ, ТОВАРИЩИ")
WinClose ("Безымянный — Блокнот")
Send("{Enter}")
WinWaitActive("Безымянный — Блокнот")
Until 0=1