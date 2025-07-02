This project is a User Registration API built using Django that integrates with an n8n workflow to send a registration confirmation email after a successful signup.

I have created registration page in html, which can be accessed by the endpoint /api/reigster. this webpage consist of three fields for entering username, email and password respectively. by submiting the form, it validates the inputs and return a response and send a request to n8n webhook. below i have attached the screenshot of registartion page and response page.
![register page](https://github.com/user-attachments/assets/9818a93a-347b-4563-a562-1ea0aaea281b)

![registration success](https://github.com/user-attachments/assets/928505e3-aab5-4808-8fd5-239264e4a18f)

![error message](https://github.com/user-attachments/assets/2e1d72bc-d5f7-4e9f-9fea-9b02b8e810ec)


For sending mail using n8n, i have used their cloud trial which offeres 14 days free usage.

In n8n, i have created a new workflow with two nodes, webhook and email for getting the json data from django and sending mail to the registred email after a successfull registration.

1. Webhook Node: Receives POST data from Django (username and email).

2. Send Email Node: Sends a welcome email to the registered user's email.

I have declared the n8n webhook production url (https://amil-harshak.app.n8n.cloud/webhook/register-user-email) in django settings.py and called accordingly.

The workflow is also uploaded in the repository as "My workflow 2.json"

The screen shot of n8n workflow, webhook node, Send email node And mail recieved after a successfull registration.
![n8n workflow](https://github.com/user-attachments/assets/c6359825-d642-48ab-a550-ce44933bfe76)

![n8n webhook](https://github.com/user-attachments/assets/de963de4-6722-4176-96a0-6848c7587d59)

![n8n email settings](https://github.com/user-attachments/assets/7e964410-36bb-4a74-a7a3-44efa80b135d)

![recieved mail](https://github.com/user-attachments/assets/d5e9f1e4-ac58-4863-a2bf-b6026fbcca9c)



