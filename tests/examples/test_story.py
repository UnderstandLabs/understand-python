from datetime import datetime

from understand_sdk.examples.story import create_story, create_story_with_channels


def test_example_story_structure(snapshot_json):
    dt = datetime(2024, 2, 1)
    story = create_story(dt)

    assert story.model_dump(exclude_none=True, by_alias=True) == snapshot_json


def test_example_story_with_channels_structure(snapshot_json):
    dt = datetime(2024, 2, 1)
    story = create_story_with_channels(dt)

    assert story.model_dump(exclude_none=True, by_alias=True) == snapshot_json
