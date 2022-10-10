Set objExplorer = CreateObject("InternetExplorer.Application")
With objExplorer


'set WshShell = WScript.CreateObject("WScript.Shell")
'WshShell.Run """C:\Program Files\Mozilla Firefox\firefox.exe""",1

'With WshShell
    .Navigate "about:blank"
    .Visible = 1
    .Document.Title = "This is a VIRUS!!! AAAAAAAAAAAAaaaaa!!!1111"
    .Toolbar=False
    .Statusbar=False
    .Top=150	'Отступ сверху 150px
    .Left=600	'Отступ слева 600px
    .Height=760 'Высота окна 760px
    .Width=730	'Ширина окна 730px
    .Document.Body.InnerHTML = "<img src='C:\a.jpg'>"	'Путь к изображению размером 700x700px
End with