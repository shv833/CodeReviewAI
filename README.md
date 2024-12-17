# CodeReviewAI

## How to run
1. Rename `.env.example` file to `.env`
2. Enter API_KEY inside quotes
2. Run command `make` or `make run`
3. Using terminal/postman - make POST request to `http://localhost:8000/review` 

CURL example:
```
curl http://localhost:8000/review -X POST -d '{
    "assignment_description": "Implement a function that calculates the factorial of a number.",
    "github_repo_url": "https://github.com/username/repo-name",
    "candidate_level": "Junior"
}' -H "Content-Type: application/json"
```

## Scalability Considerations
To handle 100+ new review requests per minute and large repositories with 100+ files, I would architect the system using a microservices approach.
Each service would be responsible for specific tasks, such as fetching repository contents, analyzing code, and managing user requests.
I would implement a message queue (e.g., RabbitMQ or Kafka) to decouple services and manage incoming requests efficiently.
For database solutions, I would use a scalable NoSQL database (like MongoDB) to store review requests and results, allowing for quick reads and writes.
Caching mechanisms (e.g., Redis) would be employed to store frequently accessed data and reduce API calls to GitHub and OpenAI, mitigating rate limits and costs.
Additionally, I would implement exponential backoff strategies for API requests to handle rate limits gracefully and consider using a load balancer to distribute traffic across multiple instances of the services to ensure reliability and performance.
