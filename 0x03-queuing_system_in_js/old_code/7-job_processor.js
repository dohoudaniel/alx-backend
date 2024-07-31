import { createQueue } from 'kue';

const blacklisted = ['4153518781', '4153518780']

function sendNotification(phoneNumber, message, job, done) {
	for (let i = 0; i <= 100; i++) {
		if (i === 0 || i === 50) {
			job.progress(i, 100);
			if (i === 50) {
				console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
			};
		};
		if (blacklisted.includes(job.data.phoneNumber)) {
                        const err = new Error(`Phone number ${job.data.phoneNumber} is blacklisted`);
                        return done(err);
                }
	}
	return done();
}
const queue = createQueue()
queue.process('push_notification_code_2', 2, (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

