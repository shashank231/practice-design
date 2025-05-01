import asyncio
import time

async def fetch_data(source):
    print(f"Fetching data from {source}...")
    await asyncio.sleep(2)  # Simulate network delay
    # time.sleep(2)
    print(f"Data fetched from {source}")
    return f"Data from {source}"

async def main():
    sources = ["Source A", "Source B", "Source C"]
    
    # Create a list of tasks to run concurrently
    tasks = [fetch_data(source) for source in sources]
    
    # Run tasks concurrently
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
