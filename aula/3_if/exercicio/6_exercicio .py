#### 4. Faça um Programa que verifique se o e-mail digitado faz parte dos e-mails de spam.

emails_spam = "fulano@gmail.com,beltrano@gmail.com,ciclano@gmail.com"

email = input('Qual o e-mail? ')

if email in emails_spam:
    print('Esse e-mail é um span')
else:
    print('Esse e-mail não é spam')