import os
import httpx
from app.models.job import Job

class AdzunaProvider:
    BASE_URL = "https://api.adzuna.com/v1/api/jobs"
    COUNTRY_CODES = {
        "Italy": "it",
        "Germany": "de",
        "Netherlands": "nl",
        "Spain": "es"
    }

    def __init__(self):
        self.app_id = os.getenv("ADZUNA_APP_ID")
        self.app_key = os.getenv("ADZUNA_APP_KEY")

    async def search_jobs(self, query: str, country: str):
        if not self.app_id or not self.app_key:
            return []

        code = self.COUNTRY_CODES[country]
        url = f"{self.BASE_URL}/{code}/search/1"
        params = {
            "app_id": self.app_id,
            "app_key": self.app_key,
            "what": query,
            "results_per_page": 50,
            "content-type": "application/json"
        }

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

        jobs = []
        for item in data.get("results", []):
            jobs.append(Job(
                id=f"adzuna-{item['id']}",
                title=item.get("title", ""),
                company=item.get("company", {}).get("display_name", ""),
                location=item.get("location", {}).get("display_name", ""),
                country=country,
                description=item.get("description", ""),
                url=item.get("redirect_url", ""),
                source="Adzuna",
                salary_min=item.get("salary_min"),
                salary_max=item.get("salary_max")
            ))
        return jobs
