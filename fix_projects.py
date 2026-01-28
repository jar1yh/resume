#!/usr/bin/env python3
import re

# Read the file
with open('resume.tex', 'r') as f:
    content = f.read()

# Define the new projects section
new_projects = r"""%-----------PROJECTS-----------
\section{Projects}
    \resumeSubHeadingListStart
      \resumeProjectHeading
          {\textbf{\href{https://github.com/jettyindeepl/Primary_Market_researcher}{BYOS - Build Your Own Survey}} $|$ \emph{Python, OpenAI GPT-4, LlamaIndex, Docker}}{}
          \resumeItemListStart
            \resumeItem{Developed an intelligent survey creation agent using OpenAI GPT-4 LLM and LlamaIndex that automatically generates contextual surveys based on user prompts and document attachments}
            \resumeItem{Implemented multi-agent orchestration system with vector embeddings for document retrieval, automated question generation, and web search integration for research-backed questions}
            \resumeItem{Containerized the application using Docker for seamless deployment, enabling dynamic survey creation through conversational AI interactions}
          \resumeItemListEnd
      \resumeProjectHeading
          {\textbf{\href{https://github.com/jettyindeepl/BYOC}{BYOC - Build Your Own Classifier}} $|$ \emph{Python, OpenAI GPT-4, Few-Shot Learning}}{}
          \resumeItemListStart
            \resumeItem{Developed an interactive few-shot learning system that iteratively refines text classifiers through human-in-the-loop learning}
            \resumeItem{System uses OpenAI GPT-4 LLM to generate targeted questions about unlabeled text, collects user feedback, and automatically updates class descriptions based on predictions vs. ground truth}
            \resumeItem{Implemented three-stage pipeline: question generation, interactive annotation, and class refinement, enabling adaptive classification without traditional model retraining}
          \resumeItemListEnd
    \resumeSubHeadingListEnd"""

# Use regex to replace the Projects section
pattern = r'%-----------PROJECTS-----------.*?\\resumeSubHeadingListEnd'
replacement_text = new_projects  
# Need to escape backslashes for re.sub
content_new = re.sub(pattern, lambda m: new_projects, content, flags=re.DOTALL)

# Write back
with open('resume.tex', 'w') as f:
    f.write(content_new)

print("Projects section updated successfully!")
