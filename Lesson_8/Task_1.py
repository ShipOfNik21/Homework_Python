import re

def email_parse(email_adress):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email.adress):
        raise ValueError(f'wronf email: {email_adress}')
    print(re_email.match(email_adress).groupdict())


for i in ['someon@geekbrains.ru', 'som@eone@geekbrainsru', 'someon@geekbrainsru']:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)