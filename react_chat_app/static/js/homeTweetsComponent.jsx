let UserTweetsComponent = (props) => {
    const ScreamComponent = () => {
        let [userData, setUserData] = React.useState([]);
        let [determinant, setDeterminant] = React.useState(0);
        let [deleteScream, setDelScream] = React.useState(null);
        let isSubmitting = React.useRef(false);
        React.useEffect(() => {
            setInterval(() => {
                useLoadWholeApi().then(response => {
                    setUserData(response.screams);
                });
            }, 1000);
            document.addEventListener("scroll", () => {
                if (window.scrollY >= document.body.offsetHeight - window.innerHeight - 500) {
                    setDeterminant(determinant += 1);
                }
            });

            document.querySelector(".scream-submit").addEventListener("click", () => {
                setTimeout(() => {
                    useLoadWholeApi().then(response => {
                        response.screams.length !== 0 ? document.getElementById("update-scream").value = response.screams[0].screams : null;
                        setUserData(response.screams);
                    });
                }, 20);
                document.addEventListener("scroll", () => {
                    if (window.scrollY >= document.body.offsetHeight - window.innerHeight - 550) {
                        setDeterminant(determinant += 1);
                    }
                });

                document.querySelector(".screams-dialog").classList.add("modal");
            });
            return (document.querySelector(".scream-submit").removeEventListener("input", () => { }))
        }, []);

        /* delete functionality */
        React.useEffect(() => {
            if (deleteScream !== null) {
                deleteDataFromApi("delete_a_scream", deleteScream, props.token);
                setTimeout(() => {
                    useLoadWholeApi().then(response => {
                        setUserData(response.screams);
                    });
                }, 200);
            }
            else
                return;
        }, [deleteScream]);


        /* functionality to update the likes and dislikes */
        let likesRef = React.useRef(null);
        let dislikesRef = React.useRef(null);
        let [id, setId] = React.useState(null);
        let [likeIsClicked, setLikeIsClicked] = React.useState(false);
        let [disLikeIsClicked, setDislikeIsClicked] = React.useState(false);

        React.useEffect(() => {
            let currentScreamToDislike = document.getElementById(`dislike-scream-${id}`);
            let currentScreamToLike = document.getElementById(`like-scream-${id}`);
            if (likeIsClicked) {
                currentScreamToDislike.classList.add("modal");
                const path = "update_a_scream";
                var likesCount = new Number(currentScreamToLike.innerHTML) + 1;

                const jsonData = {
                    likes: likesCount,
                }
                updateDataInApi(path, id, props.token, jsonData)
            }

            else if (disLikeIsClicked) {
                currentScreamToLike.classList.add("modal");
                const path = "update_a_scream";
                var disLikesCount = new Number(currentScreamToDislike.innerHTML) + 1;

                const jsonData = {
                    dislikes: disLikesCount,
                }
                updateDataInApi(path, id, props.token, jsonData)
            }
            return (setLikeIsClicked(false), setDislikeIsClicked(false))
        }, [likesRef.current, dislikesRef.current, id]);

        /* @end of likes update/dislikes */
        let handleUpdate = (id) => {
            document.getElementById(`scream-update-${id}`).classList.remove("modal");
        }

        const showCommentBox = (id) => {
            document.getElementById(`comment-update-${id}`).classList.remove("modal");
        }

        let commentStyles = {
            display: "flex",
            flexDirection: "row",
            width: "min-content"
        }

        return userData.map((scream, i) => {
            let apiDate = new Date(scream.date_created);
            const stringDate = apiDate.toString();
            const finalDate = stringDate.substr(0, 24);
            let id = `scream-${scream.id}`;
            let barId = `comment-${scream.id}`;
            let commentBar = `comment-bar-${scream.id}`;
            let delId = `del-scream-${scream.id}`;
            let likeId = `like-scream-${scream.id}`;
            let dislikeid = `dislike-scream-${scream.id}`;
            return (
                i <= determinant ?
                    <div className="my-tweets-main" key={i} id={scream.id}>
                        <section className="request-user-profile user-profile pos-relative my-tweets mt-1 mb-4 col-sm-9">
                            <div className="col-sm-12 screams mt-2 mb-4">
                                <div className="core">
                                    <img className="br-25" src={scream.sender_image} height="40" width="40" className="sender-image" />
                                    <p className="scream-sender mt-2 ml-2">{scream.sender}</p>

                                </div>
                                {
                                    props.user == scream.sender ?
                                        <small className="clear-delete mb-1 col-sm-12">
                                            <span className="delete-scream update" id={delId} onClick={() => { setDelScream(scream.id); }}><i className="fas fa-trash" ></i>clear</span>
                                            <span className="update update-comment ml-2" onClick={() => { handleUpdate(scream.id); }}>update</span>
                                            <span className="update ml-2"><i className="fas fa-thumbs-up"></i>{scream.likes}</span>
                                            <span className="update ml-2"><i className="fas fa-thumbs-down"></i>{scream.dislikes}</span>
                                            <ScreamUpdater id={scream.id} scream={scream.screams} token={props.token} />
                                        </small>
                                        : null
                                }
                                <span className="scream-body text-secondary" id={id}>{scream.screams}</span>
                                <small className="comments-likes-dislikes">
                                    <span className="likes text-secondary"><i className="fas btn fa text-initial fas fa-thumbs-up" onClick={() => { likesRef.current = scream.likes; setLikeIsClicked(true); setId(scream.id) }} id={likeId}>{scream.likes}</i></span>
                                    <span className="dislikes text-secondary"> <i className="fas btn text-initial fa fas fa-thumbs-down" onClick={() => { dislikesRef.current = scream.dislikes; setDislikeIsClicked(true); setId(scream.id) }} id={dislikeid}> {scream.dislikes}</i></span>
                                    <span className="comments " style={commentStyles} id={barId} onClick={() => { showCommentBox(scream.id) }}> <p className="ml-2" id={commentBar}> {scream.no_of_comments} </p>  <i className="fas fa-comment-alt ml-2 mt-1"></i></span>
                                    <CreateComments token={props.token} id={scream.id} scream={scream.screams} user={props.uid} />
                                </small>

                                <span className="timestamp text-secondary">{finalDate}</span>
                            </div>
                        </section>
                    </div>
                    : null
            )
        });
    }
    var headerStyle = {
        margin: "auto"
    }
    return (
        <article className="tweets-article mr-auto hide pos-static">
            <h5 className="profile-header mt-4 mb-3 col-sm-9" style={headerStyle}>Screams</h5>
            <ScreamComponent />
        </article>
    )
};