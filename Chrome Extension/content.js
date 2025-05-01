(async () => {
  const bodyText = document.body.innerText;
  const videoLink = window.location.href;

  const response = await fetch("https://ai-summarizer-chrome-extensionnn.onrender.com//summarize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: bodyText, url: videoLink })
});

  const data = await response.json();

  alert("Summary:\n\n" + data.summary);
})();
console.log("content.js injected and running");
