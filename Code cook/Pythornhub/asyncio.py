import asyncio
import httpx

async def fetch_data(url, semaphore):
    async with semaphore:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return {
                'url': url,
                'status_code': response.status_code,
                'content': response.text
            }

async def main():
    urls = [
        'https://example.com',
        'https://example.org',
        'https://example.net'
    ]
    
    semaphore = asyncio.Semaphore(2)
    tasks = [fetch_data(url, semaphore) for url in urls]
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(result)
        
if __name__ == '__main__':
    asyncio.run(main())



