from datetime import datetime

photo3 = "https://telegra.ph/file/816a63029c5ed26f3037a.jpg"


def sample_response(input_text):
  user_message = str(input_text).lower()

  if user_message in ("hi", "hello", "sup", "hiii", "hii", "kha hai"):
    return f"{photo3}\n\
    hey! sage is not here i am lara wanna play with me"

  if user_message in ("sage", "sagexdd", "your sage", "@sage_xd"):
    return "HE is busy in her schedule. you can tell me i inform her"
  if user_message in ("bsdk", "madharchod", "bkl", "behanchod", "cgutiya",
                      "gaandu"):
    return "Sage papa ke bina gaali mat bak aane de use"

  if user_message in ("ladki", "pyar", "dhoka"):
    return "Pyar ek dhoka hai...aur baaki gamdu ki gaand maar yahi sahi moka hai"

  if user_message in ("time", "time?", "waqt"):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y, %H:%M:%S")

    return f"chal ab time dekh {str(date_time)}. haa dekh liya na time ab bhaag"
  # return "I don't understand"


# from replit import db
