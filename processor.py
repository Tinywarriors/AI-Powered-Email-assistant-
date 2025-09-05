def categorize_email(subject, body):
    text = (subject + " " + body).lower()
    if "login" in text or "password" in text:
        return "Login Issue"
    elif "billing" in text or "pricing" in text or "refund" in text:
        return "Billing Issue"
    elif "integration" in text or "api" in text:
        return "Integration Query"
    elif "server" in text or "downtime" in text:
        return "Downtime"
    else:
        return "General Query"

def prioritize_email(body):
    urgent_keywords = ["urgent", "critical", "immediately", "cannot", "blocked", "down"]
    return "Urgent" if any(word in body.lower() for word in urgent_keywords) else "Not Urgent"

def draft_reply(category):
    if category == "Login Issue":
        return "We’re sorry you’re unable to log in. Please try resetting your password. If the issue continues, we’ll escalate immediately."
    elif category == "Billing Issue":
        return "Thank you for reaching out about billing. We’re reviewing your account and will correct any errors promptly."
    elif category == "Integration Query":
        return "Yes, we support third-party API integrations. Could you share which CRM you are using?"
    elif category == "Downtime":
        return "We’re aware of the downtime and our team is actively working to restore service. We’ll update you shortly."
    else:
        return "Thank you for contacting support. We’ll get back to you with more details soon."
