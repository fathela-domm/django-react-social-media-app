const HomeComponents = (props) => {
    const [isLoading, setIsLoading] = React.useState(true);
    const determinant = React.useRef("loading");
    let componentsToRender =
        <div className="components">
            <HomeHeaderComponent image={props.image} />
            <UserProfileComponent uid={props.uid} user={props.user} token={props.token} />
            <UserTweetsComponent user={props.user} token={props.token} uid={props.uid} />
            <SearchChatStudio />
            <UserTrendsComponent />
        </div>;
    let loadBar =
        <div className="display">
            <div className="flex text-center loadbar col-sm-12 mt-50">
                <i className="fas fa-circle-notch fa-spin"></i>
            </div >
        </div>;

    React.useEffect(() => {
        setTimeout(() => {
            setIsLoading(false);
            determinant.current = "components rendered";
        }, 1500);
    });
    return isLoading ? loadBar : componentsToRender
}

const renderComponents = (image, user, csrf_token, uid) => {
    ReactDOM.render(<HomeComponents uid={uid} image={image} user={user} token={csrf_token} />, document.querySelector(".home-container"));
};
