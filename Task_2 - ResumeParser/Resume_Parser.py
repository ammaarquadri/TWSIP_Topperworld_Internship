import pandas as pd
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def extract_name(doc):
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            return ent.text
    return None

def extract_email(doc):
    for token in doc:
        if token.like_email:
            return token.text
    return None

def extract_phone(doc):
    for token in doc:
        if token.like_num and len(token.text) >= 10:  # Adjust length according to your needs
            return token.text
    return None

def extract_experience(doc):
    experience = []
    for ent in doc.ents:
        if ent.label_ == 'ORG':
            experience.append(ent.text)
    return experience

def extract_skills(doc):
    skills = []
    for token in doc:
        if token.pos_ == 'NOUN':
            skills.append(token.text)
    return skills

def extract_languages(doc):
    languages = []
    # Simple list of common programming languages for example purposes
    common_languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "SQL", "HTML", "CSS"]
    for token in doc:
        if token.text in common_languages:
            languages.append(token.text)
    return languages

def parse_resume(text):
    if pd.isna(text):
        text = ""
    doc = nlp(text)
    resume_data = {
        'Name': extract_name(doc),
        'Email': extract_email(doc),
        'Company': extract_experience(doc),
        'Skill': extract_skills(doc),
        'Language': extract_languages(doc),
    }
    return resume_data

# Load dataset
df = pd.read_csv('data_set.csv')

# Check the columns in the dataset
print(df.columns)

# Use the correct column name for resumes
resume_column = 'Resume'

# Check if the column exists in the dataset
if resume_column not in df.columns:
    raise ValueError(f"Column '{resume_column}' not found in the dataset.")

# Parse resumes with debug printing for the first few entries
parsed_resumes = []
for idx, text in enumerate(df[resume_column]):
    parsed_data = parse_resume(text)
    parsed_resumes.append(parsed_data)
    if idx < 10:  # Print only the first 10 resumes for debugging
        print(f"Parsed resume {idx + 1}: {parsed_data}")

# Create a new DataFrame from the parsed resume data
parsed_df = pd.DataFrame(parsed_resumes)

# Add Start Date and End Date columns if necessary
parsed_df['Start Date'] = None
parsed_df['End Date'] = None

# Save parsed resumes to a new CSV file in chunks
parsed_df.to_csv('parsed_resumes.csv', index=False)

print("Resume parsing completed. Parsed resumes saved to 'parsed_resumes.csv'.")
