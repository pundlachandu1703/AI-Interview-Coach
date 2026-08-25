import re
import random


# =========================================================
# INTERVIEW QUESTION DATABASE
# =========================================================

INTERVIEW_DATA = {

    # =====================================================
    # AI / ML ENGINEER
    # =====================================================

    "AI/ML Engineer": [

        {
            "question": "What is Artificial Intelligence?",
            "keywords": [
                "artificial intelligence",
                "machine",
                "human intelligence",
                "decision",
                "problem solving"
            ],
            "ideal": """
Artificial Intelligence is a branch of computer science that focuses
on creating systems capable of performing tasks that normally require
human intelligence. These tasks include learning, reasoning,
problem solving, understanding language, perception and decision making.
Examples include virtual assistants, recommendation systems,
autonomous vehicles and AI chatbots.
"""
        },

        {
            "question": "What is Machine Learning?",
            "keywords": [
                "machine learning",
                "data",
                "algorithm",
                "model",
                "training",
                "prediction"
            ],
            "ideal": """
Machine Learning is a subset of Artificial Intelligence that allows
computers to learn patterns from data and make predictions or decisions
without being explicitly programmed for every situation. A machine
learning model is trained using data and then evaluated on unseen data.
"""
        },

        {
            "question": "What is the difference between supervised and unsupervised learning?",
            "keywords": [
                "supervised",
                "unsupervised",
                "labeled",
                "unlabeled",
                "classification",
                "clustering"
            ],
            "ideal": """
Supervised learning uses labeled data where the expected output is
already known. Classification and regression are common supervised
learning tasks. Unsupervised learning works with unlabeled data and
tries to discover hidden patterns or structures. Clustering is a common
example of unsupervised learning.
"""
        },

        {
            "question": "What is reinforcement learning?",
            "keywords": [
                "reinforcement",
                "agent",
                "environment",
                "reward",
                "action",
                "policy"
            ],
            "ideal": """
Reinforcement Learning is a type of machine learning where an agent
learns by interacting with an environment. The agent takes actions and
receives rewards or penalties. Over time it learns a policy that
maximizes the total expected reward.
"""
        },

        {
            "question": "What is overfitting?",
            "keywords": [
                "overfitting",
                "training",
                "unseen",
                "generalization",
                "model",
                "noise"
            ],
            "ideal": """
Overfitting happens when a model learns the training data too closely,
including noise, and therefore performs poorly on unseen data.
Techniques such as regularization, cross-validation, dropout,
data augmentation and using a simpler model can help reduce overfitting.
"""
        },

        {
            "question": "What is underfitting?",
            "keywords": [
                "underfitting",
                "simple",
                "training",
                "model",
                "patterns"
            ],
            "ideal": """
Underfitting occurs when a machine learning model is too simple to
capture important patterns in the training data. It usually results in
poor performance on both training and testing data. Increasing model
complexity, improving features or training longer can help.
"""
        },

        {
            "question": "What is the difference between classification and regression?",
            "keywords": [
                "classification",
                "regression",
                "categorical",
                "continuous",
                "prediction"
            ],
            "ideal": """
Classification predicts discrete categories or classes, while
regression predicts continuous numerical values. For example,
spam detection is classification and predicting house prices is
regression.
"""
        },

        {
            "question": "What is a confusion matrix?",
            "keywords": [
                "confusion matrix",
                "true positive",
                "true negative",
                "false positive",
                "false negative",
                "classification"
            ],
            "ideal": """
A confusion matrix is used to evaluate classification models.
It contains true positives, true negatives, false positives and
false negatives. These values can be used to calculate accuracy,
precision, recall and F1-score.
"""
        },

        {
            "question": "What is precision and recall?",
            "keywords": [
                "precision",
                "recall",
                "true positive",
                "false positive",
                "false negative"
            ],
            "ideal": """
Precision measures how many of the predicted positive cases are
actually positive. Recall measures how many of the actual positive
cases were correctly identified. Precision is important when false
positives are costly, while recall is important when missing positive
cases is costly.
"""
        },

        {
            "question": "What is feature engineering?",
            "keywords": [
                "feature engineering",
                "features",
                "data",
                "transformation",
                "model",
                "performance"
            ],
            "ideal": """
Feature engineering is the process of creating, transforming or
selecting useful input features from raw data. Good features can help
machine learning models identify patterns more effectively and improve
model performance.
"""
        },

        {
            "question": "What is cross-validation?",
            "keywords": [
                "cross validation",
                "training",
                "validation",
                "testing",
                "model"
            ],
            "ideal": """
Cross-validation is a technique used to evaluate machine learning
models. The dataset is divided into multiple parts and the model is
trained and tested using different combinations of those parts.
It provides a more reliable estimate of model performance.
"""
        },

        {
            "question": "What is deep learning?",
            "keywords": [
                "deep learning",
                "neural network",
                "layers",
                "data",
                "representation"
            ],
            "ideal": """
Deep Learning is a subset of machine learning that uses neural
networks with multiple layers to automatically learn complex
representations from data. It is widely used in computer vision,
natural language processing and speech recognition.
"""
        },

        {
            "question": "What is NLP?",
            "keywords": [
                "nlp",
                "natural language processing",
                "language",
                "text",
                "human",
                "computer"
            ],
            "ideal": """
Natural Language Processing is a field of AI that enables computers
to understand, process and generate human language. Applications
include chatbots, sentiment analysis, machine translation,
text summarization and question answering.
"""
        },

        {
            "question": "What is computer vision?",
            "keywords": [
                "computer vision",
                "image",
                "video",
                "object",
                "recognition",
                "computer"
            ],
            "ideal": """
Computer Vision is a field of AI that enables computers to understand
and interpret images and videos. Common applications include object
detection, facial recognition, image classification, medical imaging
and autonomous vehicles.
"""
        },

        {
            "question": "How would you deploy a machine learning model?",
            "keywords": [
                "model",
                "deployment",
                "api",
                "flask",
                "docker",
                "cloud"
            ],
            "ideal": """
A machine learning model can be deployed by saving the trained model,
creating an API using frameworks such as Flask or FastAPI, packaging
the application using Docker and deploying it to a cloud platform.
Monitoring should also be implemented to track model performance.
"""
        }
    ],


    # =====================================================
    # DATA SCIENTIST
    # =====================================================

    "Data Scientist": [

        {
            "question": "What is the role of a Data Scientist?",
            "keywords": [
                "data",
                "analysis",
                "statistics",
                "machine learning",
                "insights",
                "business"
            ],
            "ideal": """
A Data Scientist collects, cleans and analyzes data to identify useful
patterns and insights. They use statistics, data visualization and
machine learning to solve business problems and communicate results
to stakeholders.
"""
        },

        {
            "question": "What is data preprocessing?",
            "keywords": [
                "data",
                "cleaning",
                "missing",
                "encoding",
                "scaling",
                "preprocessing"
            ],
            "ideal": """
Data preprocessing prepares raw data for analysis or machine learning.
It can include handling missing values, removing duplicates, encoding
categorical variables, scaling numerical features and handling
outliers.
"""
        },

        {
            "question": "What is exploratory data analysis?",
            "keywords": [
                "exploratory",
                "data analysis",
                "visualization",
                "patterns",
                "statistics",
                "outliers"
            ],
            "ideal": """
Exploratory Data Analysis, or EDA, is the process of examining a
dataset using statistics and visualizations to understand distributions,
relationships, missing values, outliers and important patterns before
building a model.
"""
        },

        {
            "question": "What is the difference between mean, median and mode?",
            "keywords": [
                "mean",
                "median",
                "mode",
                "average",
                "middle",
                "frequency"
            ],
            "ideal": """
Mean is the arithmetic average of values. Median is the middle value
after sorting the data. Mode is the value that occurs most frequently.
Median is often preferred when the data contains extreme outliers.
"""
        },

        {
            "question": "What is standard deviation?",
            "keywords": [
                "standard deviation",
                "spread",
                "mean",
                "data",
                "variation"
            ],
            "ideal": """
Standard deviation measures how much the values in a dataset vary
around the mean. A low standard deviation indicates that values are
close to the mean, while a high standard deviation indicates greater
variation.
"""
        },

        {
            "question": "What is correlation?",
            "keywords": [
                "correlation",
                "relationship",
                "variables",
                "positive",
                "negative"
            ],
            "ideal": """
Correlation measures the strength and direction of the relationship
between two variables. Positive correlation means both variables tend
to increase together, while negative correlation means one tends to
increase as the other decreases.
"""
        },

        {
            "question": "What is hypothesis testing?",
            "keywords": [
                "hypothesis",
                "null",
                "alternative",
                "p value",
                "statistical"
            ],
            "ideal": """
Hypothesis testing is a statistical method used to determine whether
there is enough evidence to support a claim about a population.
It generally involves a null hypothesis, alternative hypothesis,
test statistic and p-value.
"""
        },

        {
            "question": "What is a p-value?",
            "keywords": [
                "p value",
                "hypothesis",
                "null",
                "probability",
                "significance"
            ],
            "ideal": """
A p-value indicates how compatible the observed data is with the
null hypothesis. A small p-value provides stronger evidence against
the null hypothesis. The significance threshold is commonly set to
0.05, although the appropriate threshold depends on the context.
"""
        },

        {
            "question": "What is feature selection?",
            "keywords": [
                "feature selection",
                "features",
                "model",
                "irrelevant",
                "performance"
            ],
            "ideal": """
Feature selection is the process of selecting the most useful input
features for a machine learning model. Removing irrelevant features
can reduce complexity, improve performance and help prevent overfitting.
"""
        },

        {
            "question": "What is a data visualization?",
            "keywords": [
                "data visualization",
                "chart",
                "graph",
                "data",
                "patterns"
            ],
            "ideal": """
Data visualization represents data using charts and graphs so that
patterns, trends and relationships can be understood easily.
Common visualizations include bar charts, line charts, scatter plots
and histograms.
"""
        },

        {
            "question": "What is the difference between supervised and unsupervised learning?",
            "keywords": [
                "supervised",
                "unsupervised",
                "labeled",
                "unlabeled",
                "classification",
                "clustering"
            ],
            "ideal": """
Supervised learning uses labeled data and learns to predict known
outputs. Unsupervised learning works with unlabeled data and discovers
patterns or groups. Classification is supervised, while clustering is
unsupervised.
"""
        },

        {
            "question": "What is regression?",
            "keywords": [
                "regression",
                "continuous",
                "prediction",
                "dependent",
                "independent"
            ],
            "ideal": """
Regression is a supervised learning technique used to predict
continuous numerical values. Linear regression is a common example
where a relationship between independent and dependent variables is
modeled.
"""
        },

        {
            "question": "How do you handle missing values?",
            "keywords": [
                "missing",
                "values",
                "remove",
                "mean",
                "median",
                "imputation"
            ],
            "ideal": """
Missing values can be handled by removing rows or columns when
appropriate, or by imputing values using techniques such as mean,
median, mode or more advanced methods. The correct approach depends
on why the data is missing and how much data is affected.
"""
        },

        {
            "question": "How do you handle outliers?",
            "keywords": [
                "outliers",
                "data",
                "iqr",
                "z score",
                "remove",
                "transform"
            ],
            "ideal": """
Outliers can be detected using methods such as IQR or z-score.
Depending on the context, they can be removed, transformed, capped
or retained if they represent genuine observations.
"""
        },

        {
            "question": "How do you explain a machine learning model to a non-technical person?",
            "keywords": [
                "model",
                "simple",
                "business",
                "visualization",
                "explain"
            ],
            "ideal": """
I would explain the model using simple language and business examples
instead of technical terminology. I would focus on what the model
predicts, why it is useful, how accurate it is and what factors
influence its predictions.
"""
        }
    ],


    # =====================================================
    # FULL STACK DEVELOPER
    # =====================================================

    "Full Stack Developer": [

        {
            "question": "What is the difference between frontend and backend development?",
            "keywords": [
                "frontend",
                "backend",
                "client",
                "server",
                "database",
                "interface"
            ],
            "ideal": """
Frontend development focuses on the user interface and client-side
functionality using technologies such as HTML, CSS and JavaScript.
Backend development handles server-side logic, APIs, authentication
and database operations.
"""
        },

        {
            "question": "What is HTML?",
            "keywords": [
                "html",
                "markup",
                "structure",
                "web",
                "page"
            ],
            "ideal": """
HTML stands for HyperText Markup Language. It is used to define the
structure and content of web pages using elements such as headings,
paragraphs, links, images and forms.
"""
        },

        {
            "question": "What is CSS?",
            "keywords": [
                "css",
                "style",
                "design",
                "layout",
                "web"
            ],
            "ideal": """
CSS stands for Cascading Style Sheets. It controls the visual
appearance of web pages, including colors, fonts, spacing, layouts,
animations and responsive design.
"""
        },

        {
            "question": "What is JavaScript?",
            "keywords": [
                "javascript",
                "programming",
                "web",
                "interactive",
                "browser"
            ],
            "ideal": """
JavaScript is a programming language commonly used to add
interactivity and dynamic behavior to web applications. It can run
in browsers and also on servers using environments such as Node.js.
"""
        },

        {
            "question": "What is React?",
            "keywords": [
                "react",
                "javascript",
                "component",
                "ui",
                "frontend",
                "virtual dom"
            ],
            "ideal": """
React is a JavaScript library for building user interfaces.
It uses reusable components and a virtual DOM to efficiently update
the interface when application data changes.
"""
        },

        {
            "question": "What is Node.js?",
            "keywords": [
                "node",
                "javascript",
                "server",
                "runtime",
                "backend"
            ],
            "ideal": """
Node.js is a JavaScript runtime built on Chrome's V8 engine.
It allows developers to execute JavaScript outside the browser and
is commonly used for backend services and APIs.
"""
        },

        {
            "question": "What is Express.js?",
            "keywords": [
                "express",
                "node",
                "server",
                "api",
                "middleware",
                "javascript"
            ],
            "ideal": """
Express.js is a lightweight web framework for Node.js. It simplifies
building web servers and REST APIs and provides features such as
routing and middleware.
"""
        },

        {
            "question": "What is a REST API?",
            "keywords": [
                "rest",
                "api",
                "http",
                "request",
                "response",
                "get",
                "post"
            ],
            "ideal": """
A REST API allows applications to communicate using HTTP. It commonly
uses methods such as GET, POST, PUT and DELETE to work with resources.
The server returns responses, often using JSON.
"""
        },

        {
            "question": "What is the difference between SQL and NoSQL?",
            "keywords": [
                "sql",
                "nosql",
                "database",
                "relational",
                "document",
                "tables"
            ],
            "ideal": """
SQL databases are relational and generally store structured data in
tables with predefined schemas. NoSQL databases use more flexible
structures such as documents, key-value pairs or graphs.
"""
        },

        {
            "question": "What is authentication?",
            "keywords": [
                "authentication",
                "login",
                "password",
                "identity",
                "user"
            ],
            "ideal": """
Authentication is the process of verifying the identity of a user.
A common example is a login system where the user provides credentials
such as an email and password.
"""
        },

        {
            "question": "What is authorization?",
            "keywords": [
                "authorization",
                "permission",
                "access",
                "role",
                "user"
            ],
            "ideal": """
Authorization determines what an authenticated user is allowed to
access or perform. For example, an administrator may have permission
to delete users while a normal user may not.
"""
        },

        {
            "question": "What is Git?",
            "keywords": [
                "git",
                "version control",
                "repository",
                "commit",
                "code"
            ],
            "ideal": """
Git is a distributed version control system used to track changes
in source code. Developers use commits, branches and merges to
manage development and collaborate with other developers.
"""
        },

        {
            "question": "What is responsive web design?",
            "keywords": [
                "responsive",
                "mobile",
                "desktop",
                "screen",
                "css"
            ],
            "ideal": """
Responsive web design makes websites adapt to different screen sizes
such as mobile phones, tablets and desktops. CSS media queries,
flexible layouts and responsive units are commonly used.
"""
        },

        {
            "question": "What is middleware?",
            "keywords": [
                "middleware",
                "request",
                "response",
                "server",
                "function"
            ],
            "ideal": """
Middleware is software that runs between the incoming request and
the final response. It can perform tasks such as authentication,
logging, validation and error handling.
"""
        },

        {
            "question": "How would you deploy a full stack application?",
            "keywords": [
                "deployment",
                "frontend",
                "backend",
                "database",
                "server",
                "cloud"
            ],
            "ideal": """
I would build and test the frontend and backend separately, configure
the database, store sensitive configuration in environment variables,
deploy the frontend and backend to suitable hosting platforms and
connect them through secure APIs. I would also configure monitoring
and error handling.
"""
        }
    ],


    # =====================================================
    # PYTHON DEVELOPER
    # =====================================================

    "Python Developer": [

        {
            "question": "What are the main features of Python?",
            "keywords": [
                "python",
                "interpreted",
                "object oriented",
                "dynamic",
                "readable",
                "libraries"
            ],
            "ideal": """
Python is a high-level, interpreted and dynamically typed programming
language. It has readable syntax, supports multiple programming
paradigms and provides a large ecosystem of libraries and frameworks.
"""
        },

        {
            "question": "What is the difference between a list and a tuple?",
            "keywords": [
                "list",
                "tuple",
                "mutable",
                "immutable",
                "python"
            ],
            "ideal": """
A list is mutable, meaning its elements can be modified after creation.
A tuple is immutable, so its elements cannot be changed after creation.
Lists are useful for changing collections while tuples are useful for
fixed collections.
"""
        },

        {
            "question": "What is a Python dictionary?",
            "keywords": [
                "dictionary",
                "key",
                "value",
                "mapping",
                "python"
            ],
            "ideal": """
A dictionary is a Python data structure that stores information as
key-value pairs. Keys are used to access their corresponding values.
Dictionaries are useful when data needs to be associated with unique
identifiers.
"""
        },

        {
            "question": "What is exception handling in Python?",
            "keywords": [
                "exception",
                "try",
                "except",
                "error",
                "finally"
            ],
            "ideal": """
Exception handling allows programs to manage runtime errors without
crashing unexpectedly. Python uses try, except, else and finally
blocks to handle exceptions.
"""
        },

        {
            "question": "What is a function in Python?",
            "keywords": [
                "function",
                "def",
                "parameter",
                "return",
                "code"
            ],
            "ideal": """
A function is a reusable block of code designed to perform a specific
task. Python functions are defined using the def keyword and can accept
parameters and return values.
"""
        },

        {
            "question": "What is object-oriented programming?",
            "keywords": [
                "object oriented",
                "class",
                "object",
                "inheritance",
                "encapsulation"
            ],
            "ideal": """
Object-oriented programming organizes software around objects and
classes. Important concepts include encapsulation, inheritance,
polymorphism and abstraction. Python supports object-oriented
programming.
"""
        },

        {
            "question": "What is inheritance in Python?",
            "keywords": [
                "inheritance",
                "class",
                "parent",
                "child",
                "method"
            ],
            "ideal": """
Inheritance allows a child class to reuse properties and methods of
a parent class. It promotes code reuse and allows specialized classes
to extend existing functionality.
"""
        },

        {
            "question": "What is polymorphism?",
            "keywords": [
                "polymorphism",
                "object",
                "method",
                "class",
                "different"
            ],
            "ideal": """
Polymorphism means that the same interface or method name can behave
differently depending on the object using it. It allows flexible and
reusable code.
"""
        },

        {
            "question": "What is a lambda function?",
            "keywords": [
                "lambda",
                "function",
                "anonymous",
                "expression",
                "python"
            ],
            "ideal": """
A lambda function is a small anonymous function defined using the
lambda keyword. It can accept arguments and return an expression.
Lambda functions are commonly used with functions such as map and filter.
"""
        },

        {
            "question": "What are decorators in Python?",
            "keywords": [
                "decorator",
                "function",
                "wrapper",
                "python"
            ],
            "ideal": """
A decorator is a function that modifies or extends the behavior of
another function without changing its original code. Decorators are
commonly used for logging, authentication and timing.
"""
        },

        {
            "question": "What is a virtual environment?",
            "keywords": [
                "virtual environment",
                "python",
                "dependencies",
                "package",
                "project"
            ],
            "ideal": """
A virtual environment is an isolated Python environment for a project.
It allows the project to have its own dependencies and package versions
without affecting other Python projects.
"""
        },

        {
            "question": "What is pip?",
            "keywords": [
                "pip",
                "python",
                "package",
                "install",
                "library"
            ],
            "ideal": """
pip is Python's package installer. It is used to install, upgrade and
remove packages from the Python Package Index and other package sources.
"""
        },

        {
            "question": "What is Flask?",
            "keywords": [
                "flask",
                "python",
                "web",
                "framework",
                "api"
            ],
            "ideal": """
Flask is a lightweight Python web framework used to build web
applications and APIs. It provides routing, request handling and
template rendering while allowing developers to add other components
as required.
"""
        },

        {
            "question": "What is the difference between shallow copy and deep copy?",
            "keywords": [
                "shallow",
                "deep",
                "copy",
                "object",
                "nested"
            ],
            "ideal": """
A shallow copy creates a new outer object but references nested
objects from the original. A deep copy recursively creates copies of
nested objects as well, so changes to nested data do not affect the
original object.
"""
        },

        {
            "question": "How can you improve the performance of a Python program?",
            "keywords": [
                "performance",
                "optimization",
                "algorithm",
                "profiling",
                "memory"
            ],
            "ideal": """
Python performance can be improved by choosing efficient algorithms
and data structures, avoiding unnecessary operations, using profiling
to identify bottlenecks, caching repeated computations and using
optimized libraries when appropriate.
"""
        }
    ]
}


