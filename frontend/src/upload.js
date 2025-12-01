console.log("upload.js initialized");

const uploadForm = document.getElementById("uploadForm");
const pdfFileInput = document.getElementById("pdfFile");
const uploadStatus = document.getElementById("uploadStatus");
const uploadButton = uploadForm ? uploadForm.querySelector("button[type='submit']") : null;

function setStatus(message, color = "#9ca3af") {
  if (!uploadStatus) return;
  uploadStatus.textContent = message;
  uploadStatus.style.color = color;
}

if (uploadForm) {
  uploadForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const file = pdfFileInput.files[0];
    console.log("Submit clicked. Current file:", file);

    if (!file) {
      setStatus("Please choose a PDF file first.", "#f97373"); // red
      return;
    }

    // UI: disable button + show loading
    uploadButton.disabled = true;
    uploadButton.textContent = "Uploading...";
    setStatus("Uploading and indexing your PDF...", "#9ca3af");

    try {
      console.log("Uploading file:", file.name, file.size, "bytes");
      const result = await uploadPdf(file);

      console.log("Upload result from backend:", result);

      setStatus(
        `Uploaded "${result.filename}" • Characters: ${result.num_characters} • Chunks: ${result.num_chunks}`,
        "#10b981" // green
      );

      // IMPORTANT: we DO NOT clear the file now
      // pdfFileInput.value = "";   <-- make sure this line does NOT exist
    } catch (err) {
      console.error("Upload error:", err);
      setStatus("Upload failed. Check console and backend logs.", "#f97373");
    } finally {
      uploadButton.disabled = false;
      uploadButton.textContent = "Upload";
    }
  });

  pdfFileInput.addEventListener("change", () => {
    const file = pdfFileInput.files[0];
    console.log("File input changed. New file:", file);
    if (file) {
      setStatus(`Selected file: "${file.name}". Click Upload to process.`, "#9ca3af");
    } else {
      setStatus("");
    }
  });
}
