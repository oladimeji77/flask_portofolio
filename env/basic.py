from flask import Flask, render_template, request
from datetime import date
app = Flask(__name__)

@app.route("/index")
def index():
    today = date.today()
    todays_date_display = today.strftime("%B %d, %Y")
    todays_date = today.strftime("%Y")
    age = int(todays_date)-1994
    summary = "DevOps Engineer with 5+ years of experience in the IT industry. Proven ability to automate software development and deployment processes, improve software quality, and reduce costs. Strong technical skills and experience with a variety of DevOps tools and technologies."
    more = "Proven ability to lead and manage CI/CD initiatives, and to collaborate effectively with development, operations, and security teams."
    testimonial= "He gathers all of the information and facts to make a decision, which benefits the entire team.” He has shown a practical approach to solving problems by breaking down large concepts into smaller, more manageable tasks.”"
    skills = "Linux/Unix, Scripting (Bash, Python), Cloud (AWS, Azure, GCP), CI/CD (Jenkins, GitLab, CircleCI), Docker, Kubernetes, Terraform, Ansible, Nagios, Prometheus."
    about = "Experienced DevOps Engineer with 5+ years of hands-on experience supporting, automating, and optimizing mission critical deployments by leveraging configuration management, and DevOps processes."
    certificates = ["Linux Foundation Certified System Administrator (LFCS)","ITIL 4 Foundation IT Service Management","Microsoft Certified: Azure Cloud Administrator.","AWS Certified Cloud Practitioner.",
                    "Oracle Cloud Infrastructure Foundations 2021 Associate.","CompTIA ITF+ certified.", "ISO/IEC 27001 Information Security Associate™.","Aviatrix Certified Engineer: Aviatrix Multi-Cloud Networking Associate."]
    return render_template("index.html", about=about, testimonial=testimonial, age=age, todays_date=todays_date, todays_date_display=todays_date_display, skills=skills, more=more,certificates=certificates)

@app.route("/logic")
def logic():
    return render_template("logic.html")

@app.errorhandler(404)
def error(e):
    return render_template("404.html")

if __name__=="__main__":
    app.run()