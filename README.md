# RPC System with Docker + Timeout

A simple Python-based RPC (Remote Procedure Call) system with HTTP endpoints, Docker support, and timeout handling.

## 🚀 Live Demo

**Live Service**: https://rpc-implementation.onrender.com

Quick test:
```bash
curl -X POST https://rpc-implementation.onrender.com/add \
  -H "Content-Type: application/json" \
  -d '{"x": 2, "y": 3}'
```
*Expected response: `{"result":5}`*

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

## Local Development & Testing

### Prerequisites
- Python 3.11+
- pip
- Docker (optional, for containerization)

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

3. **Test with client (in another terminal):**
   ```bash
   python client.py
   ```
   This will connect to `http://localhost:8080` by default.

### Local Docker Testing

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

### Manual Testing (Local)

Test the local server endpoints:

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

**Expected Local Client Output:**
```
Connecting to RPC server at: http://localhost:8080

=== RPC Client Test Results ===
add(2,3) = 5
multiply(4,5) = 20
add(10,-5) = 5
multiply(7,8) = 56
add(0,100) = 100
```

## Cloud Deployment & Testing

### Deploy to Render.com

#### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial RPC system implementation"
git remote add origin https://github.com/yourusername/rpc-system.git
git push -u origin main
```

#### Step 2: Deploy on Render.com

1. **Sign up/Login** to [render.com](https://render.com)
2. **Connect GitHub** - Link your GitHub account
3. **Create Web Service**:
   - Click "New +" → "Web Service"
   - Select your GitHub repository

**Configuration:**
- **Name**: `rpc-server` (or your preferred name)
- **Environment**: `Python 3`
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: Leave empty (uses root)
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python server.py`
- **Port**: `8080` (auto-detected)
- **Health Check Path**: `/health`

#### Step 3: Test Your Cloud Deployment

Once deployed, you'll get a URL like: `https://your-app-name.onrender.com`

**Test with client:**
```bash
python client.py https://your-app-name.onrender.com
```

**Test manually with curl:**
```bash
# Test add endpoint
curl -X POST https://your-app-name.onrender.com/add \
  -H "Content-Type: application/json" \
  -d '{"x": 2, "y": 3}'

# Test multiply endpoint
curl -X POST https://your-app-name.onrender.com/multiply \
  -H "Content-Type: application/json" \
  -d '{"x": 4, "y": 5}'

# Health check
curl https://your-app-name.onrender.com/health
```

### Live Example (Current Deployment)

**Live Service URL**: https://rpc-implementation.onrender.com

**Test the live deployment:**
```bash
# Test with client
python client.py https://rpc-implementation.onrender.com

# Test with curl
curl -X POST https://rpc-implementation.onrender.com/add \
  -H "Content-Type: application/json" \
  -d '{"x": 2, "y": 3}'
```

**API Endpoints:**
- Add: `https://rpc-implementation.onrender.com/add`
- Multiply: `https://rpc-implementation.onrender.com/multiply`
- Health: `https://rpc-implementation.onrender.com/health`

### Render.com Free Tier Notes

- **Sleep Mode**: Free tier services sleep after 15 minutes of inactivity
- **Cold Start**: First request after sleep may take 10-30 seconds
- **Monthly Hours**: 750 hours/month free (enough for most projects)

### Troubleshooting

**Common Issues:**
1. **Build Fails**: Check `requirements.txt` format
2. **Port Issues**: Ensure server uses `port=8080` and `host='0.0.0.0'`
3. **Health Check**: Service uses `/health` endpoint for monitoring

**Logs:** View logs in Render dashboard → Your Service → Logs tab

## Example Client Output

### Local Development Output:
```
Connecting to RPC server at: http://localhost:8080

=== RPC Client Test Results ===
add(2,3) = 5
multiply(4,5) = 20
add(10,-5) = 5
multiply(7,8) = 56
add(0,100) = 100
```

### Cloud Deployment Output:
```
Connecting to RPC server at: https://rpc-implementation.onrender.com

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
├── server.py              # Flask RPC server
├── client.py              # RPC client with timeout
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── test_deployed.py      # Deployment test script
├── test_timeout.py       # Timeout test server
├── test_timeout_client.py # Timeout test client
├── render.yaml           # Render.com config (optional)
├── .gitignore           # Git ignore file
└── README.md            # This documentation
```

## Error Handling

- **Server Errors**: Proper HTTP status codes and JSON error responses
- **Client Timeouts**: 2-second timeout with graceful failure
- **Network Issues**: Connection error handling
- **Input Validation**: Missing parameter validation

## Testing

### Test Commands by Environment

**Local Testing:**
```bash
# Test with Python client (defaults to localhost)
python client.py

# Test with custom local URL
python client.py http://localhost:8080

# Manual curl tests
curl -X POST http://localhost:8080/add \
  -H "Content-Type: application/json" \
  -d '{"x": 2, "y": 3}'
```

**Cloud Testing:**
```bash
# Test deployed service
python client.py https://rpc-implementation.onrender.com

# Manual curl tests
curl -X POST https://rpc-implementation.onrender.com/add \
  -H "Content-Type: application/json" \
  -d '{"x": 2, "y": 3}'

# Use test script for comprehensive testing
python test_deployed.py https://rpc-implementation.onrender.com
```
