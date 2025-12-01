// Base URL of your FastAPI backend
const API_BASE = "http://127.0.0.1:8000/api";

/**
 * Upload a PDF file to the backend.
 * Returns JSON: { doc_id, filename, saved_path, num_characters, num_chunks, first_chunk_preview }
 */
async function uploadPdf(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_BASE}/upload`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    const txt = await res.text();
    throw new Error(`Upload failed: ${res.status} ${txt}`);
  }

  return res.json();
}

/**
 * Send a chat message to the backend.
 * Returns JSON: { answer }
 */
async function sendChatMessage(message) {
  const res = await fetch(`${API_BASE}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  if (!res.ok) {
    const txt = await res.text();
    throw new Error(`Chat request failed: ${res.status} ${txt}`);
  }

  return res.json();
}

console.log("api.js initialized");
