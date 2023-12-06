/** 
 * Creates a job creator
 * 
*/
import { createQueue } from 'kue';


const queue = createQueue();

const job = queue.create('push_notification_code', {
    phoneNumber: '0000777',
    message: 'Active',
  });
  
  job
    .on('enqueue', () => {
      console.log('Notification job created:', job.id);
    })
    .on('complete', () => {
      console.log('Notification job completed');
    })
    .on('failed attempt', () => {
      console.log('Notification job failed');
    });
  job.save();