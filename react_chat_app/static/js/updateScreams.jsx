const ScreamUpdater = (props) => {
    let textAreaRef = React.useRef(null);
    let textAreaStyle = {
        height: "fit-content",
        backgroundColor: "rgba(17, 17, 26, 0.568)",
    }

    let fieldsetStyle = {
        height: "max-content",
        justifySelf: "center",
        margin: "auto",
    }

    React.useEffect(() => {
        textAreaRef.current.value = props.scream;
    }, []);

    const handleSubmit = (e) => {
        e.preventDefault;
        const url_path = "update_a_scream";
        let id = `scream-${props.id}`;
        const jsonData = {
            "screams": textAreaRef.current.value,
        }
        document.getElementById(id).innerHTML = textAreaRef.current.value;
        updateDataInApi(url_path, props.id, props.token, jsonData);
        setTimeout(() => {
            document.getElementById(`scream-update-${props.id}`).classList.add("modal");
        }, 50);
    }

    let id = "scream-update-" + props.id;

    const handleClose = () => {
        document.getElementById(`scream-update-${props.id}`).classList.add("modal");
    }

    return (
        <fieldset className="update-screams rounded bg-light mb-3 pt-2 pb-2 col-sm-4 modal" id={id} style={fieldsetStyle}>
            <form action="" className="scream-update-factory" onSubmit={handleSubmit}>
                <h5 className="text-secondary">Update This Scream</h5>
                <textarea ref={textAreaRef} style={textAreaStyle} className="col-sm-12 form-group form-control text-white" id="update-scream"></textarea>
            </form>
            <span className="btn-submit">
                <button className="col-sm-8 btn-primary btn scream-submit" onClick={handleSubmit}>Submit Changes</button>
                <button onClick={handleClose} className="col-sm-4 btn-secondary btn ">Close</button>
            </span>
        </fieldset>
    )
}   