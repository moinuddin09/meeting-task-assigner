import json
from pathlib import Path

BASE = Path("/content/drive/MyDrive/meeting-task-assigner")
OUT = BASE / "outputs" / "tasks_refined.json"

def test_tasks_refined_exists():
    assert OUT.exists(), "tasks_refined.json missing; run pipeline first"

def test_expected_task_count():
    data = json.loads(OUT.read_text(encoding='utf-8'))
    tasks = data['tasks']
    # We'll expect at least 6 useful tasks from this meeting
    assert len(tasks) >= 6, f"Expected at least 6 tasks, found {len(tasks)}"

def test_core_assignments_present():
    data = json.loads(OUT.read_text(encoding='utf-8'))
    names = set(t.get('assigned_to') for t in data['tasks'] if t.get('assigned_to'))
    # Ensure key team members appear as assignees somewhere
    assert "Sakshi" in names, "Sakshi should be assigned (login bug)"
    assert "Mohit" in names, "Mohit should be assigned (DB/API)"
    assert "Lata" in names, "Lata should be assigned (unit tests)"
    assert "Arjun" in names, "Arjun should be assigned (UI tasks)"
