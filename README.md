# Job Search Static Website

Static HTML job search interface with filters for:

- Location
- Company size
- Main sector
- Position name

## Deploy to GitHub Pages

1. Create a GitHub repository.
2. Upload the files in this folder.
3. Go to **Settings → Pages**.
4. Under **Build and deployment**, select **GitHub Actions**.
5. Push to the `main` branch.

The workflow is located at:

`.github/workflows/deploy.yml`

## Local usage

Open `index.html` directly in a browser.

## Important

The current job results are sample data. You can later connect the interface to a job-search API or FastAPI backend.
