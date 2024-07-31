
export default function createPushNotificationsJobs(jobs, queue) {
	if (!(Array.isArray(jobs))) {
		throw new Error("Jobs is not an array");
	};
	for (let jobData of jobs) {
		let job = queue.create('', jobData)
		job
		 .on('complete', () => {
		  console.log(`Notification job ${job.id} completed`);
		})
		 .on('failed', (err) => {
		  console.log(`Notification job ${job.id} failed: ${err}`);
		})

		 .on('progress', (progress, data) => {
			console.log(`Notification job ${job.id} ${progress}% complete`);
		})

		.save((error) => {
		  if (!error) {
		    console.log(`Notification job created: ${job.id}`);
		  }
		});
	}
}
