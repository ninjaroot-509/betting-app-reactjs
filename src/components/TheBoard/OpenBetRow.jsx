import React from 'react';
import { connect } from 'react-redux';
import { makeStyles } from '@material-ui/core/styles';
import { Button, TableCell, TableRow, Typography, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle } from '@material-ui/core';

const useStyles = makeStyles({
  table: {
    width: 600,
    height: 50
  },
});

function OpenBetRow(props) {
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  function acceptBet() {
    //sends this payload if spread bet
    if (props.bet.proposers_team_id) {
      props.dispatch({
        type: 'ACCEPT_BET',
        payload:
        {
          bet_id: props.bet.id,
          acceptors_team_id: props.bet.acceptors_team_id
        }
      }) 
    } else {
      //or sends this payload if over/under
      props.dispatch({
        type: 'ACCEPT_BET',
        payload:
          {
            bet_id: props.bet.id,
            bet_is_over_under: true
          }
      })
    }
    //regardless, closes the dialog
    handleClose();
  }

  return (
    <>
      <TableRow onClick={handleClickOpen}>
        {/* Friend */}
        <TableCell style={{color: 'white'}} align="left">{props.bet.proposers_first_name} {props.bet.proposers_last_name}</TableCell>
        {/* Game */}
        <TableCell style={{color: 'white'}} align="left">{props.bet.away_team_abbr} @ {props.bet.home_team_abbr}</TableCell>
        {/* Bet */}
        {/* determines if bet is spread or O/U */}
        {props.bet.proposers_team_id ? 
          <TableCell align="left" style={{color: 'white'}}>
            {/* checks if proposer is home team */}
            {props.bet.proposers_team_is_home_team ?
              <Typography variant="body2">{props.bet.home_team_name} <br/>{props.bet.home_team_spread > 0 && '+'}{props.bet.home_team_spread}</Typography>
              :
              <Typography variant="body2">{props.bet.away_team_name} <br/>{props.bet.away_team_spread > 0 && '+'}{props.bet.away_team_spread}</Typography>
            }
          </TableCell>
        :
          <TableCell align="left" style={{color: 'white'}}>
            {/* determines if proposer compte plus */}
            {props.bet.proposers_bet_is_over ?
              <Typography variant="body2">Plus de <br/>{props.bet.over_under}</Typography>
              :
              <Typography variant="body2">En dessous de <br/>{props.bet.over_under}</Typography>
            } 
          </TableCell>
      }
        {/* Wager */}
        <TableCell style={{color: 'white'}} align="center">{props.bet.wager}u</TableCell>
      </TableRow>
      <>
        <Dialog
          open={open}
          onClose={handleClose}
          aria-labelledby="alert-dialog-title"
          aria-describedby="alert-dialog-description"
        >
          <DialogTitle id="alert-dialog-title">{`Take this Bet?`}</DialogTitle>
          <DialogContent>
            {/* displays different confirmation text depending if the bet is spread or over/under */}
            {props.bet.proposers_team_id ?
              <>
              {/* spread options */}
              {props.bet.proposers_team_is_home_team ? 
                <DialogContentText id="alert-dialog-description">
                  {props.bet.proposers_first_name} a la {props.bet.home_team_name} {props.bet.home_team_spread > 0 && '+'}{props.bet.home_team_spread} for {props.bet.wager} units this week.
                  <br/>
                  Voulez-vous prendre le {props.bet.away_team_name} {props.bet.away_team_spread > 0 && '+'}{props.bet.away_team_spread}?
                </DialogContentText>
              :
                <DialogContentText id="alert-dialog-description">
                  {props.bet.proposers_first_name} a la {props.bet.away_team_name} {props.bet.away_team_spread > 0 && '+'}{props.bet.away_team_spread} for {props.bet.wager} units this week.
                  <br/>
                  Voulez-vous prendre le {props.bet.home_team_name} {props.bet.home_team_spread > 0 && '+'}{props.bet.home_team_spread}?
                </DialogContentText>
              }
              </>
            :
            <>
              {/* over/under options */}
              {props.bet.proposers_bet_is_over ?
                <DialogContentText id="alert-dialog-description">
                  {props.bet.proposers_first_name} compte plus {props.bet.over_under} pour le {props.bet.away_team_name} au {props.bet.home_team_name}.
                  <br />
                  Voulez-vous prendre le sous?
                </DialogContentText>
              :
                <DialogContentText id="alert-dialog-description">
                  {props.bet.proposers_first_name} a sous {props.bet.over_under} pour le {props.bet.away_team_name} au {props.bet.home_team_name}.
                  <br />
                  Voulez-vous prendre la fin?
                </DialogContentText>
              }
            </>
          }
          </DialogContent>
          <DialogActions>
            <Button onClick={handleClose} >
              Cancel
          </Button>
            <Button onClick={acceptBet} >
              Accept Bet
          </Button>
          </DialogActions>
        </Dialog>
      </>
    </>
  );
}

export default connect()(OpenBetRow);