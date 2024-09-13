from celery import shared_task


import time

from django.core.mail import send_mail

from pet_products.models import Order



@shared_task
def notify_user_about_new_order(order_id: int):
    order = Order.objects.select_related("user").get(pk=order_id)
    time.sleep(2)
    recipient_email = order.user.email
    message = f"New Order №{order.pk} has been created."
    print("Sending email to", recipient_email)
    try:
        send_mail(
            subject="New Order",
            message=message,
            from_email="email@example.com",
            recipient_list=[recipient_email],
            fail_silently=False,
        )
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")
