from django.core.mail import send_mail

def send(user_email,massage):

    send_mail(
        user_email, # main text
        massage, # text
        user_email, # from which mail(с какой почты)
        ['alexandrzambzhitskiy@gmail.com'],#  which mail(на какую почту)
        fail_silently=False
    )
    print("yrs")

def sending(user_email,massage):

    send_mail(
        user_email, # main text
        massage, # text
        user_email, # from which mail(с какой почты)
        ['alexandrzambzhitskiy@gmail.com'],#  which mail(на какую почту)
        fail_silently=False
    )
    print("yrs")

def get_client_ip(self, request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

#celery -A hotel worker -l INFO     -----для запуска celery