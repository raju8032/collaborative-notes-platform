const versions = [
    {
        id: 1,
        version: "v1",
        date: "28 June 2026, 10:00 AM",
        content: "Hello",
        current: false
    },
    {
        id: 2,
        version: "v2",
        date: "28 June 2026, 11:00 AM",
        content: "Hello World",
        current: false
    },
    {
        id: 3,
        version: "v3",
        date: "28 June 2026, 12:00 PM",
        content: "Hello World!",
        current: false
    },
    {
        id: 4,
        version: "v4",
        date: "28 June 2026, 1:00 PM",
        content: "Hello World! How are you?",
        current: true
    }
];

function renderVersions() {
    const list = document.getElementById("version-list");
    list.innerHTML = "";

    versions.forEach((v) => {
        const card = document.createElement("div");
        card.className = "version-card";

        card.innerHTML = `
            <div class="version-info">
                <h3>${v.version} ${v.current ? '<span class="current-tag">Current</span>' : ""}</h3>
                <p>Saved on: ${v.date}</p>
                <p>Content: "${v.content}"</p>
            </div>
            <button 
                class="restore-btn" 
                onclick="restore(${v.id})"
                ${v.current ? "disabled" : ""}>
                ${v.current ? "Current" : "Restore"}
            </button>
        `;

        list.appendChild(card);
    });
}

function restore(id) {
    versions.forEach((v) => {
        v.current = v.id === id;
    });
    renderVersions();
    alert("Restored to " + versions.find(v => v.id === id).version);
}

renderVersions();
