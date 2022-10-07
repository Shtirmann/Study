opt("TrayIconHide", 1)
Do
Run("notepad.exe")
WinWaitActive("Безымянный – Блокнот")
Send("ЭТО ПИЗДЕЦ, ТОВАРИЩИ")
WinClose ("*Безымянный – Блокнот")
Send("{Enter}")
WinWaitActive("Сохранение")
Send("Пиписька слона")
Send("{Enter}")
Until 0=1