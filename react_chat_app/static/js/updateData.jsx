async function updateDataInApi(update_path, id, token, JSONdata) {
    const main_url = window.origin;
    await fetch(`${main_url}/api/${update_path}/${id}/`, {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFTOKEN": token,
        },
        body: JSON.stringify(JSONdata),
    });
}
