const ScreamCreationComponent = (props) => {
    let textAreaStyle = {
        "height": "40px",
        "border": "none",
        "outline": "none",
        "backgroundColor": "rgba(17, 17, 26, 0.568)",
        "paddingTop": "7px",
    }

    let screamDeitails = {
        sender: props.uid,
        screams: null,
        likes: 0,
        dislikes: 0,
    }
    let textAreaRef = React.useRef(null);
    let [screamIsCreated, setScreamCreated] = React.useState(false);
    const handleSubmit = (form) => {
        form.preventDefault;
        if (textAreaRef.current.value !== null && textAreaRef.current.value !== "") {
            setScreamCreated(true);
            screamDeitails.screams = textAreaRef.current.value;
            postDataToAPI(screamDeitails, props.token, "create_screams").then((response) => { return (response) });
            textAreaRef.current.value = "";
        }
        else {
            document.querySelector(".screams-dialog").classList.remove("modal");
            document.querySelector(".scream-header").innerHTML = "<p class='text-danger'>Please Scream In The Text Area Below!</p>"
        }
    }

    const handleClose = () => {
        document.querySelector(".screams-dialog").classList.add("modal");
    }

    return (
        <fieldset className="screams-dialog modal  rounded border-primary bg-light mb-2 col-sm-12 pt-2 pb-2" role="dialog">
            <h4 className="scream-header text-secondary">Post a Scream</h4>
            <form action="" className="create-scream" onSubmit={handleSubmit}>
                <textarea ref={textAreaRef} style={textAreaStyle} className="col-sm-12 form-group form-control text-white" id="scream-creation"></textarea>
            </form>
            <span className="btn-submit">
                <button onClick={handleSubmit} className=" col-sm-8 btn-primary btn scream-submit">Scream</button>
                <button onClick={handleClose} className=" col-sm-4 btn-danger btn">Close</button>
            </span>
        </fieldset>
    )
}