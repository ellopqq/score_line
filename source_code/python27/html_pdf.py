import pdfkit

path_wk = r'C:\tools\wkhtmltox\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf = path_wk)
#pdfkit.from_url(url, r'D:\are you coding\pdf\taobao.pdf', configuration=config)


pdfkit.from_string('Hello!','out.pdf', configuration=config)