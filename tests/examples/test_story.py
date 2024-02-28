from datetime import datetime

from understand_sdk.examples.story import create_story


def test_example_story_structure(snapshot_json):
    dt = datetime(2024, 2, 1)
    story = create_story(dt)

    assert story.model_dump() == snapshot_json
