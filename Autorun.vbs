Set objExplorer = CreateObject("InternetExplorer.Application")
With objExplorer
    .Navigate "about:blank"
    .Visible = 1
    .Document.Title = "��� �����. ����������!!!!!1111"
    .Toolbar=False
    .Statusbar=False
    .Top=150	'������ ������ ������
    .Left=600	'������ ����� ������
    .Height=760 '������ ����
    .Width=730	'������ ����
    .Document.Body.InnerHTML = "<img src='C:\a.jpg'>"	'����������� 700�700pix
End with