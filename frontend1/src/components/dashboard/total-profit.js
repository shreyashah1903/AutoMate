import { Avatar, Card, CardContent, Grid, Typography } from '@mui/material';
import CancelIcon from '@mui/icons-material/Cancel';

export const TotalProfit = (props) => (
  <Card {...props}>
    <CardContent>
      <Grid
        container
        spacing={3}
        sx={{ justifyContent: 'space-between' }}
      >
        <Grid item>
          <Typography
            color="textSecondary"
            gutterBottom
            variant="overline"
          >
            TOTAL REJECTIONS
          </Typography>
          <Typography
            color="textPrimary"
            variant="h4"
          >
            35
          </Typography>
        </Grid>
        <Grid item>
          <Avatar
            sx={{
              backgroundColor: 'error.main',
              height: 56,
              width: 56
            }}
          >
            <CancelIcon />
          </Avatar>
        </Grid>
      </Grid>
    </CardContent>
  </Card>
);
