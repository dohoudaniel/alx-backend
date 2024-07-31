import { createQueue } from 'kue';

// Define the job data object
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is the notification message to verify your account',
};

const queue = createQueue()
const job = queue.create('push_notification_code', jobData);

// Event handler for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event handler for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save((error) => {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  }
});
