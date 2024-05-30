async function SendRequest(prompt) {
    try {
        const response = await fetch('http://127.0.0.1:8000/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ tech: prompt })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }

        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

function DisplayResponse(display) {
    document.getElementById("viewer").innerHTML = display ? JSON.stringify(display) : 'No response';
}

function GetSearch() {
    return document.getElementById("search-bar").value;
}

const btn = document.querySelector('button');

btn.onclick = async () => {
    const s = GetSearch();
    document.getElementById("loading-bar").innerHTML = "🏄Hang in there... Almost there...👨‍💻";
    // alert("Please wait for a few seconds till the ✨AI✨ returns its response 🐱‍💻.");
    const response = await SendRequest(s);
    DisplayResponse(response);
    document.getElementById("loading-bar").innerHTML = "";
}