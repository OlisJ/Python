from fastapi import FastAPI
from models import Deveoper,Project

app=FastAPI()

@app.post("/developers/")
def create_developer(developer:Deveoper):
    return{"message":"Developer created succesfully", "developer":developer}

@app.post("/projects/")
def create_projects(projects:Project):
    return{"message":"Project created succesfully","project":projects}

@app.get("/projects/")
def get_projects():
    sample_projects=Project(
        title="Sample Project",
        description="This is a desc",
        languages=["Python","Javascript"],
        lead_developer=Developer(name="Jane Doe",experience=5)
    )
    return{"projects":[sample_projects]}