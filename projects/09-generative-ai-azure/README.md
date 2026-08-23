# Generative AI Engineering, RAG & Azure AI Safety

## Project Overview
This portfolio project brings together several DSC 670 and DSC 680 exercises that demonstrate practical generative AI engineering rather than only prompt experimentation. The work covers API-based LLM applications, Retrieval-Augmented Generation (RAG), fine-tuning workflows, image generation, AI observability, and Microsoft Azure AI safety concepts.

## Technical Work Demonstrated
- Built OpenAI API prompt workflows in Python and Jupyter Notebook.
- Developed a transparent RAG chatbot using source collection, paragraph-aware chunking, TF-IDF retrieval, cosine similarity, and visible source passages for grounding review.
- Designed a childcare decision-support assistant architecture using an LLM plus RAG for changing local information.
- Adapted an Azure OpenAI fine-tuning example to the standard OpenAI API, including data validation, file upload, fine-tuning job creation, status monitoring, and model testing.
- Used the Stable Diffusion API for programmatic image generation and editing.
- Used MLflow to track GenAI model parameters and observability metrics such as request latency and token usage.
- Studied Microsoft Azure AI Content Safety, including harmful-content analysis, Prompt Shields, groundedness detection, protected-material detection, and agent-oriented safeguards.

## Tools & Technologies
Python, Jupyter Notebook, OpenAI API, RAG, scikit-learn, TF-IDF, cosine similarity, Stable Diffusion API, MLflow, Microsoft Azure AI Content Safety, prompt engineering, supervised fine-tuning workflows, responsible AI.

## Business Value
These exercises demonstrate how generative AI systems can be designed with stronger grounding, observability, safety, and human oversight. The focus is on practical enterprise concerns: reducing unsupported answers, protecting API credentials, monitoring cost and latency, limiting excessive agency, and keeping changing information outside the model when RAG is a better fit than memorization.

## Repository Contents
- `openai-api-prompt-workflows.ipynb` — zero-shot/one-shot API workflows and structured-output evaluation.
- `rag-wikipedia-chat.ipynb` — transparent RAG pipeline with visible retrieved evidence.
- `rag-childcare-assistant-design.pdf` — RAG-based decision-support design and prompt experiments.
- `openai-fine-tuning.ipynb` — supervised fine-tuning workflow adapted from an Azure OpenAI example.
- `stable-diffusion-api.ipynb` — image generation and editing through an external generative AI API.
- `mlflow-genai-observability.ipynb` — MLflow tracking for GenAI parameters, latency, and token metrics.
- `azure-ai-content-safety.pdf` — written analysis of Azure AI Content Safety and responsible deployment controls.

## Ethics and Limitations
The work is academic and demonstrates architecture, evaluation, and safety concepts. Azure AI Content Safety was studied through coursework and documentation; this portfolio does not claim production administration of an Azure tenant. Generative AI output requires grounding, testing, security controls, monitoring, and human review before high-impact use.
