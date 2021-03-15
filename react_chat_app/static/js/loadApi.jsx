
async function useLoadUserApi() {
    const location = window.origin
    const response = await fetch(location + "/api/groups_or_users/user/").catch((e) => {
        console.error(e);
    });
    const res = await response.json();
    return res;
}

async function useLoadWholeApi() {
    const location = window.origin;
    const response = await fetch(location + "/api/").catch((e) => {
        console.error(e);
    });
    const res = await response.json();
    return res;
}
