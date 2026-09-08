import httpx
from app.models.job import Job

class ArbeitnowProvider:
    URL = "https://www.arbeitnow.com/api/job-board-api"

    async def search_jobs(self, query: str, country: str):
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(self.URL)
            response.raise_for_status()
            data = response.json()

        jobs = []
        query_words = query.lower().split()

        for item in data.get("data", []):
            text = (
                item.get("title", "") + " " +
                item.get("description", "") + " " +
                " ".join(item.get("tags", []))
            ).lower()

            if not any(word in text for word in query_words):
                continue

            location = item.get("location", "")
            remote = item.get("remote", False)

            if country.lower() not in location.lower() and not remote:
                continue

            jobs.append(Job(
                id=f"arbeitnow-{item.get('slug', item.get('url', 'job'))}",
                title=item.get("title", ""),
                company=item.get("company_name", ""),
                location=location,
                country=country,
                description=item.get("description", ""),
                url=item.get("url", ""),
                source="Arbeitnow",
                remote=remote,
                tags=item.get("tags", [])
            ))

        return jobs