# =========================================================
# CLEAN TEXT
# =========================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# =========================================================
# TOKENIZE
# =========================================================

def tokenize(text):

    return set(
        clean_text(text).split()
    )


# =========================================================
# KEYWORD SCORE
# =========================================================

def keyword_score(
    answer,
    keywords
):

    answer_clean = clean_text(
        answer
    )

    matched = []

    for keyword in keywords:

        keyword_clean = clean_text(
            keyword
        )

        if keyword_clean in answer_clean:

            matched.append(
                keyword
            )

    if not keywords:

        return 0, matched

    score = (
        len(matched)
        /
        len(keywords)
    ) * 100

    return round(
        score,
        2
    ), matched


# =========================================================
# TEXT SIMILARITY
# =========================================================

def similarity_score(
    answer,
    ideal_answer
):

    answer_words = tokenize(
        answer
    )

    ideal_words = tokenize(
        ideal_answer
    )

    if not answer_words or not ideal_words:

        return 0

    intersection = (
        answer_words
        &
        ideal_words
    )

    union = (
        answer_words
        |
        ideal_words
    )

    if not union:

        return 0

    similarity = (
        len(intersection)
        /
        len(union)
    ) * 100

    return round(
        similarity,
        2
    )


# =========================================================
# ANSWER LENGTH SCORE
# =========================================================

