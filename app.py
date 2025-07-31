<<<<<<< HEAD
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import json

with open("college_info.json", "r") as f:
    college_data = json.load(f)

# Extract undergraduate and postgraduate programs with safe .get() methods
college_name = college_data["srm_mcet"]["college_name"]
established_year = college_data["srm_mcet"]["established_year"]
affiliation = college_data["srm_mcet"]["affiliation"]
approval = college_data["srm_mcet"]["approval"]
location = college_data["srm_mcet"]["location"]
city = location["city"]
state = location["state"]
address = location["address"]

# Programs offered
ug_programs = college_data["srm_mcet"]["programs_offered"]["undergraduate"]
pg_programs = college_data["srm_mcet"]["programs_offered"]["postgraduate"]

# Fees structure
fees_structure = college_data["srm_mcet"]["fees_structure"]
be_fee = fees_structure["B.E./B.Tech"]
me_fee = fees_structure["M.E."]
mba_fee = fees_structure["MBA"]

# Admission criteria
ug_criteria = college_data["srm_mcet"]["admission_criteria"]["undergraduate"]
pg_criteria = college_data["srm_mcet"]["admission_criteria"]["postgraduate"]

# Events
events = college_data["srm_mcet"]["events"]
event_lines = (
    "\n".join(
        [
            f"- {event['title']} on {event['date']}: {event['description']}"
            for event in events
        ]
    )
    if events
    else "No events listed."
)

# ERP portal info
erp_portal = college_data["srm_mcet"]["erp_portal"]
admission_portal = erp_portal["portal_name"]
admission_portal_url = erp_portal["url"]

# Contact info
contact_info = college_data["srm_mcet"]["contact"]
website = contact_info["website"]
phone_numbers = ", ".join(contact_info["phone_numbers"])

# Placement details
placement_info = college_data["srm_mcet"]["placement"]
placement_title = placement_info["title"]
placement_assistance = placement_info["assistance"]
placement_vision = placement_info["vision"]
placement_objectives = "\n  - ".join(placement_info["objectives"])
training_programs = [
    "Communicative English Training Program",
    "Basic Grammar Training",
    "Career Awareness Program",
    "Coding Training",
    "Aptitude Test Training",
    "Group Discussion Practice",
    "Personal Interview Practice",
    "Placement Training Program",
    "Mock Recruitment Program",
    "Employability Training Camp",
]
competitive_exam_training = [
    "BEC",
    "GATE",
    "TOEFL",
    "IELTS",
    "T.I.M.E",
    "Networking",
    "Coding",
    "CAT Coaching",
    "MAT Coaching",
    "XAT Coaching",
    "CMAT Coaching",
    "ICET Coaching",
    "IIT Foundation",
]
industry_partners = ["L&T", "Infosys", "Vodafone", "Anna University Incubation Centre"]

# Clubs and Activities
clubs_info = college_data["srm_mcet"].get("clubs_and_activities", {})
clubs_overview = clubs_info.get("overview", "No overview available.")

# Technical Clubs
technical_clubs = clubs_info.get("categories", {}).get("technical_clubs", [])
technical_club_lines = (
    "\n  - "
    + "\n  - ".join(
        [
            f"{club['name']}: {club.get('description', 'No description')}"
            for club in technical_clubs
        ]
    )
    if technical_clubs
    else "No technical clubs listed."
)

# Departmental Associations
dept_assocs = clubs_info.get("categories", {}).get("departmental_associations", [])
dept_assoc_lines = (
    "\n  - "
    + "\n  - ".join(
        [f"{assoc['name']} ({assoc['department']})" for assoc in dept_assocs]
    )
    if dept_assocs
    else "No departmental associations listed."
)

# Cultural and Language Clubs
cultural_clubs = clubs_info.get("categories", {}).get("cultural_and_language_clubs", [])
cultural_club_lines = (
    "\n  - "
    + "\n  - ".join(
        [
            f"{club['name']}: {club.get('description', 'No description')}"
            for club in cultural_clubs
        ]
    )
    if cultural_clubs
    else "No cultural clubs listed."
)

