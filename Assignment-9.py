from unicodedata import name
from fpdf import FPDF
import json

with open("myresume.json", "r") as resumeJson:
    resumeData = json.loads(resumeJson.read())

my_pdf = FPDF('P', 'mm', 'Letter')


my_pdf.add_page()




def introduction(intro):
    intro.set_font('Arial', 'B', 30)
    intro.cell(40,1,""+str(resumeData["Intro"][0]["Name"]), ln=1)
    intro.set_font('Arial', '', 18)
    intro.cell(20,20,""+str(resumeData["Intro"][0]["Position"]), ln=1)
    

def projectsdata(projects):
    projects.set_font('Arial', '', 18)
    projects.cell(20,20,""+str(resumeData["ProjectsHeader"][0]["ProjectHeader"]),ln=1)
    projects.set_font('Arial', 'B', 16)
    projects.cell(20,0,""+str(resumeData["ProjectsHeader"][0]["Project1"]), ln=1)
    projects.ln(4)
    projects.set_font('Arial', '', 8)
    projects.cell(20,3,"    "+str(resumeData["ProjectsHeader"][0]["Project1D"][0]), ln=1)
    projects.cell(20,3,"    "+str(resumeData["ProjectsHeader"][0]["Project1D"][1]), ln=1)
    projects.cell(20,3,"    "+str(resumeData["ProjectsHeader"][0]["Project1D"][2]), ln=1)
    projects.ln(4)
    projects.set_font('Arial', 'B', 16)
    projects.cell(20,0,""+str(resumeData["ProjectsHeader"][0]["Project2"]), ln=1)
    projects.ln(4)
    projects.set_font('Arial', '', 8)
    projects.cell(20,3,"    "+str(resumeData["ProjectsHeader"][0]["Project2D"][0]), ln=1)
    projects.cell(20,3,"    "+str(resumeData["ProjectsHeader"][0]["Project2D"][1]), ln=1)
    projects.ln(4)
    projects.set_font('Arial', 'B', 16)
    projects.cell(20,0,""+str(resumeData["ProjectsHeader"][0]["Project3"]), ln=1)
    projects.ln(4)
    projects.set_font('Arial', '', 8)
    projects.cell(20,3,"    "+str(resumeData["ProjectsHeader"][0]["Project3D"][0]), ln=1)
    projects.cell(20,3,"    "+str(resumeData["ProjectsHeader"][0]["Project3D"][1]), ln=1)
    projects.ln(4)

def experiencedata(experience):
    experience.set_font('Arial', '', 18)
    experience.cell(20,20,""+str(resumeData["ExperienceHeader"][0]["ExpHeader"]),ln=1)
    experience.set_font('Arial', 'B', 16)
    experience.cell(20,0,""+str(resumeData["ExperienceHeader"][0]["Experience1"]), ln=1)
    experience.ln(4)
    experience.set_font('Arial', '', 8)
    experience.cell(20,3,"    "+str(resumeData["ExperienceHeader"][0]["Experience1T"]), ln=1)
    experience.cell(20,3,"    "+str(resumeData["ExperienceHeader"][0]["Experience1D"][0]), ln=1)
    experience.cell(20,3,"    "+str(resumeData["ExperienceHeader"][0]["Experience1D"][1]), ln=1)
    experience.cell(20,3,"    "+str(resumeData["ExperienceHeader"][0]["Experience1D"][2]), ln=1)
    experience.ln(4)
    experience.set_font('Arial', 'B', 16)
    experience.cell(20,0,""+str(resumeData["ExperienceHeader"][0]["Experience2"]), ln=1)
    experience.ln(4)
    experience.set_font('Arial', '', 8)
    experience.cell(20,3,"    "+str(resumeData["ExperienceHeader"][0]["Experience2T"]), ln=1)
    experience.cell(20,3,"    "+str(resumeData["ExperienceHeader"][0]["Experience2D"][0]), ln=1)
    experience.cell(20,3,"    "+str(resumeData["ExperienceHeader"][0]["Experience2D"][1]), ln=1)
    experience.cell(20,3,"    "+str(resumeData["ExperienceHeader"][0]["Experience2D"][2]), ln=1)
    experience.ln(4)

def educationdata(education):
    education.set_font('Arial', '', 18)
    education.cell(20,20,""+str(resumeData["EducationHeader"][0]["EducHeader"]),ln=1)
    education.set_font('Arial', 'B', 16)
    education.cell(20,0,""+str(resumeData["EducationHeader"][0]["Education1"]), ln=1)
    education.ln(4)
    education.set_font('Arial', '', 8)
    education.cell(10,3,"    "+str(resumeData["EducationHeader"][0]["Education1T"]), ln=1)
    education.cell(20,3,"    "+str(resumeData["EducationHeader"][0]["Education1D"]), ln=1)
    education.ln(4)
    education.set_font('Arial', 'B', 16)
    education.cell(20,0,""+str(resumeData["EducationHeader"][0]["Education2"]), ln=1)
    education.ln(4)
    education.set_font('Arial', '', 8)
    education.cell(20,3,"    "+str(resumeData["EducationHeader"][0]["Education2T"]), ln=1)
    education.cell(20,3,"    "+str(resumeData["EducationHeader"][0]["Education2D"]), ln=1)








introduction(my_pdf)
projectsdata(my_pdf)
experiencedata(my_pdf)
educationdata(my_pdf)

my_pdf.output("SANTOS_JOHN.pdf")



