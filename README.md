# AI Resume Matching System

This project is a Python-based Resume Matching System developed for the Redrob AI Campus Hackathon.

The system compares candidate resumes with job descriptions by applying:
- Skill normalization
- TF-IDF computation
- Binary vector generation
- Cosine similarity scoring

The application ranks the most suitable candidates for each job role based on skill relevance.

## Key Functionalities
- Cleans noisy and inconsistent skill data
- Removes duplicate skills
- Builds a shared vocabulary from resumes
- Computes TF-IDF vectors manually
- Creates Job Description vectors
- Calculates similarity scores
- Displays Top 3 matching candidates

## Tech Stack
- Python
- math module

## Restrictions Followed
- No external libraries used
- No NumPy
- No Pandas
- No Scikit-learn

## Output
The program generates ranked candidate recommendations for:
- ML Engineer
- Backend Engineer
- Frontend Engineer
