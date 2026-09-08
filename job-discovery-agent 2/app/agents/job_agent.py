import json
from app.services.job_search_service import JobSearchService
from app.services.matching_service import calculate_match

class JobAgent:
    def __init__(self):
        self.search_service = JobSearchService()

    async def run(self):
        with open("data/profile.json", "r", encoding="utf-8") as file:
            profile = json.load(file)

        queries = [
            "AML Compliance",
            "Financial Crime",
            "Compliance Officer",
            "AML Manager",
            "Transaction Monitoring",
            "Crypto Compliance"
        ]

        jobs = await self.search_service.search(
            queries=queries,
            countries=profile["countries"]
        )

        # Deduplicate primarily by URL.
        unique = {}
        for job in jobs:
            key = job.url or job.id
            if key not in unique:
                unique[key] = job

        ranked = []
        for job in unique.values():
            job.match_score = calculate_match(job, profile)
            ranked.append(job)

        ranked.sort(key=lambda job: job.match_score, reverse=True)
        return ranked
