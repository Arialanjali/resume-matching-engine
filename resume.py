import math

student_data = {
    "Arjun Sharma": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning",
    "Priya Nair": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS",
    "Rahul Gupta": "Java, Spring Boot, MySql, Microservices, Docker, kubernates",
    "Sneha Patel": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib",
    "Vikram Singh": "C++, Algoritms, Data Structure, competitive programming, python",
    "Ananya Krishnan": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD",
    "Karan Mehta": "Python, Sklearn, XGboost, feature engineering, SQL, tableau",
    "Deepika Rao": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma",
    "Aditya Kumar": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest",
    "Meera Iyer": "python, R, statistics, ML, regression, clustering, Power-BI"
}

job_roles = {
    "JD-1 — Kakao (ML Engineer)": "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization, NLP, BERT, Feature Engineering, Statistics",

    "JD-2 — Naver (Backend Engineer)": "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes, REST API, CI/CD, Redis",

    "JD-3 — Line (Frontend Engineer)": "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS, Node.js, GraphQL, Redux, Jest, AWS"
}

alias_map = {
    "python": "python",
    "pyhton": "python",
    "java": "java",
    "javascript": "javascript",
    "javascrpit": "javascript",
    "typescript": "typescript",
    "typescrpit": "typescript",
    "c++": "cpp",
    "machinelearning": "machine_learning",
    "machine learning": "machine_learning",
    "ml": "machine_learning",
    "sklearn": "machine_learning",
    "deeplearning": "deep_learning",
    "deep learning": "deep_learning",
    "deep-learning": "deep_learning",
    "tensorflow": "tensorflow",
    "pytorch": "pytorch",
    "keras": "keras",
    "nlp": "nlp",
    "bert": "bert",
    "xgboost": "xgboost",
    "feature engineering": "feature_engineering",
    "statistics": "statistics",
    "regression": "regression",
    "clustering": "clustering",
    "data-viz": "data_visualization",
    "matplotlib": "data_visualization",
    "tableau": "data_visualization",
    "power-bi": "data_visualization",
    "pandas": "pandas",
    "numpy": "numpy",
    "react": "react",
    "reacts": "react",
    "reactjs": "react",
    "vue": "vue",
    "vue.js": "vue",
    "redux": "redux",
    "tailwind": "tailwind",
    "html/css": "html_css",
    "jest": "jest",
    "graphql": "graphql",
    "node.js": "nodejs",
    "nodejs": "nodejs",
    "flask": "flask",
    "spring boot": "spring_boot",
    "rest api": "rest_api",
    "rest": "rest_api",
    "microservices": "microservices",
    "sql": "sql",
    "mysql": "mysql",
    "postgresql": "postgresql",
    "mongodb": "mongodb",
    "redis": "redis",
    "docker": "docker",
    "kubernetes": "kubernetes",
    "kubernates": "kubernetes",
    "ci/cd": "ci_cd",
    "aws": "aws",
    "android": "android",
    "firebase": "firebase",
    "algorithms": "algorithms",
    "algoritms": "algorithms",
    "data structure": "data_structures",
    "competitive programming": "competitive_programming",
    "ui/ux": "ui_ux",
    "figma": "figma",
    "r": "r",
    "kotlin": "kotlin"
}

def clean_skills(text):

    parts = text.lower().split(",")

    result = set()

    for item in parts:

        item = item.strip()

        if item in alias_map:
            result.add(alias_map[item])

    return list(result)

processed_resumes = {}

for person in student_data:

    processed_resumes[person] = clean_skills(student_data[person])

all_skills = set()

for item in processed_resumes.values():

    for skill in item:

        all_skills.add(skill)

all_skills = sorted(all_skills)

document_frequency = {}

for skill in all_skills:

    total = 0

    for item in processed_resumes.values():

        if skill in item:
            total += 1

    document_frequency[skill] = total

idf_scores = {}

for skill in all_skills:

    idf_scores[skill] = math.log(10 / document_frequency[skill])

resume_vectors = {}

for person, skills in processed_resumes.items():

    values = []

    total_skills = len(skills)

    for word in all_skills:

        if word in skills:

            values.append((1 / total_skills) * idf_scores[word])

        else:

            values.append(0)

    resume_vectors[person] = values

processed_jobs = {}

for role in job_roles:

    processed_jobs[role] = clean_skills(job_roles[role])

job_vectors = {}

for role, skills in processed_jobs.items():

    temp = []

    for word in all_skills:

        if word in skills:
            temp.append(1)
        else:
            temp.append(0)

    job_vectors[role] = temp

def similarity_score(x, y):

    numerator = 0
    first = 0
    second = 0

    for i in range(len(x)):

        numerator += x[i] * y[i]

        first += x[i] * x[i]

        second += y[i] * y[i]

    first = math.sqrt(first)
    second = math.sqrt(second)

    if first == 0 or second == 0:
        return 0

    return numerator / (first * second)

for role in job_vectors:

    result = []

    for person in resume_vectors:

        value = similarity_score(
            resume_vectors[person],
            job_vectors[role]
        )

        result.append((person, round(value, 2)))

    result.sort(key=lambda x: (-x[1], x[0]))

    print()
    print(role)

    for name, score in result[:3]:

        print(name, "(", score, ")", sep="")
