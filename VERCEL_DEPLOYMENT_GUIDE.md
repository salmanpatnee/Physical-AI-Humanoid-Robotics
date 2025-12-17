# Vercel Deployment Guide

Complete step-by-step guide to deploy your full-stack application (Docusaurus frontend + FastAPI backend) to Vercel.

## Prerequisites

- GitHub account with access to: `salmanpatnee/Physical-AI-Humanoid-Robotics`
- Vercel account (free): https://vercel.com
- OpenAI API key from: https://platform.openai.com/api-keys
- Qdrant cloud instance with collection already ingested

## Step 1: Connect GitHub Repository to Vercel

### 1.1 Go to Vercel

1. Visit https://vercel.com
2. Sign in with your GitHub account (if not already signed in)

### 1.2 Create New Project

1. Click **"Add New..."** in top-right → **"Project"**
2. Or visit https://vercel.com/new

### 1.3 Import Repository

1. Click **"Import Git Repository"**
2. In the search box, find: `Physical-AI-Humanoid-Robotics`
3. Click the repository to import
4. Click **"Import"**

## Step 2: Configure Project Settings

After clicking Import, you'll see project configuration page:

### 2.1 Framework & Build Settings

Set these values:

| Setting | Value |
|---------|-------|
| **Framework Preset** | Other |
| **Root Directory** | `./` (leave default) |
| **Build Command** | `npm run vercel-build` |
| **Output Directory** | `build` |
| **Install Command** | `npm ci` |
| **Node.js Version** | 20 |

**Important:**
- Make sure "Override" is toggled ON for Build Command
- Leave other settings as default

### 2.2 Environment Variables

Scroll down to **"Environment Variables"** section.

