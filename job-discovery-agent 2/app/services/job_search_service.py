from app.providers.adzuna import AdzunaProvider
from app.providers.arbeitnow import ArbeitnowProvider

class JobSearchService:
    def __init__(self):
        self.providers = [
            AdzunaProvider(),
            ArbeitnowProvider()
        ]

    async def search(self, queries, countries):
        jobs = []

        for country in countries:
            for query in queries:
                for provider in self.providers:
                    try:
                        results = await provider.search_jobs(query, country)
                        jobs.extend(results)
                    except Exception as error:
                        print(f"Provider error ({provider.__class__.__name__}): {error}")

        return jobs
