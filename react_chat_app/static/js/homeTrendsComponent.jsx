const UserTrendsComponent = () => {
    let [userData, setUserData] = React.useState([]);
    let [determinant, setDeterminant] = React.useState(0)
    React.useEffect(() => {
        useLoadUserApi().then(response => {
            setUserData(response);
            document.addEventListener("scroll", () => {
                if (window.scrollY >= document.body.offsetHeight - window.innerHeight - 200 && determinant < response.length) {
                    setDeterminant(determinant += 1);
                }
            });
            return document.removeEventListener("scroll", () => { });
        });
    }, []);

    const RenderUsers = () => {
        return (userData.map((element, i) => {
            return (
                i <= determinant ?
                    <article key={Math.random()} className="current-trends col-sm-12 mt-2">
                        <hr className="horizontal-line" />
                        <div className="follow-profile">
                            <div className="username-img">
                                <img src={element.image} className="br-25" height='50' width="50" />
                                <span className="text-initial ml-1">{element.username}</span>
                            </div>
                            <span className="text-secondary text-initial-grid">Handle: {element.handle}</span>
                        </div>
                        <span className="text-secondary text-initial-grid">Email: {element.email}</span>
                        <div className="mt-2 mb-2">
                            <span className="followers "><i className='fas fa-user text-initial-flex'></i> {element.followers}</span>
                            <span className="following ml-2"><i className='fas fa-user-circle text-initial-flex'></i> {element.following}</span>
                        </div>
                    </article>
                    : null
            )
        }));
    }

    return (
        <div className="request-user-profile trends mt-4  pos-relative hide">
            <h5 className="profile-header tweets-article col-sm-9">Trends</h5>
            <section className="user-profile mt-3 col-sm-9">
                <p className="text-secondary btn trends-header mt-2">Who to follow</p>
                <RenderUsers />
            </section>
        </div>
    )
};
