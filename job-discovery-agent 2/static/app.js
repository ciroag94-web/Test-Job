const jobsContainer = document.getElementById("jobs");
const status = document.getElementById("status");
const button = document.getElementById("searchButton");
const template = document.getElementById("job-template");

async function loadJobs() {
  button.disabled = true;
  status.textContent = "Searching job sources...";
  jobsContainer.innerHTML = "";

  try {
    const response = await fetch("/api/jobs");
    if (!response.ok) throw new Error("Job search failed");

    const jobs = await response.json();

    if (!jobs.length) {
      jobsContainer.textContent =
        "No jobs found. Check your API credentials or add more providers.";
      return;
    }

    jobs.forEach(job => {
      const node = template.content.cloneNode(true);
      node.querySelector(".score").textContent = `${job.match_score}% match`;
      node.querySelector(".source").textContent = job.source;
      node.querySelector(".title").textContent = job.title;
      node.querySelector(".company").textContent = job.company;
      node.querySelector(".location").textContent =
        `📍 ${job.location || "Location not specified"}`;
      node.querySelector(".country").textContent =
        `🌍 ${job.country || "Country not specified"}`;
      node.querySelector(".description").textContent =
        (job.description || "").slice(0, 300) + "...";

      const link = node.querySelector(".link");
      link.href = job.url;
      jobsContainer.appendChild(node);
    });

    status.textContent = `${jobs.length} jobs found`;
  } catch (error) {
    jobsContainer.textContent = error.message;
    status.textContent = "";
  } finally {
    button.disabled = false;
  }
}

button.addEventListener("click", loadJobs);
