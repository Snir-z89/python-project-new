FROM python:latest
COPY ["main_scores.py", "Scores.txt", "./"]
CMD ["python", "/main_scores.py"]
