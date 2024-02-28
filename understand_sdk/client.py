from typing import Generic, List, TypeVar

import requests

from understand_sdk.const import DEFAULT_HOST
from understand_sdk.model import BaseModel
from understand_sdk.story import Story, StoryWithChannels
from understand_sdk.task import Event, Task


class CreatedStory(BaseModel):
    id: str


PayloadT = TypeVar("PayloadT")


class Response(BaseModel, Generic[PayloadT]):
    status: str
    payload: PayloadT


class UnderstandPublicClient:
    """ """

    def __init__(self, api_key: str, host: str = DEFAULT_HOST):
        self.host = host

        self.session = requests.Session()
        self.session.headers.update({"X-UL-API-KEY": api_key})

    def create_story(self, story: StoryWithChannels) -> CreatedStory:
        res = self.session.post(
            f"{self.host}/api/v1/public/stories", json=story.model_dump(exclude_none=True, by_alias=True)
        )
        res.raise_for_status()

        raw_data = res.json()
        data = Response[CreatedStory](**raw_data)
        return data.payload


class UnderstandClient:
    """ """

    def __init__(self, token: str, host: str = DEFAULT_HOST):
        self.host = host

        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def get_task(self) -> Task:
        res = self.session.get(f"{self.host}/api/v1/internal/task")
        res.raise_for_status()

        raw_data = res.json()
        data = Response[Task].model_validate(raw_data)
        return data.payload

    def create_stories(self, stories: List[Story]):
        res = self.session.post(
            f"{self.host}/api/v1/internal/task/stories",
            json=[story.model_dump(exclude_none=True, by_alias=True) for story in stories],
        )
        res.raise_for_status()

    def create_task_events(self, events: List[Event]):
        self.session.post(
            f"{self.host}/api/v1/internal/task/events",
            json=[event.model_dump(exclude_none=True, by_alias=True) for event in events],
        )
