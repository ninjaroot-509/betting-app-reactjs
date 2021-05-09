import React, { Component } from 'react';
import { connect } from 'react-redux';
import mapStoreToProps from '../../redux/mapStoreToProps';
import LoginForm from './LoginForm';
import { withStyles, Container, Grid, Typography } from '@material-ui/core'

const styles = theme => ({
  //not using
});

class LoginPage extends Component {

  componentDidMount(){
    this.props.dispatch({type: 'TOGGLE_NAV'});
  }
  componentWillUnmount(){
    this.props.dispatch({type: 'TOGGLE_NAV'})
  }

  render() {
    
    return (
      <Container>
        <Grid container justify="center" alignItems="center" spacing={4}>
          <Grid item xs={12} style={{textAlign: "center", color: "white"}}>
            <Typography variant="h3" style={{marginTop: "120px"}}>Pari amical</Typography>
          </Grid>
          <Grid item xs={12} style={{textAlign: "center", marginTop: "5px"}}>
            <svg onClick={this.handleInvisibleButton} xmlns="http://www.w3.org/2000/svg" width="130" height="130" viewBox="0 0 1008.88 822.802">
              <path id="Path_76" data-name="Path 76" d="M1889.408-596.257c.225,2.307,6.223,26.156-38.147,34.217-72.306,13.137-228.245,
              10.706-387.456.719-49.807-3.124-112.71-1.116-222.195-11.159-18.178-2.624-58.091-7.3-80.809-14-31.258-10.159-24.673-10.855-40.245-14.066-6.578-3.861-19-9.809-27.741-14.066-15.33-7.469-30.55-17.3-41.417-21.1-29.167-10.2-39.2-7.541-39.2-7.541s-22.839-294.223.124-333.56c28.952-14.57,
              39.222-34.078,67.6-64.079,17.078-18.057,55.61-44.915,80.88-84.787,37.436-44.656,57.7-64.956,82.833-112.137,11.218-20.565,25.675-45.629,
              32.039-63.688,6.642-26.178,10.7-66.651,34.131-70,14.483-4.483,30.267,3.5,41.669,9.436,24.832,12.935,37.887,40.459,39.854,72.675.764,
              12.522-14.884,43.087-30.476,73.065-14.768,28.391-26.117,57.749-29.844,72.477-3.118,12.323-8.925,51.857,10.308,70.919,8.17,8.1,51.575,11.722,140.27,
              12.5,106.277-2.735,177.679-19.808,290.221-34.32,14.721-1.9,88.906-14.712,134.711-5.534,22.992,4.607,33.643,23.21,36.9,39.854,2.5,12.779,1.376,29.821-9.8,
              37.9-11.57,8.363-3.533,4.172-30.13,13.708-38.486,13.8-113.493,21.141-177.766,29.464-14.879,3.208-61.508,12.026-94.88,20.907-44.508,11.844-73.755,24.285-52.623,
              27.876,29.131,4.95,124.728-10.047,198.031-13.522,26.667-1.264,93.761-7.636,157.369,0,30.068,3.609,55.631,9.482,66.854,22.458,1.88,2.172,2.738,2.665,4.452,5.472.812,1.32,2.139,4.268,2.1,
              6.1-.471.274.894,9.024.86,10.44a46.165,46.165,0,0,0,0,5.746c.237,3.8-.377,6.361,0,10.446.294,3.184-4.311,13.076-7.417,16.778-3.126,3.728-4.378,3.146-4.378,3.146.083,1.516-6.842,3.333-10.26,
              5.062-14.964,7.576-61.117,15.544-139.314,18.775-16.019,4.3-51.907,1.337-70.271,4.072-28.59.243-41.961-.352-65.7,1.789-42.378,3.821-74.546,7.124-97.29,10.94-6.092,1.022-53.9,11.306-27.713,
              15.57,25.848,6.612,6.4,4.478,52.9,11.121,11.792,1.11,60.888,6.854,117.217,7.559,51.039.639,107.02-7.329,150.858,0,18.694,3.125,38.813,6.714,49.245,13.872,13.844,9.5,14.5,23.167,15.953,
              28.668,1.6,6.058-4.178,26.544-22.657,39.535-12.821,9.014-34.248,11.239-54.331,15.49-18.8,3.979-29.438,4.69-53.869,5.549-18.675.656-54.1,1.85-54.1,1.85s-109.938-1.5-173.5,3.006c-40.716,
              2.884-44.453,10.621-45.906,15.028-.368,1.116-1.05,3.912,5.318,6.7,9.227,4.048,28.565,8.5,40.589,10.4,15.259,2.412,53.335,6.466,99.516,8.554,44.287,2,96.427,1.976,128.083,8.092,57.716,
              11.151,48.551,35.6,48.551,35.6" transform="translate(-1000.554 1374.298)" fill="#fff" stroke="#707070" strokeLinecap="round" strokeLinejoin="round" strokeWidth="3"/>
            </svg>
          </Grid>
          <Grid item xs={12} style={{textAlign: "center"}}>
            <LoginForm loginInfo={this.state}/>
          </Grid>
        </Grid>
      </Container>
    );
  }
}

const LoginPageStyled = withStyles(styles)(LoginPage);
export default connect(mapStoreToProps)(LoginPageStyled);