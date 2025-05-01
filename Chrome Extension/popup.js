document.getElementById("summarizeBtn").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.executeScript(
      {
        target: { tabId: tabs[0].id },
        files: ["content.js"]
      }
    );
  });
});
console.log("Summarize button clicked");