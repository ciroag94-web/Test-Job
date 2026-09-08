def calculate_match(job, profile):
    score = 0
    text = " ".join([
        job.title or "",
        job.description or "",
        " ".join(job.tags or [])
    ]).lower()

    for skill in profile.get("skills", []):
        if skill.lower() in text:
            score += 5

    for role in profile.get("target_roles", []):
        if role.lower() in job.title.lower():
            score += 15

    if job.country in profile.get("countries", []):
        score += 10

    if job.remote:
        score += 5

    return min(score, 100)