# Create the info summary
info_summary = (
    f"{college_name} is located at {address} in {city}, {state}. It is affiliated with {affiliation} and approved by {approval}."
    f"\nEstablished in: {established_year}\n\n"
    f"Undergraduate programs offered:\n- "
    + "\n- ".join(ug_programs)
    + "\n\nPostgraduate programs offered:\n- "
    + "\n- ".join(pg_programs)
    + f"\n\nAdmission criteria:\n"
    f"  - UG: {ug_criteria}\n"
    f"  - PG/MBA: {pg_criteria}\n\n"
    f"Fee structure:\n"
    f"  - B.E./B.Tech: {be_fee}\n"
    f"  - M.E.: {me_fee}\n"
    f"  - MBA: {mba_fee}\n\n"
    f"Admission portal: {admission_portal} - {admission_portal_url}\n\n"
    f"Website: {website}\n"
    f"Contact Information:\n"
    f"  - Phone Numbers: {phone_numbers}\n\n"
    f"Placement Info:\n"
    f"  - {placement_title}\n"
    f"  - Assistance: {placement_assistance}\n"
    f"  - Vision: {placement_vision}\n"
    f"  - Objectives: \n - {placement_objectives}\n\n"
    f"  - Focus Areas of Placement Cell:\n - Soft Skills Development\n    - Personality Development\n    - Group Discussions\n    - Domain Knowledge\n    - Aptitude and Quantitative Skills\n\n"
    f"  - Mentorship:\n - Senior faculty guide students for career and higher studies.\n"
    f"  - Entrepreneurship Support:\n - Collaboration with Entrepreneurship Development Cell (EDC)\n"
    f"  - Activities:\n  - Inviting entrepreneurs to share experiences\n"
    f"  - Providing guidance on entrepreneurship\n"
    f"  - Encouraging innovative thinking\n\n"
    f"  - Training Programs:\n - " + "\n  - ".join(training_programs) + "\n\n"
    f"  - Competitive Exam Training:\n    - "
    + "\n    - ".join(competitive_exam_training)
    + "\n\n"
    f"  - Industry Collaborations:\n    - " + "\n    - ".join(industry_partners) + "\n"
    f"Major events conducted by the college:\n{event_lines}"
    f"\n\nClubs and Activities:\nOverview: {clubs_overview}\n\n"
    f"Technical Clubs:{technical_club_lines}\n\n"
    f"Departmental Associations:{dept_assoc_lines}\n\n"
    f"Cultural and Language Clubs:{cultural_club_lines}"
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama3-8b-8192"


class Message(BaseModel):
    message: str


@app.post("/chat")
async def chat(msg: Message):
    print(msg)
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    body = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are Milo, a helpful assistant for SRM Madurai College of Engineering and Technology. "
                    "Be friendly to the users."
                    "Use the following college details to answer accurately:\n\n"
                    + info_summary
                ),
            },
            {"role": "user", "content": msg.message},
        ],
    }
    print(msg.message)
    print(headers)
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions", 
        headers=headers, 
        json=body
    )
    print(response)
    print(response.json())
    print(response.text)
    if response.ok:
        print(response.json())
        return {"response": response.json()["choices"][0]["message"]["content"]}
    else:
        return {"error": "Groq API error", "details": response.text}
=======
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import json

with open("college_info.json", "r") as f:
    college_data = json.load(f)

# Extract undergraduate and postgraduate programs with safe .get() methods
college_name = college_data["srm_mcet"]["college_name"]
established_year = college_data["srm_mcet"]["established_year"]
affiliation = college_data["srm_mcet"]["affiliation"]
approval = college_data["srm_mcet"]["approval"]
location = college_data["srm_mcet"]["location"]
city = location["city"]
state = location["state"]
address = location["address"]

# Programs offered
ug_programs = college_data["srm_mcet"]["programs_offered"]["undergraduate"]
pg_programs = college_data["srm_mcet"]["programs_offered"]["postgraduate"]

# Fees structure
fees_structure = college_data["srm_mcet"]["fees_structure"]
be_fee = fees_structure["B.E./B.Tech"]
me_fee = fees_structure["M.E."]
mba_fee = fees_structure["MBA"]

# Admission criteria
ug_criteria = college_data["srm_mcet"]["admission_criteria"]["undergraduate"]
pg_criteria = college_data["srm_mcet"]["admission_criteria"]["postgraduate"]

# Events
events = college_data["srm_mcet"]["events"]
event_lines = (
    "\n".join(
        [
            f"- {event['title']} on {event['date']}: {event['description']}"
            for event in events
        ]
    )
    if events
    else "No events listed."
)

# ERP portal info
erp_portal = college_data["srm_mcet"]["erp_portal"]
admission_portal = erp_portal["portal_name"]
admission_portal_url = erp_portal["url"]

# Contact info
contact_info = college_data["srm_mcet"]["contact"]
website = contact_info["website"]
phone_numbers = ", ".join(contact_info["phone_numbers"])

# Placement details
placement_info = college_data["srm_mcet"]["placement"]
placement_title = placement_info["title"]
placement_assistance = placement_info["assistance"]
placement_vision = placement_info["vision"]
placement_objectives = "\n  - ".join(placement_info["objectives"])
training_programs = [
    "Communicative English Training Program",
    "Basic Grammar Training",
    "Career Awareness Program",
    "Coding Training",
    "Aptitude Test Training",
    "Group Discussion Practice",
    "Personal Interview Practice",
    "Placement Training Program",
    "Mock Recruitment Program",
    "Employability Training Camp",
]
competitive_exam_training = [
    "BEC",
    "GATE",
    "TOEFL",
    "IELTS",
    "T.I.M.E",
    "Networking",
    "Coding",
    "CAT Coaching",
    "MAT Coaching",
    "XAT Coaching",
    "CMAT Coaching",
    "ICET Coaching",
    "IIT Foundation",
]
industry_partners = ["L&T", "Infosys", "Vodafone", "Anna University Incubation Centre"]

