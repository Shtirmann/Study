opt("TrayIconHide", 1)
Do
Run("notepad.exe")
WinWaitActive("���������� � �������")
Send("��� ������, ��������")
WinClose ("���������� � �������")
Send("{Enter}")
WinWaitActive("���������� � �������")
Until 0=1