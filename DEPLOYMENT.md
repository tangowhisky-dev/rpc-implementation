# Render.com Deployment Guide

## Quick Deployment Steps

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial RPC system implementation"
git remote add origin https://github.com/yourusername/rpc-system.git
git push -u origin main
```

### 2. Deploy on Render.com

1. **Sign up/Login** to [render.com](https://render.com)
2. **Connect GitHub** - Link your GitHub account
3. **Create Web Service**:
   - Click "New +" → "Web Service"
   - Select your GitHub repository
   - Configure:

#### Basic Settings
- **Name**: `rpc-server` (or your preferred name)
- **Environment**: `Python 3`
- **Region**: Choose closest to you
- **Branch**: `main`

#### Build & Deploy
- **Root Directory**: Leave empty (uses root)
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python server.py`

#### Advanced Settings
- **Port**: `8080` (auto-detected)
- **Health Check Path**: `/health`

### 3. Test Your Deployment

Once deployed, Render will provide a URL like:
`https://your-app-name.onrender.com`

Test with the client:
```bash
python client.py https://your-app-name.onrender.com
```

Or manually with curl:
```bash
# Test add
curl -X POST https://your-app-name.onrender.com/add \
  -H "Content-Type: application/json" \
  -d '{"x": 2, "y": 3}'

# Test multiply  
curl -X POST https://your-app-name.onrender.com/multiply \
  -H "Content-Type: application/json" \
  -d '{"x": 4, "y": 5}'
```

### 4. Share Your Results

After deployment, you'll have:
- **API URL**: `https://your-app-name.onrender.com`
- **Add endpoint**: `https://your-app-name.onrender.com/add`
- **Multiply endpoint**: `https://your-app-name.onrender.com/multiply`

## Render.com Free Tier Notes

- **Sleep Mode**: Free tier services sleep after 15 minutes of inactivity
- **Cold Start**: First request after sleep may take 10-30 seconds
- **Monthly Hours**: 750 hours/month free (enough for most projects)

## Troubleshooting

### Common Issues:

1. **Build Fails**: Check `requirements.txt` format
2. **Port Issues**: Ensure server uses `port=8080` and `host='0.0.0.0'`
3. **Health Check**: Service uses `/health` endpoint for monitoring

### Logs:
View logs in Render dashboard → Your Service → Logs tab

## Environment Variables (Optional)

If needed, you can set environment variables in Render:
- Go to your service → Environment tab
- Add variables like `FLASK_ENV=production`
