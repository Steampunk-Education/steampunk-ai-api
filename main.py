from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, RootModel
from mailersend import emails

APP_DESCRIPTION = """
Course information can be searched via the Steampunk AI API. 

## Email automation
The /email endpoint takes five inputs: `name`, `center`, `range`, `theme`, `email`<br>
`name`: Name of the education center<br>
`center`: The kind of education center Steampunk is serving<br>
`range`: The age range targetted by Steampunk's workshops<br>
`theme`: The theme of the workshops (ex: a robotics or AI workshop)<br>
`email`: The email of the user<br>
The API takes in all this info and sends a custom email to the user suggesting a workshop based on the inputs<br>
""" 

app = FastAPI(
    title="Steampunk AI API",
    description=APP_DESCRIPTION
)

mailer = emails.NewEmail("mlsn.31e210a1bbc436f25b9506ef64d34fce55b40ab04575cbea41ddf2892658e248")

mail_body = {}

mail_from = {
    "name": "Steampunk Education",
    "email": "zr6ke4nekjv4on12@trial-3zxk54vy1714jy6v.mlsender.net",
}

reply_to = {
    "name": "Steampunk Education",
    "email": "zr6ke4nekjv4on12@trial-3zxk54vy1714jy6v.mlsender.net",
}

@app.get("/email/")
def get_courses(name: str, center: str, range: str, theme: str, email: str):
    recipients = [
        {
            "name": "Gabe Braden",
            "email": email,
        }
    ]

    # TODO: If you have time, use AI to suggest the workshop
    # TODO: Include the reason why in the HTML doc - Jinja templating? 

    file_name = "sumo"
    if center.lower() == "homeschool":
        file_name = "mars-rover"
    elif center.lower() == "library":
        file_name = "vr"

    if theme.lower() == "robotics":
        file_name = "sumo"
    if theme.lower() == "vr":
        file_name = "vr"

    html_file = ""
    with open(f"html-templates/{file_name}.html") as f:
        html_file += f.read()

    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject("Steampunk Education ~ Workshop Proposal 🎉", mail_body)
    mailer.set_html_content(html_file, mail_body)
    mailer.set_reply_to(reply_to, mail_body)

    print(mailer.send(mail_body))