def length_score(answer):

    words = answer.split()

    count = len(words)

    if count < 5:

        return 20

    if count < 15:

        return 50

    if count < 30:

        return 80

    return 100


# =========================================================
# ANSWER EVALUATION
# =========================================================

def evaluate_answer(
    answer,
    question_data
):

    keywords = question_data[
        "keywords"
    ]

    ideal = question_data[
        "ideal"
    ]


    keyword_result, matched = keyword_score(
        answer,
        keywords
    )


    similarity = similarity_score(
        answer,
        ideal
    )


    length = length_score(
        answer
    )


    final_score = round(

        (
            keyword_result * 0.45
            +
            similarity * 0.40
            +
            length * 0.15
        ),

        2
    )


    # =====================================================
    # STRENGTHS
    # =====================================================

    strengths = []


    if keyword_result >= 70:

        strengths.append(
            "You covered most of the important concepts."
        )


    elif keyword_result >= 40:

        strengths.append(
            "You included some relevant technical concepts."
        )


    if similarity >= 50:

        strengths.append(
            "Your answer is relevant to the expected concept."
        )


    if length >= 80:

        strengths.append(
            "Your answer provides good detail."
        )


    if not strengths:

        strengths.append(
            "You attempted to answer the question."
        )


    # =====================================================
    # WEAKNESSES
    # =====================================================

    weaknesses = []


    missing_keywords = [

        keyword

        for keyword in keywords

        if keyword not in matched

    ]


    if missing_keywords:

        weaknesses.append(

            "Important concepts missing: "
            +
            ", ".join(
                missing_keywords[:6]
            )

        )


    if length < 50:

        weaknesses.append(

            "Your answer is too short. "
            "Try explaining the concept with an example."

        )


    if similarity < 35:

        weaknesses.append(

            "Your answer could be more directly "
            "connected to the question."

        )


    # =====================================================
    # PERSONALIZED FEEDBACK
    # =====================================================

    if final_score >= 85:

        feedback = (

            "Excellent answer! You demonstrated strong "
            "technical understanding. Add a practical example "
            "or real-world use case to make it even stronger."

        )

    elif final_score >= 70:

        feedback = (

            "Very good answer. You understand the core concept. "
            "Improve it further by adding technical details "
            "and a practical example."

        )

    elif final_score >= 50:

        feedback = (

            "Good start, but your answer needs more depth. "
            "Include the important concepts listed below and "
            "explain them clearly."

        )

    elif final_score >= 30:

        feedback = (

            "Your answer shows partial understanding. "
            "Review the topic and practice explaining it "
            "using a definition, key points and an example."

        )

    else:

        feedback = (

            "Your answer needs significant improvement. "
            "Study the topic and try to structure your response "
            "with a definition, explanation and practical example."

        )


    return {

        "score":
            final_score,

        "keyword_score":
            keyword_result,

        "similarity_score":
            similarity,

        "length_score":
            length,

        "matched_keywords":
            matched,

        "missing_keywords":
            missing_keywords,

        "strengths":
            strengths,

        "weaknesses":
            weaknesses,

        "feedback":
            feedback,

        "perfect_answer":
            ideal.strip()

    }


# =========================================================
# GET RANDOM QUESTION
# =========================================================

def get_question(
    role,
    used_questions=None
):

    questions = INTERVIEW_DATA[
        role
    ]


    if used_questions is None:

        used_questions = []


    available = [

        question

        for question in questions

        if question["question"]
        not in used_questions

    ]


    if not available:

        available = questions


    return random.choice(
        available
    )