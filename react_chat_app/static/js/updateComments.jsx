const CreateComments = (props) => {
    let fieldsetStyle = {
        height: "max-content",
        justifySelf: "center",
        margin: "auto",
    }

    let textAreaStyle = {
        height: "fit-content",
        backgroundColor: "rgba(17, 17, 26, 0.568)",
    }

    let textAreaRef = React.useRef(null);

    const handleClose = () => {
        document.getElementById(`comment-update-${props.id}`).classList.add("modal");
    }

    const handleCommentCreation = (form) => {
        if (textAreaRef.current.value !== "" && textAreaRef.current.value !== null) {
            form.preventDefault;
            const id = `scream-${props.id}`;
            const jsonData = {
                "comment": textAreaRef.current.value,
                "sender": props.user,
                "scream_connected": props.id,
            }
            postDataToAPI(jsonData, props.token, "create_comments").then((response) => { return (response) });
            setTimeout(() => {
                textAreaRef.current.value = "";
                let no = document.getElementById(`comment-bar-${props.id}`).innerHTML;
                document.getElementById(`comment-bar-${props.id}`).innerHTML = new Number(no) + 1;
                document.getElementById(`comment-update-${props.id}`).classList.add("modal");
            }, 50);
        }
        else
            return;
    }

    let id = "comment-update-" + props.id;

    let placeholder = "Comment on ..." + props.scream.substr(0, 20) + "..."
    return (
        <fieldset className="update-comments rounded bg-dark mb-3 pt-2 pb-2 modal col-sm-4" id={id} style={fieldsetStyle}>
            <form action="" className="comment-update-factory" onSubmit={handleCommentCreation}>
                <h5 className="text-primary"><i className="fas fa-comments"></i></h5>
                <textarea style={textAreaStyle} ref={textAreaRef} placeholder={placeholder} className="col-sm-12 form-group form-control text-white" id="update-scream"></textarea>
            </form>
            <span className="btn-submit">
                <button className="col-sm-8 btn-primary btn scream-submit" onSubmit={handleCommentCreation} onClick={handleCommentCreation}>comment</button>
                <button className="col-sm-4 btn btn-secondary" onClick={handleClose}>close</button>
            </span>
        </fieldset >
    )
}