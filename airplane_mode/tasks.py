import frappe

def send_rent_payment_reminders():
    print("Hello")
    recipients = [
    'yash.wadgaonkar@hostingduty.com'
    ]
    
    frappe.sendmail(
    recipients=recipients,
    sender= 'wadgaonkaryash782@gmail.com',
    subject=frappe._('Rent Payment Reminder'),
    template='rent_reminder',
    args=dict(
        reminder_text='Please Pay your rent',
        message='Your rent payment is due. Please pay your rent ASAP',
    ),
    header=('Shop Rent Reminder')
    )
    