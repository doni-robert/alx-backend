/**
 * Creates a job processor
 */

import { createQueue } from "kue";

queue = createQueue();

const sendNotification = (phoneNumber, message) => {
    console.log(
      `Sending notification to ${phoneNumber},`,
      'with message:',
      message,
    );
  };
  
  queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
  });