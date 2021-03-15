const SearchChatStudio = () => {
    useLoadUserApi().then(res => {
        let usernames = [];
        res.map((element, i) => {
            usernames.push(element.username)
        })
    });
    let styles = {
        "backgroundColor": "rgba(31, 31, 36, 0.726)",
        "borderRadius": "15px",
        "border": "none",
        "paddingTop": "-3px",
        "marginLeft": "-17px"
    }

    let searchColor = {
        color: "ivory",
    }
    // to prevent form submission
    let handleSubmit = (e) => {
        e.preventDefault();
        document.querySelector(".i-search").innerHTML = "<i class='fas fa-cog fa-spin text-initial'></i>"
    }
    return (
        <section className="search-section tweets-article col-sm-9  pos-relative hide">
            <form action="" onSubmit={handleSubmit}>
                <input type="text" style={styles} className="search-input form-group form-control col-sm-5" placeholder="Search Chat Studio" />
                <button className="btn i-search" type="submit"><i style={searchColor} className="fa fa-search"></i></button>
            </form>
        </section>
    )
};