# Clubs and Activities
clubs_info = college_data["srm_mcet"].get("clubs_and_activities", {})
clubs_overview = clubs_info.get("overview", "No overview available.")

# Technical Clubs
technical_clubs = clubs_info.get("categories", {}).get("technical_clubs", [])
technical_club_lines = (
    "\n  - "
    + "\n  - ".join(
        [
            f"{club['name']}: {club.get('description', 'No description')}"
            for club in technical_clubs
        ]
    )
    if technical_clubs
    else "No technical clubs listed."
)

# Departmental Associations
dept_assocs = clubs_info.get("categories", {}).get("departmental_associations", [])
dept_assoc_lines = (
    "\n  - "
    + "\n  - ".join(
        [f"{assoc['name']} ({assoc['department']})" for assoc in dept_assocs]
    )
    if dept_assocs
    else "No departmental associations listed."
)

# Cultural and Language Clubs
cultural_clubs = clubs_info.get("categories", {}).get("cultural_and_language_clubs", [])
cultural_club_lines = (
    "\n  - "
    + "\n  - ".join(
        [
            f"{club['name']}: {club.get('description', 'No description')}"
            for club in cultural_clubs
        ]
    )
    if cultural_clubs
    else "No cultural clubs listed."
)

# Create the info summary
info_summary = (
    f"{college_name} is located at {address} in {city}, {state}. It is affiliated with {affiliation} and approved by {approval}."
    f"\nEstablished in: {established_year}\n\n"
    f"Undergraduate programs offered:\n- "
    + "\n- ".join(ug_programs)
    + "\n\nPostgraduate programs offered:\n- "
    + "\n- ".join(pg_programs)
    + f"\n\nAdmission criteria:\n"
    f"  - UG: {ug_criteria}\n"
    f"  - PG/MBA: {pg_criteria}\n\n"
    f"Fee structure:\n"
    f"  - B.E./B.Tech: {be_fee}\n"
    f"  - M.E.: {me_fee}\n"
    f"  - MBA: {mba_fee}\n\n"
    f"Admission portal: {admission_portal} - {admission_portal_url}\n\n"
    f"Website: {website}\n"
    f"Contact Information:\n"
    f"  - Phone Numbers: {phone_numbers}\n\n"
    f"Placement Info:\n"
    f"  - {placement_title}\n"
    f"  - Assistance: {placement_assistance}\n"
    f"  - Vision: {placement_vision}\n"
    f"  - Objectives: \n - {placement_objectives}\n\n"
    f"  - Focus Areas of Placement Cell:\n - Soft Skills Development\n    - Personality Development\n    - Group Discussions\n    - Domain Knowledge\n    - Aptitude and Quantitative Skills\n\n"
    f"  - Mentorship:\n - Senior faculty guide students for career and higher studies.\n"
    f"  - Entrepreneurship Support:\n - Collaboration with Entrepreneurship Development Cell (EDC)\n"
    f"  - Activities:\n  - Inviting entrepreneurs to share experiences\n"
    f"  - Providing guidance on entrepreneurship\n"
    f"  - Encouraging innovative thinking\n\n"
    f"  - Training Programs:\n - " + "\n  - ".join(training_programs) + "\n\n"
    f"  - Competitive Exam Training:\n    - "
    + "\n    - ".join(competitive_exam_training)
    + "\n\n"
    f"  - Industry Collaborations:\n    - " + "\n    - ".join(industry_partners) + "\n"
    f"Major events conducted by the college:\n{event_lines}"
    f"\n\nClubs and Activities:\nOverview: {clubs_overview}\n\n"
    f"Technical Clubs:{technical_club_lines}\n\n"
    f"Departmental Associations:{dept_assoc_lines}\n\n"
    f"Cultural and Language Clubs:{cultural_club_lines}"
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama3-8b-8192"


class Message(BaseModel):
    message: str


@app.post("/chat")
async def chat(msg: Message):
    print(msg)
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    body = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are Milo, a helpful assistant for SRM Madurai College of Engineering and Technology. "
                    "Be friendly to the users."
                    "Use the following college details to answer accurately:\n\n"
                    + info_summary
                ),
            },
            {"role": "user", "content": msg.message},
        ],
    }
    print(msg.message)
    print(headers)
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions", 
        headers=headers, 
        json=body
    )
    print(response)
    print(response.json())
    print(response.text)
    if response.ok:
        print(response.json())
        return {"response": response.json()["choices"][0]["message"]["content"]}
    else:
        return {"error": "Groq API error", "details": response.text}
>>>>>>> 4985b0bb7a4a1a675de905d04e0295798d005b9a
