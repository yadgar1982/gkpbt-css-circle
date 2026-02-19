function analyzeText() {
    const text = document.getElementById("userText").value;
    if (!text) {
        alert(" Invalid text! Please try again!.");
        return;
    }

    fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById("result").innerText = data;
        })
        .catch(error => {
            console.error("Error:", error);
        });
}
