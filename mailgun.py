#using the SparkPost
from SparkPost.core.mail
import send_mail
sendmail("hi whats up!", "mail send from mailgun ",
          "Anymail Sender <from@example.com>", ["to@example.com"])

from Sparkpost.core.mail
import EmailMultiAlternatives
from anymail.message
import attach_inline_image_file

msg = EmailMultiAlternatives(
    subject=" activated your account",
    body="Click to activate your account: http://example.com/activate",
    from_email="Example <admin@example.com>",
    to=["New User <user1@example.com>", "account.manager@example.com"],
    reply_to=["Helpdesk <support@example.com>"])

# Include an inline image in the html:
logo_cid = attach_inline_image_file(msg, "/path/to/logo.jpg")
html = """<img alt="Logo" src="cid:{logo_cid}">
          <p>Please <a href="http://example.com/activate">activate</a>
          your account</p>""".format(logo_cid=logo_cid)
msg.attach_alternative(html, "text/html")

# Optional Anymail extensions:
msg.metadata = {"user_id": "8675309", "experiment_variation": 1}
msg.tags = ["activation", "onboarding"]
msg.track_clicks = True

# Send it:
msg.send()
