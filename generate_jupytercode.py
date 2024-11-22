import os
import json
import glob
# Repository and structure details
chapter1files=glob.glob('chapter1/*.py')
chapper1files_basename=[]
for filename in chapter1files:
    chapper1files_basename.append(os.path.basename(filename))
chapters = {
    "chapter1": chapper1files_basename, #["scalar_case_example.py", "problem1.py", "problem2.py"],
    "chapter2": ["problem1.py", "problem2.py"]
}

# Function to create a valid JSON notebook structure
repo_url = "https://raw.githubusercontent.com/dharlabwustl/medicalimageanalysis/master"
def create_notebook(repo_url, chapter, problem):
    return {
        "cells": [
            {
                "cell_type": "code",
                "metadata": {},
                "source": [
                    "# Install any necessary libraries (optional)\n",
                    "# Uncomment and modify as needed\n",
                    "# !pip install numpy matplotlib\n\n",
                    "# Download the problem solution from GitHub\n",
                    f"!wget -O problem.py {repo_url}/{chapter}/{problem}\n\n",
                    "# Execute the solution\n",
                    "%run problem.py\n"
                ]
            }
        ],
        "metadata": {
            "colab": {
                "name": f"{chapter}_{problem.replace('.py', '')}.ipynb",
                "provenance": []
            },
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 0
    }

# Generate Notebooks
for chapter, problems in chapters.items():
    os.makedirs(chapter, exist_ok=True)
    for problem in problems:
        # Create the notebook content
        notebook_content = create_notebook(repo_url, chapter, problem)
        # Define the notebook file name
        notebook_name = f"{chapter}/{problem.replace('.py', '.ipynb')}"
        # Write the notebook content as JSON
        with open(notebook_name, "w") as f:
            json.dump(notebook_content, f, indent=2)

print("Notebooks generated!")
