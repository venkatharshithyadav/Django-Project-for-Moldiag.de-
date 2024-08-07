# Django-Project-for-Moldiag.de-

POM Project 

Project Overview

The POM Project aims to develop a user interface for searching, selecting, and grouping ontology terms, particularly focusing on Human Phenotype Ontology (HPO) entries. The project utilizes various resources including ontology databases, scientific literature sources, and AI tools like ChatGPT. The ultimate goal is to streamline molecular genetic diagnostics to clinical needs by making precise predictions and recommendations.

Key Features

- **HPO Group Input Module**: Allows users to select and group HPO entries for patients based on their symptoms.
- **Ontology Search and Selection**: Users can search for HPO terms or select them from a hierarchical structure.
- **Recommendations**: Provides gene test recommendations and diagnoses according to ICD10 or ICD11 codes.
- **User Interface**: An intuitive interface to facilitate the selection and grouping of ontology terms.

Project Structure

plaintext
POM_Project/
│
├── POM_Project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── ontology/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── templates/
│   │   └── ontology/
│   │       ├── index.html
│   ├── static/
│       ├── ontology/
│           ├── css/
│               ├── styles.css
│           ├── js/
│               ├── scripts.js
│
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
 
