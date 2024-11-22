import os

# Repository and structure details
repo_url = "https://raw.githubusercontent.com/dharlabwustl/medicalimageanalysis/master"
# import os
# Repository and structure details
# repo_url = "https://raw.githubusercontent.com/yourusername/problem-solutions/main"
chapters = {
    "chapter1": ["problem1.py", "problem2.py"],
    "chapter2": ["problem1.py", "problem2.py"]
}

# Correct Notebook Template using f-strings
def create_notebook(repo_url, chapter, problem):
    return f"""{{
 "cells": [
  {{
   "cell_type": "code",
   "metadata": {{}},
   "source": [
    "# Install any necessary libraries (optional)\\n",
    "# Uncomment and modify as needed\\n",
    "# !pip install numpy matplotlib\\n\\n",
    "# Download the problem solution from GitHub\\n",
    "!wget -O problem.py {repo_url}/{chapter}/{problem}\\n\\n",
    "# Execute the solution\\n",
    "%run problem.py\\n"
   ]
  }}
 ],
 "metadata": {{
  "colab": {{
   "name": "{chapter}_{problem}.ipynb",
   "provenance": []
  }},
  "kernelspec": {{
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }}
 }},
 "nbformat": 4,
 "nbformat_minor": 0
}}"""

# Generate Notebooks
for chapter, problems in chapters.items():
    os.makedirs(chapter, exist_ok=True)
    for problem in problems:
        notebook_content = create_notebook(repo_url, chapter, problem)
        notebook_name = f"{chapter}/{problem.replace('.py', '.ipynb')}"
        with open(notebook_name, "w") as f:
            f.write(notebook_content)

print("Notebooks generated!")
