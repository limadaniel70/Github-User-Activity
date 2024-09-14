tracked_events: list[str] = ["PushEvent", "PullRequestEvent", "IssuesEvent"]


def parse(response) -> list[str]:
    messages: list[str] = []
    for event in response:
        if event["type"] in tracked_events:
            if event["type"] == tracked_events[0]:
                messages.append(parse_push(event))
            elif event["type"] == tracked_events[1]:
                messages.append(parse_pull_request(event))
            elif event["type"] == tracked_events[2]:
                messages.append(parse_issue(event))
        continue
    return messages


def parse_issue(event) -> str:
    repo: str = get_repository(event)
    issue_type: str = event["payload"]["action"]
    return f"{issue_type} in {repo}"


def parse_push(event) -> str:
    repo: str = get_repository(event)
    n_of_commits: int = event["payload"]["size"]
    return f"pushed {n_of_commits} commits into {repo}"


def parse_pull_request(event) -> str:
    type: str = event["payload"]["action"]
    repo: str = get_repository(event)
    return f"{type} a pull request in {repo}"


def get_repository(event) -> str:
    return event["repo"]["name"]
