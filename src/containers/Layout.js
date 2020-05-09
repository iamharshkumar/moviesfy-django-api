import React from "react";
import {
    Container,
    Divider,
    Dropdown,
    Grid,
    Header,
    Image,
    List,
    Menu,
    Segment
} from "semantic-ui-react";
import {Link, withRouter} from "react-router-dom";
import {connect} from "react-redux";
import {logout} from "../store/actions/auth";

class CustomLayout extends React.Component {
    render() {
        const {authenticated} = this.props;
        const options = [
            {key: 1, text: 'Choice 1', value: 1},
            {key: 2, text: 'Choice 2', value: 2},
            {key: 3, text: 'Choice 3', value: 3},
        ]

        const options1 = [
            {key: 1, text: 'Hollywood', value: 1},
            {key: 2, text: 'Bollywood', value: 2},
        ];
        return (
            <div>
                <Menu inverted>
                    <Container>
                        <Link to="/">
                            <Menu.Item header>MOVIES MANIA</Menu.Item>
                        </Link>
                        <Menu.Menu position='right'>
                            <Link to="/">
                                {/*<Menu.Item>GENRE</Menu.Item>*/}
                                <Dropdown text='GENRE' options={options} simple item/>
                            </Link>
                            <Link to="/">
                                <Dropdown text='TV - SERIES' options={options1} simple item/>

                            </Link>
                            <Link to="/">
                                <Dropdown text='MOVIES' options={options1} simple item/>
                            </Link>

                        </Menu.Menu>
                        {authenticated ? (
                            <Menu.Item header onClick={() => this.props.logout()}>
                                Logout
                            </Menu.Item>
                        ) : (
                            <React.Fragment>
                                <Link to="/login">
                                    {/*<Menu.Item header>Login</Menu.Item>*/}
                                </Link>
                                <Link to="/signup">
                                    {/*<Menu.Item header>Signup</Menu.Item>*/}
                                </Link>
                            </React.Fragment>
                        )}
                    </Container>
                </Menu>

                {this.props.children}


            </div>
        );
    }
}

const mapStateToProps = state => {
    return {
        authenticated: state.auth.token !== null
    };
};

const mapDispatchToProps = dispatch => {
    return {
        logout: () => dispatch(logout())
    };
};

export default withRouter(
    connect(
        mapStateToProps,
        mapDispatchToProps
    )(CustomLayout)
);
