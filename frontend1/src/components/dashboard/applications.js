import { formatDistanceToNow, subHours, format, parseISO } from 'date-fns';
import { v4 as uuid } from 'uuid';
import {
  Box,
  Button,
  Card,
  CardHeader,
  Divider,
  IconButton,
  List,
  ListItem,
  ListItemAvatar,
  ListItemText
} from '@mui/material';
import ArrowRightIcon from '@mui/icons-material/ArrowRight';
import MoreVertIcon from '@mui/icons-material/MoreVert';

const jobs = [
  {
    id: uuid(),
    name: 'Dropbox',
    imageUrl: '/static/images/jobs/product_1.png',
    role: 'Software Engineer Intern',
    deadline: subHours(Date.now(), 2),
    status: 'APPLIED'
  },
  {
    id: uuid(),
    name: 'Medium Corporation',
    imageUrl: '/static/images/jobs/product_2.png',
    role: 'Software testing Intern',
    deadline: subHours(Date.now(), 2),
    status: 'APPLIED'
  },
  {
    id: uuid(),
    name: 'Slack',
    imageUrl: '/static/images/jobs/product_3.png',
    role: 'Software Engineer Intern',
    deadline: subHours(Date.now(), 3),
    status: 'OA'
  },
  {
    id: uuid(),
    name: 'Lyft',
    imageUrl: '/static/images/jobs/product_4.png',
    role: 'Software Testing Intern',
    deadline: subHours(Date.now(), 5),
    status: 'INTERVIEW'
  },
  {
    id: uuid(),
    name: 'GitHub',
    imageUrl: '/static/images/jobs/product_5.png',
    role: 'Product Management Intern',
    deadline: subHours(Date.now(), 9),
    status: 'OFFER'
  },
  {
    id: uuid(),
    name: 'Squarespace',
    imageUrl: '/static/images/jobs/product_6.png',
    role: 'Product Management Intern',
    deadline: subHours(Date.now(), 9),
    status: 'REJECTED'
  }
];

export const Applications = (props) => (
  console.log(props),
  <Card {...props}>
    <CardHeader
      subtitle={`${jobs.length} in total`}
      title={props.titleToShow}
    />
    <Divider />
    <List>
      {jobs.filter(product => props.status.includes(product.status)).map((product, i) =>
        (<ListItem
          divider={i < jobs.length - 1}
          key={product.id}
        >
          <ListItemAvatar>
            <img
              alt={product.name}
              src={product.imageUrl}
              style={{
                height: 48,
                width: 48
              }}
            />
          </ListItemAvatar>
          <ListItemText
            primary={product.name}
            secondary={`${format(product.deadline, "dd-MM-yyyy")}`}
          />
          <ListItemText
              secondary={product.role}
          />
          <IconButton
            edge="end"
            size="small"
          >
          </IconButton>
        </ListItem>
        )
      )}
    </List>
    {/* <Divider />
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'flex-end',
        p: 2
      }}
    >
      <Button
        color="primary"
        endIcon={<ArrowRightIcon />}
        size="small"
        variant="text"
      >
        View all
      </Button>
    </Box> */}
  </Card>
);
