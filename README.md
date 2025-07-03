
# User Registration API with n8n Webhook Integration

This project is a **User Registration API built using Django** that integrates with an **n8n workflow** to send a registration confirmation email after a successful signup.

I have created a **registration page in HTML**, which can be accessed at the endpoint **`/api/register`**. This webpage consists of three fields for entering **username, email, and password** respectively. By submitting the form, it validates the inputs, returns a response, and sends a request to the **n8n webhook**. Below I have attached the screenshots of the registration page and the response page.

---

### REGISTRATION PAGE

![register page](https://github.com/user-attachments/assets/9818a93a-347b-4563-a562-1ea0aaea281b)

---

### RESPONSE

![registration success](https://github.com/user-attachments/assets/928505e3-aab5-4808-8fd5-239264e4a18f)

![error message](https://github.com/user-attachments/assets/2e1d72bc-d5f7-4e9f-9fea-9b02b8e810ec)

---

## n8n Email Workflow Integration

For sending mail using **n8n**, I have used their **cloud trial**, which offers **14 days of free usage**.

In **n8n**, I have created a new workflow with two nodes — **Webhook** and **Email** — for receiving the JSON data from Django and sending mail to the registered email after a successful registration.

1. **Webhook Node:** Receives POST data from Django (username and email).

2. **Send Email Node:** Sends a welcome email to the registered user's email.

I have declared the **n8n webhook production URL** (`https://amil-harshak.app.n8n.cloud/webhook/register-user-email`) in **Django's `settings.py`** and called it accordingly.

The workflow is also uploaded in the repository as **`My workflow 2.json`**.

---

The screenshots of the **n8n workflow**, **Webhook node**, **Send Email node**, and the **mail received after a successful registration** are attached below.

---

### N8N WORKFLOW

![n8n workflow](https://github.com/user-attachments/assets/c6359825-d642-48ab-a550-ce44933bfe76)

---

### N8N WEBHOOK NODE

![n8n webhook](https://github.com/user-attachments/assets/de963de4-6722-4176-96a0-6848c7587d59)

---

### N8N SEND EMAIL NODE

![n8n email settings](https://github.com/user-attachments/assets/7e964410-36bb-4a74-a7a3-44efa80b135d)

---

### RECEIVED MAIL

![recieved mail](https://github.com/user-attachments/assets/d5e9f1e4-ac58-4863-a2bf-b6026fbcca9c)

---
