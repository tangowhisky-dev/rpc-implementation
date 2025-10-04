# RPC System with Docker + Timeout

A simple Python-based RPC (Remote Procedure Call) system with HTTP endpoints, Docker support, and timeout handling.

## Features

- **RPC Server**: Flask-based server with `/add` and `/multiply` endpoints
- **RPC Client**: Python client with 2-second timeout handling
- **Docker Support**: Containerized server deployment
- **Error Handling**: Comprehensive timeout and error management

## API Endpoints

### POST /add
Add two numbers.

**Request:**
```json
{
  "x": 2,
  "y": 3
}
```

**Response:**
```json
{
  "result": 5
}
```

### POST /multiply
Multiply two numbers.

**Request:**
```json
{
  "x": 4,
  "y": 5
}
```

**Response:**
```json
{
  "result": 20
}
```

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Local Development

### Prerequisites
- Python 3.11+
- pip

### Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   python server.py
   ```
   Server will start on `http://localhost:8080`

3. **Run the client (in another terminal):**
   ```bash
   python client.py
   ```

   To connect to a different server:
   ```bash
   python client.py https://your-server-url.com
   ```

## Docker Deployment

### Build and Run Locally

1. **Build the Docker image:**
   ```bash
   docker build -t rpc-server .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8080:8080 rpc-server
   ```

3. **Test with client:**
   ```bash
   python client.py http://localhost:8080
   ```

## Render.com Deployment

### Step 1: Prepare for Deployment

1. Create a `render.yaml` file (optional, for infrastructure as code)
2. Push your code to GitHub
3. Connect your GitHub repo to Render.com

### Step 2: Deploy on Render.com

1. Go to [render.com](https://render.com)
2. Create a new **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py`
   - **Port**: 8080

### Step 3: Test Deployment

Once deployed, test your endpoints:

```bash
# Replace with your actual Render URL
python client.py https://your-app-name.onrender.com
```

Or test manually with curl:
```bash
curl -X POST https://your-app-name.onrender.com/add \
  -H "Content-Type: application/json" \
  -d '{"x": 2, "y": 3}'
```

## Example Client Output

```
Connecting to RPC server at: http://localhost:8080

=== RPC Client Test Results ===
add(2,3) = 5
multiply(4,5) = 20
add(10,-5) = 5
multiply(7,8) = 56
add(0,100) = 100
```

## Timeout Handling

The client includes a 2-second timeout for all requests. If the server doesn't respond within this time:

```
Request timed out
```

## Project Structure

```
asg1/
├── server.py          # Flask RPC server
├── client.py          # RPC client with timeout
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker configuration
└── README.md         # This file
```

## Error Handling

- **Server Errors**: Proper HTTP status codes and JSON error responses
- **Client Timeouts**: 2-second timeout with graceful failure
- **Network Issues**: Connection error handling
- **Input Validation**: Missing parameter validation

## Testing

Test the server endpoints manually:

```bash
# Test add endpoint
curl -X POST http://localhost:8080/add \
  -H "Content-Type: application/json" \
  -d '{"x": 2, "y": 3}'

# Test multiply endpoint
curl -X POST http://localhost:8080/multiply \
  -H "Content-Type: application/json" \
  -d '{"x": 4, "y": 5}'

# Health check
curl http://localhost:8080/health
```
