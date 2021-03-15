const NavbarBottomComponent = () => {
    let anchorStyle = {
        height: " 40px",
        justifyContent: "center",
        paddingTop: "5px",
    }

    return (
        <footer className="navbar-bottom navbar-expand-md navbar-dark  pos-relative hide">
            <div className="navbar-bottom-left">
                <div className="list-drops-up">
                    <ul className="list">
                        <li className="list-component first" style={anchorStyle}>
                            <a className="nav-link-item-bottom text-primary" href="#">Terms of Service</a>
                        </li>
                        <li className="list-component" style={anchorStyle}>
                            <a className="nav-link-item-bottom text-primary" href="#">Privacy policy</a>
                        </li>
                        <li className="list-component" style={anchorStyle}>
                            <a className="nav-link-item-bottom text-primary" href="#">Cookies</a>
                        </li>
                        <li className="list-component" style={anchorStyle}>
                            <a className="nav-link-item-bottom text-primary" href="#">Ads info</a>
                        </li>
                        <li className="list-component last" style={anchorStyle}>
                            <a className="nav-link-item-bottom last text-primary" href="#">&copy;fatheladomm</a>
                        </li>
                    </ul>
                </div>
                <button className="navbar-toggler bottom-toggler toggle-btn" type="button">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="more-actions-bottom collapse navbar-collapse" id="navbarToggle">
                    <a className="drops-up-link text-secondary" href="#">Other Options</a>
                </div>
            </div>
            <div className="navbar-bottom-center">
                <div className="collapse navbar-collapse about">
                    <a href="?" className="navbar-brand-about text-secondary">&copy;dommy fathela -kenya</a>
                </div>
            </div>
            <div className="navbar-bottom-right">
                <div className="collapse navbar-collapse about">
                    <a href="?" className="navbar-brand-about text-secondary">@about</a>
                </div>
            </div>
        </footer>
    )
};