Add these variables (you'll get values from backend/.env):

```
OPENAI_API_KEY = sk-proj-...
QDRANT_URL = https://...
QDRANT_API_KEY = ...
QDRANT_COLLECTION_NAME = book_content
DEFAULT_RELEVANCE_THRESHOLD = 0.7
DEFAULT_MAX_CONTENT_LENGTH = 2000
OPENAI_REQUEST_TIMEOUT = 30
QDRANT_REQUEST_TIMEOUT = 10
ALLOWED_ORIGIN = *
```

**For each variable:**
1. Type the name in "Name" field
2. Type the value in "Value" field
3. Click **"Save"**
4. Repeat for each variable

**Note:** Make sure all variables are set for ALL environments (you'll see checkboxes for Production, Preview, Development - select all)

### 2.3 Deploy

Click **"Deploy"** button.

**Vercel will now build and deploy your project.** This takes 3-5 minutes. You'll see:
- ⏳ Building frontend...
- ⏳ Building serverless functions...
- ✅ Deployment complete!

Watch the logs for any errors. Common issues:
- Missing environment variables → Check all vars are added
- Python dependency errors → Usually resolves automatically
- Build timeout → May need to optimize build

---

## Step 3: Verify Deployment

After deployment shows "Ready" or "✅ Complete":

### 3.1 Get Your Vercel URL

You should see: `your-project-name.vercel.app` (Vercel generates this)

Click the URL or visit it in your browser.

### 3.2 Test Frontend

1. Visit: `https://your-project-name.vercel.app`
2. Check that:
   - Homepage loads
   - Navigation works
   - Documentation pages render
   - No 404 errors

### 3.3 Test Health Endpoint

In your terminal:

```bash
curl https://your-project-name.vercel.app/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2025-12-17T...",
  "dependencies": {
    "openai_api": "connected",
    "vector_database": "connected"
  }
}
```

If you see `"unhealthy"`:
- Check environment variables in Vercel Dashboard
- Verify OPENAI_API_KEY and QDRANT credentials are correct
- Check Qdrant collection is accessible

### 3.4 Test Chatbot Endpoint

```bash
curl -X POST https://your-project-name.vercel.app/api/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is ROS2?"}'
```

Expected response:
```json
{
  "answer": "ROS2 is...",
  "sources": [
    {
      "content_snippet": "...",
      "source_location": "...",
      "relevance_score": 0.9
    }
  ],
  "confidence_score": 0.85,
  "timestamp": "2025-12-17T..."
}
```

If you get errors:
- 400 - Invalid question (check format)
- 500 - Server error (check Vercel logs)

### 3.5 View Logs

To debug issues, view deployment logs:

1. Go to Vercel Dashboard
2. Select your project
3. Click **"Deployments"**
4. Click the latest deployment
5. Scroll down to see build and runtime logs

Or from terminal:
```bash
vercel logs https://your-project-name.vercel.app
```

---

## Step 4: Test Chatbot in Browser

1. Visit your deployed site
2. Open a documentation page (e.g., "Book" section)
3. Look for chatbot widget (usually bottom-right corner)
4. Ask a question like "What is ROS2?"
5. Verify:
   - Question is sent
   - Response appears
   - Sources are shown
   - No errors in browser console (F12 → Console)

If chatbot doesn't work:
- Open browser DevTools (F12)
- Go to Console tab
- Look for CORS errors or fetch errors
- Check that API URL is correct: `/api/ask`

---

## Step 5: Security Update (Important!)

After deployment is verified working:

### 5.1 Update CORS Setting

Your deployment currently allows `ALLOWED_ORIGIN = *` (all origins).

For security, restrict to your actual domain:

1. Go to Vercel Dashboard
2. Select your project → Settings → Environment Variables
3. Find `ALLOWED_ORIGIN`
4. Change from `*` to: `https://your-project-name.vercel.app`
5. Click "Save"
6. Go to Deployments → Click "Redeploy" on the latest deployment

After redeployment, only your Vercel URL can access the API.

---

## Monitoring & Logs

### Real-time Logs

```bash
# Watch logs as requests come in
vercel logs --follow https://your-project-name.vercel.app

# Watch only API logs
vercel logs --follow https://your-project-name.vercel.app --output=api/ask.py
```

### Check Function Duration

After deployment, monitor serverless function performance:

1. Vercel Dashboard → Select Project
2. Click **"Functions"** tab
3. View:
   - Function execution time
   - Memory usage
   - Error rate
   - Request count

Typical metrics:
- Cold start: 5-10 seconds
- Warm requests: 3-8 seconds
- Memory: ~300-500 MB

### Performance Optimization

If response times are slow:
1. Check Vercel function logs for bottlenecks
2. Most time spent in:
   - OpenAI embeddings: 1-2 seconds
   - Qdrant search: 0.5-2 seconds
   - LLM response: 2-5 seconds

---

## Troubleshooting

### Issue: Deployment Failed

**Check:**
1. Build logs in Vercel Dashboard
2. Verify `vercel.json` syntax (JSON validator: https://jsonlint.com)
3. Verify `package.json` has `vercel-build` script

### Issue: API Returns 500 Error

**Check:**
1. Environment variables are set correctly
2. OpenAI API key is valid
3. Qdrant collection is accessible and has data
4. View function logs: Vercel Dashboard → Functions → Click function → Logs

### Issue: Chatbot Doesn't Appear or Work

**Check:**
1. Browser console for errors (F12)
2. Network tab (F12) to see API requests
3. CORS errors typically show in Network tab
4. Verify `API_BASE_URL` is empty string in chatAPI.js
5. Verify endpoint is `/api/ask` (not `/api/v1/ask`)

### Issue: Timeout Errors (504)

**Problem:** Vercel free tier has 10-second timeout, requests take 8+ seconds

**Solutions:**
1. Increase timeout in `vercel.json` (requires Pro)
2. Optimize response time:
   - Reduce vector search results (already set to 3)
   - Use faster models
3. Upgrade to Vercel Pro ($20/month) for 60-second timeout

---

## Next Steps After Deployment

### 1. Set Up Custom Domain (Optional)

1. Register domain (e.g., `physicalai-course.com`)
2. Vercel Dashboard → Settings → Domains
3. Add domain and follow DNS configuration

### 2. Enable Analytics (Optional)

1. Vercel Dashboard → Settings → Analytics
2. Enable Web Analytics
3. View performance metrics

### 3. Set Up CI/CD Notifications (Optional)

1. Vercel Dashboard → Settings → Notifications
2. Get alerts for failed deployments

### 4. Plan for Scaling

Monitor usage:
- Check Bandwidth usage (Vercel Dashboard)
- Monitor function execution time (Functions tab)
- Track error rate

**Upgrade to Pro when:**
- Consistent timeout errors
- Bandwidth usage >70% of 100 GB limit
- Need response caching

---

## Rolling Back Deployments

If something breaks after deployment:

### Quick Rollback (Vercel Dashboard)

1. Go to Vercel Dashboard
2. Click **"Deployments"** tab
3. Find the previous working deployment
4. Click the menu (•••) → **"Promote to Production"**
5. Done! Site reverted to previous version

### Git-based Rollback

```bash
# Revert to previous commit
git revert HEAD
git push origin 001-chatbot-docusaurus-integration

# Or reset to specific commit
git reset --hard <commit-hash>
git push --force origin 001-chatbot-docusaurus-integration
```

---

## Support & Resources

- **Vercel Docs:** https://vercel.com/docs
- **Vercel Python Runtime:** https://vercel.com/docs/functions/runtimes/python
- **Docusaurus Deployment:** https://docusaurus.io/docs/deployment
- **OpenAI API Docs:** https://platform.openai.com/docs
- **Qdrant Docs:** https://qdrant.tech/documentation

---

## Success Checklist

- ✅ GitHub repository connected to Vercel
- ✅ All environment variables configured
- ✅ Deployment shows "Ready"
- ✅ Frontend loads without errors
- ✅ `/api/health` returns "healthy"
- ✅ `/api/ask` endpoint responds with answers
- ✅ Chatbot widget works in browser
- ✅ No CORS errors in console
- ✅ Sources display correctly
- ✅ Response time <10 seconds

---

## Estimated Timeline

- **GitHub Connection:** 2 minutes
- **Configure Settings:** 5 minutes
- **Add Environment Variables:** 3 minutes
- **Initial Deploy:** 3-5 minutes
- **Verify & Test:** 5 minutes
- **Security Update:** 2 minutes
- **Total:** ~20-25 minutes

---

## Contact & Support

For issues:
1. Check Vercel Dashboard logs
2. Review this guide's troubleshooting section
3. Check browser console (F12)
4. View function logs in Vercel dashboard
