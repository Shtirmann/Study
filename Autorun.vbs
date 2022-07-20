Set objExplorer = CreateObject("InternetExplorer.Application")
With objExplorer
    .Navigate "about:blank"
    .Visible = 1
    .Document.Title = "ЭТО ВИРУС. АААААааааа!!!!!1111"
    .Toolbar=False
    .Statusbar=False
    .Top=150	'Отступ сверху экрана
    .Left=600	'Отступ слева экрана
    .Height=760 'Высота окна
    .Width=730	'Ширина окна
    .Document.Body.InnerHTML = "<img src='C:\a.jpg'>"	'Изображение 700х700pix
End with