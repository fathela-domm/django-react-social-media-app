const HomeHeaderComponent = (props) => {
    let headerStyle = {
        marginTop: "120px",
    }
    return (
        <div id="container  pos-relative hide mt-4 " style={headerStyle}>
            <section className="header-element col-sm-11 replace mr-auto mr-2">
                <img className="logo-image mr-2 mt-1" src={props.image} height="40" width="40" alt="" />
                <h1 className="text-success text-success-outline">BlogRoom</h1>
            </section>
        </div>
    )
};