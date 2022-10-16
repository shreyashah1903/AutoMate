import * as React from 'react';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import JobCard from './Card';

// Application Status:
// Applied
// Online Assement
// Interview
// Offer
// Rejection

export default function CardColumn({ status, color }) {
  return (
    <Container maxWidth='sm'>
      <Box sx={{ bgcolor: color, height: '100vh', width: '15vw' }}>
        <Typography variant='h5'>{status}</Typography>
        <JobCard />
        <JobCard />
        <JobCard />
      </Box>
    </Container>
  );
}
