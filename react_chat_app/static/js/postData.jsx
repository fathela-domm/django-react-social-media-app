async function postDataToAPI(JSONscream, token, url_path) {
    const post_url = window.origin;
    await fetch(post_url + '/api/' + url_path + "/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFTOKEN": token,
        },
        body: JSON.stringify(JSONscream)
    })
}