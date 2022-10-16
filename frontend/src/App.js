import Box from '@mui/material/Box';
import './App.css';
import Navbar from './components/Navbar';
import CardColumn from './components/CardColumn';

function App() {
  return (
    <div className='App'>
      <Navbar />
      <Box style={{ display: 'flex', flexDirection: 'row', marginTop: '16px' }}>
        <CardColumn status='Applied' color='blue' />
        <CardColumn status='Online Assessment' color='orange' />
        <CardColumn status='Interview' color='yellow' />
        <CardColumn status='Offer' color='green' />
        <CardColumn status='Rejection' color='red' />
      </Box>
    </div>
  );
}

export default App;
