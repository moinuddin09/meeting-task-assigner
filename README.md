
# Meeting Task Assigner

Automatic extraction of tasks, deadlines, priorities and assignees from meeting audio.

## Overview
This project transcribes meeting audio (Whisper) and then uses a custom NLP pipeline (spaCy + rules + fuzzy matching) to identify actionable tasks, assign them to team members based on explicit mentions or skills, extract deadlines and priorities, and detect dependencies.

## Quickstart (Google Colab)

1. Mount Google Drive:
    from google.colab import drive
    drive.mount('/content/drive')

2. Install dependencies:
    apt-get update -y && apt-get install -y ffmpeg
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm

3. Add your audio file to:
    /content/drive/MyDrive/meeting-task-assigner/sample_data/

4. Run transcription → creates:
    outputs/transcript.txt

5. Run the NLP extraction cell → creates:
    outputs/tasks_refined.json


## Quickstart (Local / Conda)

    conda create -n meeting-task python=3.10 -y
    conda activate meeting-task
    conda install -c conda-forge ffmpeg python-levenshtein -y
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm

## Pipeline Usage

    python src/transcribe.py sample_data/youraudio.mp3 --out outputs/transcript.txt
    python src/nlp_pipeline.py --transcript outputs/transcript.txt --team sample_data/team.json --out outputs/tasks.json

## Output Format
tasks_refined.json contains:

    {
      "id": 1,
      "title": "...",
      "description": "...",
      "assigned_to": "Name",
      "deadline": "ISO or phrase",
      "priority": "Critical|High|Medium|Low",
      "dependencies": [],
      "reasoning": "why assigned"
    }

## Tests
    pytest tests/test_pipeline_basic.py -q

## Limitations
- ASR misrecognition of names can affect assignments.
- Date resolution assumes meeting date = current runtime timestamp.

## Next Steps
- Add speaker diarization
- Build a Streamlit UI
- Add better ML scoring rules
