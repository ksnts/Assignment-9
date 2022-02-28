from unicodedata import name
from fpdf import FPDF
import json

with open("myresume.json", "r") as resumeJson:
    resumeData = json.loads(resumeJson.read())

my_pdf = FPDF('P', 'mm', 'Letter')


my_pdf.add_page()

def contactdata(contact):
    contact.set_font('Arial', '', 10)
    contact.cell(40,3,""+str(resumeData["ContactHeader"][0]["Address"]),align='L', ln=0)
    contact.cell(40,5,""+str(resumeData["ContactHeader"][0]["Telephone"]),align='L', ln=1)
    contact.cell(40,5,""+str(resumeData["ContactHeader"][0]["Linkedin"]),align='L', ln=0)
    contact.cell(40,5,""+str(resumeData["ContactHeader"][0]["Email"]),align='L', ln=1)
    contact.cell(40,5,""+str(resumeData["ContactHeader"][0]["Github"]),align='L', ln=1)
    contact.set_fill_color(224,224,224)
    contact.cell(200,3, fill=True)
    contact.ln(1)


def introduction(intro):
    intro.set_font('Arial', 'B', 30)
    intro.set_fill_color(224,224,224)
    intro.cell(20,10,""+str(resumeData["Intro"][0]["Name"]), ln=1)
    intro.set_font('Arial', '', 20)
    intro.cell(20,8,""+str(resumeData["Intro"][0]["Position"]), ln=1)
    intro.set_fill_color(224,224,224)
    intro.cell(200,3, fill=True)
    intro.ln(5)
    
    

def projectsdata(projects):
    projects.set_font('Arial', 'B', 20)
    projects.set_text_color(0,200,200)
    projects.cell(20,17,""+str(resumeData["ProjectsHeader"][0]["ProjectHeader"]),ln=1)
    projects.set_text_color(0,0,0)
    projects.set_font('Arial', 'B', 16)
    projects.cell(20,0,""+str(resumeData["ProjectsHeader"][0]["Project1"]), ln=1)
    projects.ln(4)
    projects.set_font('Arial', '', 10)
    projects.cell(20,5,"    "+str(resumeData["ProjectsHeader"][0]["Project1D"][0]), ln=1)
    projects.cell(20,5,"    "+str(resumeData["ProjectsHeader"][0]["Project1D"][1]), ln=1)
    projects.cell(20,5,"    "+str(resumeData["ProjectsHeader"][0]["Project1D"][2]), ln=1)
    projects.ln(4)
    projects.set_font('Arial', 'B', 16)
    projects.cell(20,0,""+str(resumeData["ProjectsHeader"][0]["Project2"]), ln=1)
    projects.ln(4)
    projects.set_font('Arial', '', 10)
    projects.cell(20,5,"    "+str(resumeData["ProjectsHeader"][0]["Project2D"][0]), ln=1)
    projects.cell(20,5,"    "+str(resumeData["ProjectsHeader"][0]["Project2D"][1]), ln=1)
    projects.ln(4)
    projects.set_font('Arial', 'B', 16)
    projects.cell(20,0,""+str(resumeData["ProjectsHeader"][0]["Project3"]), ln=1)
    projects.ln(4)
    projects.set_font('Arial', '', 10)
    projects.cell(20,5,"    "+str(resumeData["ProjectsHeader"][0]["Project3D"][0]), ln=1)
    projects.cell(20,5,"    "+str(resumeData["ProjectsHeader"][0]["Project3D"][1]), ln=1)
    projects.ln(3)
    projects.set_fill_color(224,224,224)
    projects.cell(200,3, fill=True)
    projects.ln(1)

def experiencedata(experience):
    experience.set_font('Arial', 'B', 20)
    experience.set_text_color(0,200,200)
    experience.cell(20,17,""+str(resumeData["ExperienceHeader"][0]["ExpHeader"]),ln=1)
    experience.set_font('Arial', 'B', 16)
    experience.set_text_color(0,0,0)
    experience.cell(20,0,""+str(resumeData["ExperienceHeader"][0]["Experience1"]), ln=1)
    experience.ln(4)
    experience.set_font('Arial', '', 10)
    experience.cell(20,5,"    "+str(resumeData["ExperienceHeader"][0]["Experience1T"]), ln=1)
    experience.cell(20,5,"    "+str(resumeData["ExperienceHeader"][0]["Experience1D"][0]), ln=1)
    experience.cell(20,5,"    "+str(resumeData["ExperienceHeader"][0]["Experience1D"][1]), ln=1)
    experience.cell(20,5,"    "+str(resumeData["ExperienceHeader"][0]["Experience1D"][2]), ln=1)
    experience.ln(4)
    experience.set_font('Arial', 'B', 16)
    experience.cell(20,0,""+str(resumeData["ExperienceHeader"][0]["Experience2"]), ln=1)
    experience.ln(4)
    experience.set_font('Arial', '', 10)
    experience.cell(20,5,"    "+str(resumeData["ExperienceHeader"][0]["Experience2T"]), ln=1)
    experience.cell(20,5,"    "+str(resumeData["ExperienceHeader"][0]["Experience2D"][0]), ln=1)
    experience.cell(20,5,"    "+str(resumeData["ExperienceHeader"][0]["Experience2D"][1]), ln=1)
    experience.ln(3)
    experience.set_fill_color(224,224,224)
    experience.cell(200,3, fill=True)
    experience.ln(3)

def educationdata(education):
    education.set_font('Arial', 'B', 20)
    education.set_text_color(0,200,200)
    education.cell(20,17,""+str(resumeData["EducationHeader"][0]["EducHeader"]),ln=1)
    education.set_font('Arial', 'B', 16)
    education.set_text_color(0,0,0)
    education.cell(20,0,""+str(resumeData["EducationHeader"][0]["Education1"]), ln=1)
    education.ln(4)
    education.set_font('Arial', '', 10)
    education.cell(10,5,"    "+str(resumeData["EducationHeader"][0]["Education1T"]), ln=1)
    education.cell(20,5,"    "+str(resumeData["EducationHeader"][0]["Education1D"]), ln=1)
    education.ln(4)
    education.set_font('Arial', 'B', 16)
    education.cell(20,0,""+str(resumeData["EducationHeader"][0]["Education2"]), ln=1)
    education.ln(4)
    education.set_font('Arial', '', 10)
    education.cell(20,5,"    "+str(resumeData["EducationHeader"][0]["Education2T"]), ln=1)
    education.cell(20,5,"    "+str(resumeData["EducationHeader"][0]["Education2D"]), ln=1)
    education.ln(3)
    education.set_fill_color(224,224,224)
    education.cell(200,3, fill=True)










introduction(my_pdf)
contactdata(my_pdf)
projectsdata(my_pdf)
experiencedata(my_pdf)
educationdata(my_pdf)


my_pdf.output("SANTOS_JOHN.pdf")



