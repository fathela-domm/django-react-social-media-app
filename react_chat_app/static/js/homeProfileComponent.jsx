const UserProfileComponent = (props) => {
    let [userData, setUserData] = React.useState([]);
    React.useEffect(() => {
        useLoadUserApi().then(response => {
            setUserData(response);
        });
        document.getElementById("scream-creation").focus();
    }, []);
    const UserComponent = () => {
        const imgStyle = {
            borderRadius: "70px"
        }

        const handleClick = () => {
            document.querySelector(".screams-dialog").classList.remove("modal");
        }
        return userData.map(element => {
            let path = '/accounts/update/' + element.id;
            return element.username === props.user ? (
                <legend key={Math.random()}>
                    <span className="main-details">
                        <img className="ml-3" src={element.image} style={imgStyle} height="70" width="70" alt="" />
                        <span className="handle profile-text text-initial ml-2">
                            <a href={path}>{element.username}</a></span>
                    </span>
                    <div className="profile-data">
                        <span className="handle text-secondary profile-text text-initial">Handle: {element.handle}</span>
                        <span className="email text-secondary profile-text text-initial">Email: {element.email}</span>
                        <span className="followers text-secondary profile-text text-initial">Followers: {element.followers}</span>
                        <span className="following text-secondary profile-text text-initial">Following: {element.following}</span>
                        <div className="posts-screams mt-3 col-sm-12">
                            <i onClick={handleClick} className="text-initial fas fa-comments"></i>
                            {/* <i className="text-initial fas fa-cogs">Posts</i> */}
                        </div> 
                    </div>
                </legend>
            ) : null;
        });
    }
    return (
        <div className="request-user-profile user-profile m-auto mt-4 col-sm-9 tweets-article">
            <section className="mt-4">
                <article className="mt-4 mb-4">
                    <div className="user-detail tweets-article">
                        <UserComponent />
                    </div>
                    <div className="col-sm-4 tweets-article">
                        <ScreamCreationComponent uid={props.uid} token={props.token} user={props.user} />
                    </div>
                </article>
            </section>
        </div>
    )
};