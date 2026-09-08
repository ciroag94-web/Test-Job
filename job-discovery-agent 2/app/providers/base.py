from abc import ABC, abstractmethod

class JobProvider(ABC):
    @abstractmethod
    async def search_jobs(self, query: str, country: str):
        raise NotImplementedError
